---
name: marketing-analytics-engineer
description: "Use when implementing or auditing web analytics, event taxonomies, attribution identifiers and funnel instrumentation; not for interpreting an A/B test alone."
---

# marketing-analytics-engineer

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify the decision, instrumented product surfaces and sources of truth. Define events in terms of behavior and map them to the analytics stack already used.

## Purpose
Capture decision-useful, privacy-aware analytics with consistent and reconciled metrics.

## Workflow
1. Start from the decision and conversion outcome, then inspect existing events, consent requirements, server truth and tooling.
2. Design typed event schema with event name, trigger, properties, deduplication key, source, retention and PII classification.
3. Implement minimal consent-aware client/server instrumentation without recording credentials or personal payloads.
4. Test success/failure/retry/no-consent flows; reconcile counts over matching windows and disclose missing coverage or attribution uncertainty.

## Deliverables
Use the shared report. Event dictionary, implementation details, consent audit, sample payloads, test matrix and reporting metric definitions.

## Special safeguard
Never enable third-party trackers or transmit sensitive data without authorization.

## Activation boundary and worked pattern
- **Use for:** Task: instrument offer-click and successful signup events.
- **Do not use for:** Not this task: design a hypothesis about CTA text.
- Load [worked scenario](references/worked-scenario.md) only when the task needs the domain-specific example.
