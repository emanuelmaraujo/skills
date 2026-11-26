# Worked scenario — visual audit without a new dependency

Compare checkout before and after a CSS change using the project viewport matrix, relevant breakpoint edges and the same seeded cart, browser, role and revision metadata. Include long item names, a modal and both loading and error.

Hold the checkout request through the existing fixture or browser tooling, capture the loading state, release and confirm recovery. Fail the request with the supported fixture and capture feedback and retry. If automation is prohibited, use a permitted browser and existing fixtures. A simulated offline state verifies the offline path only. Mark the targeted failure state BLOCKED if you cannot exercise it.

Keep application files and baselines intact while auditing. Use the shared report with route, expected and actual state, viewport, reproduction steps and evidence. This example describes a proposed procedure.
