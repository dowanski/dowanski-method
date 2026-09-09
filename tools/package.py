#!/usr/bin/env python3
"""Build deterministic, allowlisted review archives. No network or publishing."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

ROOT = Path(__file__).resolve().parent.parent
MAX_FILE = 4 * 1024 * 1024
MAX_TOTAL = 16 * 1024 * 1024
VERSION_RE = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?")


def regular_bytes(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Expected a regular, non-symlink file: {path.name}")
    if path.stat().st_size > MAX_FILE:
        raise ValueError(f"File exceeds the packaging limit: {path.name}")
    return path.read_bytes()


def valid_path(name):
    path = PurePosixPath(name)
    return (isinstance(name, str) and bool(name) and not path.is_absolute()
            and all(part not in ("", ".", "..") for part in name.split("/"))
            and re.fullmatch(r"[A-Za-z0-9_./-]+", name) is not None
            and not any(part.startswith(".") for part in path.parts))


def source_files(root=ROOT):
    starter = root / "starter"
    if starter.is_symlink() or not starter.is_dir():
        raise ValueError("starter must be a real directory")
    inventory = json.loads(regular_bytes(root / "tools/starter-files.json"))
    if (not isinstance(inventory, list) or not inventory
            or any(not isinstance(p, str) or not valid_path(p) for p in inventory)
            or inventory != sorted(set(inventory))):
        raise ValueError("Starter inventory must contain sorted, unique safe paths")
    found = []
    for path in starter.rglob("*"):
        if path.is_symlink():
            raise ValueError("Symlinks are not allowed in the starter")
        if path.is_file():
            found.append(path.relative_to(starter).as_posix())
        elif not path.is_dir():
            raise ValueError("Special files are not allowed in the starter")
    if sorted(found) != inventory:
        raise ValueError("Starter files differ from the reviewed allowlist")
    result = {name: regular_bytes(starter / name) for name in inventory}
    if sum(map(len, result.values())) > MAX_TOTAL:
        raise ValueError("Starter exceeds the total packaging limit")
    version = result["VERSION"].decode("ascii").strip()
    if not VERSION_RE.fullmatch(version):
        raise ValueError("VERSION must be a safe three-part version with optional prerelease")
    return result, version


def zip_bytes(name, files):
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as archive:
        for path, content in sorted(files.items()):
            if not valid_path(path):
                raise ValueError("Unsafe archive path")
            info = zipfile.ZipInfo(f"{name}/{path}", date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, content)
    return output.getvalue()


def artifacts(root=ROOT):
    files, version = source_files(root)
    packages = {"complete": files}
    direct_notice = regular_bytes(root / "tools/direct-notice.md")
    for weight in ("light", "standard", "governed"):
        prefix = f"dm-foundations/{weight}/"
        selected = {p[len(prefix):]: data for p, data in files.items() if p.startswith(prefix)}
        if not selected:
            raise ValueError(f"Missing foundation: {weight}")
        selected.update({"VERSION": files["VERSION"],
                         "LICENSE-TEMPLATES.md": files["LICENSE-TEMPLATES.md"],
                         "NOTICE.md": direct_notice})
        packages[weight] = selected
    archives = {}
    for label, content in packages.items():
        name = f"dowanski-method-{label}-v{version}"
        archives[name + ".zip"] = zip_bytes(name, content)
    hashes = "".join(f"{hashlib.sha256(data).hexdigest()}  {name}\n"
                     for name, data in sorted(archives.items()))
    archives["SHA256SUMS.txt"] = hashes.encode("ascii")
    return archives


def write_artifacts(output, root=ROOT):
    output = Path(output).absolute()
    # Refuse symlinked destinations and existing output rather than overwriting.
    if any(p.is_symlink() for p in (output, *output.parents)):
        raise ValueError("Output must not use a symlink")
    output, root = output.resolve(), root.resolve()
    if output == root or root in output.parents:
        raise ValueError("Keep generated artifacts outside the source repository")
    if output.exists():
        raise ValueError("Choose a new output directory; existing output is never overwritten")
    built = artifacts(root)
    output.mkdir(parents=True, exist_ok=False)
    for name, data in built.items():
        with (output / name).open("xb") as target:
            target.write(data)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="A new directory outside this repository")
    args = parser.parse_args()
    try:
        result = write_artifacts(args.output)
    except (ValueError, OSError, KeyError, UnicodeError, json.JSONDecodeError) as error:
        parser.exit(1, f"Packaging refused: {error}\n")
    print(f"Created four ZIPs and SHA256SUMS.txt in {result}")
