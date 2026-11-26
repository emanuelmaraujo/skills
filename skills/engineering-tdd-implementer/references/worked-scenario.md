# Worked scenario — test-first evidence

A team adds a new status action to Orders and independently corrects how a subtotal is shown.

- Expose the smallest callable route while the status rule is absent. Record any missing-route failure as setup. With the project's authenticated browser fixture, check an allowed operator, a restricted operator and the persisted status. Before implementing the rule, capture the assertion failure for the expected state change.
- Freeze an independently reviewed expected visual reference for the subtotal on an affected viewport. With updates disabled, compare against the unchanged route. If only a generated baseline is available, start with an explicit expected subtotal and use the comparison as supplementary evidence.
- Run both regressions with independent fixtures if neither depends on the other. Record both results even if the runner defaults to fail-fast. Re-run the same cases after implementation.

Use the shared report and list which assertions ran, red and green results, baseline provenance and any role or browser checks that were blocked. This example describes a proposed procedure.
