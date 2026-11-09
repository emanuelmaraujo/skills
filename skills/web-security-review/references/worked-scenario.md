# Worked scenario — web-security-review

## Appropriate request
Task: review a new OAuth callback and redirect handling.

## Near-miss request
Not this task: improve landing page typography.

## Domain-specific approach
Trace trust boundaries from user-controlled URL to authorization and backend checks. Check redirect allowlist, token storage, CSRF/state validation, XSS sinks and server-side authorization. Reproduce a harmless failing case in a test environment; never exploit a real user or bypass project permission.

## Acceptance evidence
Threat table with entry point, trust boundary, evidence, severity, fix and tests.

This is an example, not a completed runtime test. Do not claim real test results without evidence.
