# Fictional Example — Correct a Navigation Overlap

Status: Example only; never active project authority  
Fictional project: Northstar Notes

## Outcome

At widths from 768px through 900px, the navigation title and local-time label no
longer overlap. Existing desktop and small-mobile behavior remains unchanged.

## Starting evidence

- The overlap is visible at 834×1112 in the local browser.
- No horizontal overflow occurs before the repair.
- The relevant layout is controlled by one responsive stylesheet.

## Scope

Included:

- the affected header spacing and intermediate type scale;
- local responsive verification at 768px, 834px, and 900px.

Not included:

- header redesign;
- copy changes;
- production publication;
- unrelated responsive cleanup.

## Authority

Allowed: inspect and edit the header component and its stylesheet; run the local
site and visual checks.

Requires new authority: committing, publishing, or changing unrelated routes.

## Execution

1. Confirm the exact elements and breakpoint causing the collision.
2. Add the smallest intermediate responsive adjustment.
3. Preserve existing desktop and mobile behavior.
4. Capture local verification at the named widths.

## Verification

| Claim | Required evidence | Result |
|---|---|---|
| Labels no longer collide | Visual captures at all three widths | Pending in this fictional example |
| No horizontal overflow | Browser width check at all three widths | Pending in this fictional example |
| Desktop and mobile remain unchanged | Comparison at 1440px and 390px | Pending in this fictional example |

## Stop conditions

Stop if the repair requires new markup, changes desktop navigation, or reveals
that the collision comes from a different shared component.

## Closeout

This example intentionally contains no claimed implementation result. A real
packet earns its result only after matched evidence and the required review.

