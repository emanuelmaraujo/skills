# Delivery quality gates

Quality is a set of **non-compensating gates**. A beautiful page does not excuse a security flaw, inaccessible form or broken payment flow.

## Preflight

1. Identify source repository, base commit/branch, repo instructions, stack, design tokens and environment.
2. Record goal, user tasks, audience, pages, brand, accessibility target, performance baseline and decision owner.
3. Scope risk, third-party permissions/licenses and operations requiring explicit user approval.

## Validation checklist

| Gate | Evidence to collect | Failure signal |
| --- | --- | --- |
| Functional | Existing tests, realistic data flows, route and form interactions | Broken central journey |
| Responsive | At least 390×844, 768×1024, 1440×900 plus variable text | Overflow, cut content, invisible CTA |
| Accessibility | Keyboard, focus, labels, contrast, reduced motion; manual AT when possible | Blocked critical journey |
| Security | Dependency, XSS, auth boundary, external script, secret checks | Exploitable change |
| Performance | Reproducible before/after for LCP/INP/CLS where relevant | Unexplained material regression |
| Design | Consistent hierarchy, spacing, typography, state feedback | Brand or usability regression |
| License/privacy | Assets/copy licenses, consent and vendor contracts | Unknown rights for shipped assets |

## Result vocabulary

- **PASS** — executed and meets acceptance; link to evidence.
- **FAIL** — executed and did not meet acceptance; reproduce.
- **SKIP** — intentionally omitted and why.
- **BLOCKED** — impossible due to missing access/tool/device; describe alternative.

Do not confuse reading code with running tests or a self-evaluation with independent review. No deploy/merge/migration by default.

## Final report

Scope; changed files; design decisions with references; dependencies and licenses; exact commands/tests/results; screenshots or blocking reason; performance before/after if measured; security/privacy findings; follow-up; authorization requests.
