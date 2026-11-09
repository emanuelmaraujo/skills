# Worked scenario — marketing-analytics-engineer

## Appropriate request
Task: instrument offer-click and successful signup events.

## Near-miss request
Not this task: design a hypothesis about CTA text.

## Domain-specific procedure
Define event schema: name, trigger, user consent, anonymous/session ID, property allowlist, backend confirmation, dedupe key and retention. Test event emission under retries, navigation, failure and no consent. Reconcile against authoritative server events over the same observation window.

## Required output
Typed event dictionary, privacy classification, event tests and reconciliation results or BLOCKED.

Demonstrative scenario only. Do not claim this scenario has been executed by a model.
