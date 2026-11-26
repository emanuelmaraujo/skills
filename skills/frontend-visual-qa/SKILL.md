---
name: frontend-visual-qa
description: "Use when comparing rendered web screens and investigating responsive or visual regressions; do not use as the primary reviewer of API-only PRs."
---

# frontend-visual-qa

Apply the [shared execution and delivery guide](references/quality-gates.md). Use audit mode for visual comparison. Check changed routes, approved baseline, project breakpoints, supported devices and existing test tooling before selecting coverage.

## Procedure

1. Use the project's viewport matrix and check both sides of affected breakpoints where relevant. If the project has no matrix, derive sizes from layout and target devices. With no reliable project data, choose representative phone, tablet and desktop widths and record the assumption. Include relevant orientations, themes and realistic text lengths.
2. Open the real route with representative data and role. Inspect clipping, wrapping, overflow, stacking, fonts, images, layout shift, menus, dialogs and scrolling. Reuse the accessibility specialist's evidence for keyboard, focus and reduced motion.
3. Use existing fixtures or permitted browser controls. On a disposable environment, seed empty and dense lists. For loading, have the existing fixture or network interception hold the affected request pending. For error, return the status defined by the scenario (for example, a 500 from the order service), or simulate the supported network failure. Capture loading before releasing the response, then check success. Verify the error message and retry or recovery. Use a restricted test session for access denied where applicable.
4. Without automation, use an available browser with resizing or device emulation. Use existing fixtures or native network controls only where they reproduce the intended state. Mark uncovered states BLOCKED and give repeatable steps. Keep baseline updates disabled in audit mode.
5. If fixes are in scope, rerun under the original conditions. Support fidelity claims with side-by-side evidence.

## Deliverables

Use the shared report. Include route, role, viewport and orientation, trigger, expected and observed rendering, severity and capture path or limitation. Identify simulated states.

See [a worked visual comparison](references/worked-scenario.md).
