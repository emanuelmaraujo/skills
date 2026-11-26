---
name: web-accessibility-audit
description: "Use when auditing WCAG, keyboard access, screen-reader semantics and focus behavior; not as generic visual polish."
---

# web-accessibility-audit

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify target users, input methods, critical journeys and applicable conformance needs. Use available tools and complement automation with manual checks.

## Goal
Audit user journeys against applicable WCAG guidance. Implement and verify fixes when requested.

## Procedure
1. Identify core journeys and relevant WCAG conformance target; review semantics and accessible names before automated tests.
2. Check keyboard-only navigation, focus visibility/order/return, dialogs, forms, validation messages, skip links and headings.
3. Inspect contrast, touch targets, zoom/reflow, pointer-only interactions, status announcements and motion preferences.
4. Run the project's existing accessibility checks for each in-scope route and relevant state. If automation is prohibited or absent, use manual keyboard, semantics, contrast and reflow checks. Use a screen reader when available and mark unavailable checks. Record automated violation counts by route and ruleset when collected.
5. In audit mode, record findings and proposed corrections. When fixes are requested, address high-impact issues incrementally and retest using the same routes, states and ruleset. Record device, assistive technology and limitations.
6. Avoid treating automation scores as certification; communicate residual issues.

## Deliverables
Use the shared report. Accessibility findings by journey and severity, WCAG references, fix diffs, keyboard/AT evidence and residual risk.

## Specific constraints
Never claim WCAG compliance solely from static analyzers or perfect Lighthouse accessibility scores.

## Activation boundary and worked pattern
- **Use for:** Task: diagnose keyboard trap in a checkout modal.
- **Do not use for:** Not this task: change card shadows and brand colors.
- Load [worked scenario](references/worked-scenario.md) only when a concrete example is useful.
