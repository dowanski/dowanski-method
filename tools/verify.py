#!/usr/bin/env python3
"""Verify the local distribution contract, not universal agent behavior."""
import copy
import hashlib
import io
from pathlib import Path
import posixpath
import re
import shutil
import stat
import tempfile
import unittest
from urllib.parse import unquote
import zipfile

import package

ROOT = package.ROOT
BOOT = ["README.md", "AGENTS.md", "qdi/README.md", "qdi/CURRENT_STATE.md", "qdi/ACTIVE_PACKET.md"]
PHASES = {
    "SEED": ["DISCOVERY_ANCHORS.md"],
    "ANCHOR_DISCOVERY": ["DISCOVERY_ANCHORS.md"],
    "BRANCH_PLANNING": ["BRANCH_PLAN.md", "lenses/README.md"],
    "SPECIALIST_DISCOVERY": ["BRANCH_PLAN.md", "SPECIALIST_BRANCH_GUIDE.md"],
    "SIDEQUEST_ACTIVE": ["SIDEQUEST_TEMPLATE.md"],
    "CONVERGENCE": ["PRE_BUILD_BLUEPRINT.md"],
    "OWNER_REVIEW": ["OWNER_REVIEW.md"],
    "APPROVED_FOR_HANDOFF": ["OWNER_REVIEW.md", "QDI_TO_DM_HANDOFF.md", "../dm-foundations/README.md"],
    "DEFERRED": [], "STOPPED": [],
}


def section(text, heading):
    parts = text.split(f"## {heading}\n", 1)
    return re.split(r"^## ", parts[1], maxsplit=1, flags=re.M)[0] if len(parts) == 2 else ""


def links(text):
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def link_errors(files):
    errors = []
    for source, text in files.items():
        for raw in links(text):
            target = unquote(raw.strip().strip("<>"))
            if target.startswith(("https://", "http://", "mailto:")):
                continue
            path, _, anchor = target.partition("#")
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), path)) if path else source
            if resolved.startswith(("../", "/")) or resolved not in files:
                errors.append(f"Missing/outside link: {source} -> {target}")
            elif anchor and resolved.endswith(".md"):
                headings = re.findall(r"^#{1,6}\s+(.+)$", files[resolved], flags=re.M)
                slugs = [re.sub(r"[^\w\s-]", "", h.lower()).replace(" ", "-") for h in headings]
                if anchor not in slugs:
                    errors.append(f"Missing heading: {source} -> {target}")
    return errors


def route_errors(files):
    errors = []
    needed = set(BOOT + ["INSTALLATION_AND_STORAGE.md", "qdi/BRANCH_PLAN.md",
                        "qdi/DISCOVERY_LEDGER.md", "qdi/QDI_TO_DM_HANDOFF.md",
                        "dm-foundations/README.md", "dm-foundations/ADAPTING_A_FOUNDATION.md"])
    if not needed.issubset(files):
        return ["Required routing document is missing"]
    agent, router = files["AGENTS.md"], files["qdi/README.md"]
    if links(section(agent, "Boot route")) != [p for p in BOOT if p != "AGENTS.md"]:
        errors.append("Boot route/order changed or inactive context was added")
    if sum(len(files[p].split()) for p in BOOT + ["INSTALLATION_AND_STORAGE.md"]) > 4200:
        errors.append("First-session route exceeds 4,200 words")
    rows = {}
    for row in section(router, "Phase routes").splitlines():
        cells = [v.strip() for v in row.split("|")]
        if len(cells) >= 5 and re.fullmatch(r"`[A-Z_]+`", cells[1]):
            rows[cells[1].strip("`")] = cells[2:4]
    if list(rows) != list(PHASES):
        errors.append("The ten phase routes differ")
    for phase, targets in PHASES.items():
        row = rows.get(phase, ["", ""])
        if links(" ".join(row)) != targets or not row[1]:
            errors.append(f"Phase targets or advance/stop rule differs: {phase}")
    for phrase in ("only with explicit generation authority", "accepted setup authority"):
        if phrase not in " ".join(rows.get("APPROVED_FOR_HANDOFF", [])):
            errors.append("Handoff authority guard is missing")
    if "exact saved phase and return point" not in " ".join(rows.get("SIDEQUEST_ACTIVE", [])):
        errors.append("Sidequest return guard is missing")
    if "restart condition and human direction" not in " ".join(rows.get("DEFERRED", [])):
        errors.append("Deferred restart guard is missing")
    if "Human explicitly reopens" not in " ".join(rows.get("STOPPED", [])):
        errors.append("Stopped restart guard is missing")
    for name, pattern in (("qdi/CURRENT_STATE.md", r"Active phase: `SEED`"),
                          ("qdi/ACTIVE_PACKET.md", r"Phase: `SEED`")):
        if not re.search(pattern, files[name]):
            errors.append("Initial phase/state mismatch")
    event = section(router, "Conditional event routes")
    for target in ("../INSTALLATION_AND_STORAGE.md", "DISCOVERY_LEDGER.md", "lenses/README.md",
                   "SIDEQUEST_TEMPLATE.md", "QDI_RECORD_INDEX.md", "CONTEXT_CLEANUP_CHECKPOINT.md",
                   "../CONTEXT_AND_TOKEN_STEWARDSHIP.md", "archive/README.md"):
        if target not in links(event):
            errors.append(f"Conditional event route is missing: {target}")
    graph = {}
    for name, body in files.items():
        targets = links(body) + re.findall(r"`([^`\n]+\.md)`", body)
        graph[name] = [posixpath.normpath(posixpath.join(posixpath.dirname(name), p.split("#")[0]))
                       for p in targets if not p.startswith(("http", "mailto:", "#"))]
    seen, pending = set(), ["qdi/README.md"]
    while pending:
        item = pending.pop()
        if item in seen or item not in files:
            continue
        seen.add(item)
        pending.extend(graph.get(item, []))
    if any(p.startswith("qdi/") and p not in seen for p in files):
        errors.append("Unreachable QDI module")
    persistent = " ".join(agent.split())
    for phrase in ("Mandatory pushback", "stop before a third unchanged attempt",
                   "Exact usage requires actual telemetry", "Archived information has no current authority",
                   "Never place secrets or unnecessary sensitive data in Markdown",
                   "Do not trade away required quality", "stop for review before implementation"):
        if phrase not in persistent:
            errors.append(f"Persistent control is missing: {phrase}")
    controls = [section(files.get(f"dm-foundations/{w}/AGENTS.md", ""), "Continuing controls")
                for w in ("light", "standard", "governed")]
    if not controls[0] or len(set(controls)) != 1:
        errors.append("Foundation continuing controls are missing or inconsistent")
    for phrase in ("Challenge drift, contradictions, unsupported claims", "one canonical writer",
                   "Reserve capacity for verification", "stop before a third unchanged attempt",
                   "exact usage only from actual telemetry", "Efficiency never waives required quality",
                   "Before pause or handoff", "At closure or documentation drag", "linked QDI successor"):
        if phrase not in " ".join(controls[0].split()):
            errors.append(f"Continuing responsibility missing: {phrase}")
    if "Preserve the selected foundation's Continuing controls" not in files["qdi/QDI_TO_DM_HANDOFF.md"]:
        errors.append("Handoff drops continuing controls")
    receiver = files["dm-foundations/README.md"]
    if "Inspect only `light/`, `standard/`, or `governed/`—never all three" not in receiver:
        errors.append("Foundation selection isolation missing")
    if "Stop before implementation" not in receiver:
        errors.append("Receiver implementation gate missing")
    index = "dm-foundations/governed/docs/workstreams/01-governed-workstream/WORK_PACKET_INDEX.md"
    if "`packets/01-WORK_PACKET.md`" not in files.get(index, ""):
        errors.append("Governed packet target is wrong")
    labels = re.findall(r"^- `([A-Z_]+)`", section(files["qdi/DISCOVERY_LEDGER.md"], "Evidence classifications"), flags=re.M)
    if labels != ["OWNER_STATEMENT", "OBSERVED", "SOURCED", "INFERENCE", "ASSUMPTION",
                  "UNKNOWN", "CONTRADICTION", "DEFERRED", "NOT_APPLICABLE", "OWNER_CONFIRMED"]:
        errors.append("Evidence classifications are missing, duplicated, or changed")
    cycles = []
    for line in section(files.get("qdi/QDI_RECORD_INDEX.md", ""), "Record index").splitlines():
        cells = [c.strip().strip("`") for c in line.split("|")]
        if len(cells) >= 9 and re.fullmatch(r"QDI-C\d+", cells[1]):
            cycles.append(cells[1])
            if cells[4] == "ACTIVE" and "qdi/" + cells[5] not in files:
                errors.append("Active cycle ID has a missing path")
    match = re.search(r"Active QDI Cycle ID: `([^`]+)`", files["qdi/CURRENT_STATE.md"])
    if cycles != ([match[1]] if match else []):
        errors.append("Cycle ID is duplicated or inconsistent with Current State")
    errors.extend(link_errors(files))
    return errors


class DistributionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source, cls.version = package.source_files()
        cls.docs = {k: v.decode("utf-8") for k, v in cls.source.items() if k.endswith(".md")}

    def test_inventory_and_privacy(self):
        self.assertEqual(len(self.source), 96)
        pattern = re.compile(r"/Users/[A-Za-z]|/home/[A-Za-z]|AKIA[0-9A-Z]{16}|ghp_[0-9A-Za-z]{36}|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY")
        for path, data in self.source.items():
            self.assertIsNone(pattern.search(data.decode()), path)
        for path in ROOT.rglob("*"):
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            self.assertFalse(path.is_symlink(), str(path))
            if path.is_file() and path.suffix in (".md", ".json", ".yml"):
                self.assertIsNone(pattern.search(path.read_text()), str(path))
        for control in BOOT + ["INSTALLATION_AND_STORAGE.md"]:
            if control not in ("qdi/CURRENT_STATE.md", "qdi/ACTIVE_PACKET.md"):
                self.assertNotRegex(self.docs[control], r"\{\{[^}]+\}\}")

    def test_repository_links(self):
        files = {p.relative_to(ROOT).as_posix(): p.read_text() for p in ROOT.rglob("*.md")}
        self.assertEqual(link_errors(files), [])

    def test_routing_contract(self):
        self.assertEqual(route_errors(self.docs), [])
        self.assertEqual(sum(p.startswith("qdi/") for p in self.docs), 20)

    def test_routing_fault_injection(self):
        mutations = [
            ("missing target", "qdi/BRANCH_PLAN.md", None, None),
            ("handoff authority", "qdi/README.md", "only with explicit generation authority", "when convenient"),
            ("archive preload", "AGENTS.md", "## Boot route\n", "## Boot route\n[History](qdi/archive/README.md)\n"),
            ("startup excess", "README.md", None, " redundant" * 600),
            ("phase mismatch", "qdi/ACTIVE_PACKET.md", "Phase: `SEED`", "Phase: `SPECIALIST_DISCOVERY`"),
            ("sidequest return", "qdi/README.md", "exact saved phase and return point", "a new topic"),
            ("packet path", "dm-foundations/governed/docs/workstreams/01-governed-workstream/WORK_PACKET_INDEX.md", "packets/01-WORK_PACKET.md", "01-WORK_PACKET.md"),
            ("dropped control", "dm-foundations/light/AGENTS.md", "Challenge drift, contradictions, unsupported claims", "Agree with everything"),
            ("classification missing", "qdi/DISCOVERY_LEDGER.md", "- `ASSUMPTION`", "- `UNCLASSIFIED`"),
            ("cycle mismatch", "qdi/CURRENT_STATE.md", "Active QDI Cycle ID: `QDI-C01`", "Active QDI Cycle ID: `QDI-C02`"),
            ("active ID path", "qdi/QDI_RECORD_INDEX.md", "| ACTIVE | `CURRENT_STATE.md`", "| ACTIVE | `MISSING.md`"),
        ]
        for name, path, old, new in mutations:
            with self.subTest(name=name):
                changed = copy.copy(self.docs)
                if new is None:
                    del changed[path]
                elif old is None:
                    changed[path] += new
                else:
                    self.assertIn(old, changed[path])
                    changed[path] = changed[path].replace(old, new, 1)
                self.assertTrue(route_errors(changed))

    def test_reproducible_archives_and_extraction(self):
        first, second = package.artifacts(), package.artifacts()
        self.assertEqual(first, second)
        manifest = dict(line.split("  ", 1)[::-1] for line in first["SHA256SUMS.txt"].decode().splitlines())
        self.assertEqual(len(manifest), 4)
        for filename, digest in manifest.items():
            self.assertEqual(hashlib.sha256(first[filename]).hexdigest(), digest)
            label = filename.removeprefix("dowanski-method-").split("-v", 1)[0]
            root = filename.removesuffix(".zip")
            with zipfile.ZipFile(io.BytesIO(first[filename])) as archive:
                names = archive.namelist()
                self.assertEqual(len(names), len(set(names)))
                expected = self.source if label == "complete" else {
                    p.removeprefix(f"dm-foundations/{label}/"): data
                    for p, data in self.source.items() if p.startswith(f"dm-foundations/{label}/")}
                if label != "complete":
                    expected = {**expected, "VERSION": self.source["VERSION"],
                                "LICENSE-TEMPLATES.md": self.source["LICENSE-TEMPLATES.md"],
                                "NOTICE.md": (ROOT / "tools/direct-notice.md").read_bytes()}
                self.assertEqual(sorted(names), sorted(f"{root}/{p}" for p in expected))
                for info in archive.infolist():
                    self.assertTrue(package.valid_path(info.filename))
                    self.assertTrue(stat.S_ISREG(info.external_attr >> 16))
                    self.assertEqual(info.compress_type, zipfile.ZIP_STORED)
                with tempfile.TemporaryDirectory(prefix="dm-extract-") as temp:
                    archive.extractall(temp)  # Names and types verified above.
                    for p, content in expected.items():
                        self.assertEqual((Path(temp) / root / p).read_bytes(), content)

    def test_active_base_installation(self):
        for weight in ("light", "standard", "governed"):
            with tempfile.TemporaryDirectory(prefix="dm-install-") as temp:
                target = Path(temp)
                base = ROOT / "starter/dm-foundations" / weight
                for name in ("README.md", "AGENTS.md"):
                    shutil.copyfile(base / name, target / name)
                shutil.copytree(base / "docs", target / "docs")
                self.assertFalse((target / "_optional").exists())
                self.assertFalse((target / "_examples").exists())
                self.assertFalse((target / "qdi").exists())
                self.assertIn("## Continuing controls", (target / "AGENTS.md").read_text())

    def test_unsafe_source_and_output_refused(self):
        with tempfile.TemporaryDirectory(prefix="dm-safety-") as temp:
            temp = str(Path(temp).resolve())
            fixture = Path(temp) / "repo"
            shutil.copytree(ROOT / "starter", fixture / "starter")
            shutil.copytree(ROOT / "tools", fixture / "tools", ignore=shutil.ignore_patterns("__pycache__"))
            unknown = fixture / "starter/.unexpected"
            unknown.write_text("must not enter the archive")
            with self.assertRaises(ValueError):
                package.source_files(fixture)
            unknown.unlink()
            linked = fixture / "starter/linked.md"
            linked.symlink_to(fixture / "starter/README.md")
            with self.assertRaises(ValueError):
                package.source_files(fixture)
            linked.unlink()
            version_file = fixture / "starter/VERSION"
            version_file.write_text("../../outside")
            with self.assertRaises(ValueError):
                package.source_files(fixture)
            version_file.write_bytes(self.source["VERSION"])
            with self.assertRaises(ValueError):
                package.write_artifacts(fixture / "output", fixture)
            with self.assertRaises(ValueError):
                package.write_artifacts(Path(temp), fixture)
            fresh = package.write_artifacts(Path(temp) / "fresh", fixture)
            self.assertEqual(len(list(fresh.iterdir())), 5)
            with self.assertRaises(ValueError):
                package.write_artifacts(fresh, fixture)

    def test_license_scope(self):
        self.assertIn("qdi/", self.docs["NOTICE.md"])
        self.assertIn("MIT", self.docs["NOTICE.md"])
        self.assertIn("LICENSE-TEMPLATES.md", (ROOT / "tools/direct-notice.md").read_text())
        for name in ("LICENSE-TEMPLATES.md", "LICENSE-CONTENT.md"):
            self.assertEqual((ROOT / name).read_bytes(), self.source[name])


if __name__ == "__main__":
    unittest.main(verbosity=2)
