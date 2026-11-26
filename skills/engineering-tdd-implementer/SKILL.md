---
name: engineering-tdd-implementer
description: "Use for test-first implementation and bug fixes through observable public entry points, including snapshots, authenticated UI and independent batches."
---

# engineering-tdd-implementer

Before choosing tests, apply the [shared execution and delivery guide](references/quality-gates.md). Identify acceptance criteria, existing entry points, runner, fixtures and supported environments. For a review-only request, inspect existing red/green evidence using audit mode.

## Workflow

1. For an existing behavior change, run the new regression on the unchanged implementation. For a new public function or route, record missing import, missing route or compilation failure as interface setup. Add only enough wiring or a placeholder for the runner to reach the scenario, then obtain a separate failure on the business assertion before adding the rule. Setup failures, inaccessible fixtures and zero discovered tests do not demonstrate a business red.
2. Assert a user-visible outcome, persisted effect or public response with an independent expected value. For a snapshot or visual baseline, first review an expected reference from the spec or approved design, freeze it, and compare with updates disabled. Record the actual mismatch before the fix. A first run that creates or rewrites the reference is baseline setup. If there is no independent approved reference, obtain a behavioral red with an explicit assertion and use snapshots as supplementary evidence.
3. For a single behavior, change one cause at a time. For independent items, batch the red runs with named cases and independent data. Record the expected failure and result for every item before implementing them. Disable fail-fast or run cases individually to confirm the runner reached every case. Split dependent cases or shared setup failures before interpreting results.
4. For UI depending on session, role or tenant, use the product's real authentication and session path in a test environment with supported test accounts or the existing authenticated browser fixture. Exercise the real route and its guards with an allowed session and the relevant denied or expired session. Component mocks are supplementary. If the session or browser is unavailable, record the integration check as BLOCKED and retain narrower evidence.
5. Implement the smallest change for green and rerun the same assertions and fixtures with snapshot updates disabled. Refactor after green. Run applicable repository regression, lint and type checks. Keep pre-existing failures separate and preserve assertion strength.

## Deliverables

Use the shared report. Include the public entry point, red and green command/results per behavior, baseline provenance when relevant, any interface setup failure and the scope of regression checks. Identify tests written after implementation as verification.

For a worked example, see [test-first evidence](references/worked-scenario.md).
