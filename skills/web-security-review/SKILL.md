---
name: web-security-review
description: "Use for frontend security reviews of auth, browser integrations, untrusted data, dependencies or client-side secrets; not for generic styling changes."
---

# web-security-review

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify browser capabilities, origins, externally supplied data and privilege boundaries. Adapt defensive verification to the architecture and authorized scope.

## Goal
Review concrete web threat surfaces and reduce exploitable changes before they ship.

## Procedure
1. Inspect data flows, auth boundaries, roles, environment handling, CSP, dependency changes and the touched endpoints.
2. Identify relevant risks: XSS, CSRF, open redirect, IDOR, cookie/session handling, leaked tokens, supply-chain, unsafe HTML and third-party embeds.
3. Trace authorization enforcement to the backend; never accept UI hiding as a control. Validate redirects and external URLs.
4. Review untrusted inputs, dependency scripts, external assets, secrets in logs and analytics; avoid broad risky security refactors.
5. Propose minimal remediations and reproducible tests. Escalate live-environment verification rather than performing it unapproved.

## Deliverables
Use the shared report. Threat assumptions, affected files, findings with severity and evidence, remediation, tests and residual risk.

## Specific constraints
Do not access secrets, change production auth/security controls or run active scans without authorization.

## Activation boundary and worked pattern
- **Use for:** Task: review a new OAuth callback and redirect handling.
- **Do not use for:** Not this task: improve landing page typography.
- Load [worked scenario](references/worked-scenario.md) only when a concrete example is useful.
