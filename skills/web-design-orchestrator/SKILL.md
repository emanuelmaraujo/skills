---
name: web-design-orchestrator
description: "Use for a multi-step web build requiring coordinated research, design, implementation and independent QA; not for narrow one-component fixes."
---

# web-design-orchestrator

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify the project goal, scope and available evidence. Route only the disciplines needed for this project and reuse existing project conventions.

## Goal
Coordinate specialized web skills without delegating away project constraints or claiming unavailable capabilities.

## Procedure
1. Inspect project rules and repo; define scope, business goal, brand, pages, stakeholders, success metrics and permissions.
2. Build a minimal plan; select only relevant specialist skills and order dependencies: reference research → design system → builder → motion/3D (optional) → a11y/performance/security/visual QA.
3. Assign one owner per decision. Product art direction owns interpretation of the visual brief and approved brand, design system owns tokens and reusable components, and the builder owns implementation. Accessibility owns WCAG evidence, performance owns runtime metrics, security owns trust-boundary findings and visual QA owns rendered comparisons. In audit mode, route only relevant evidence checks.
4. For each stage require an evidence handoff (files, tests, sources, limitations), not merely agent self-report. Distinguish independent review from self-review.
5. Stop on security/license blockers or missing approval, and surface alternatives. Reconcile conflicting outputs against real code and product requirements.
6. Consolidate each specialist's evidence into the shared report. Record decisions and release status when relevant.

## Deliverables
Use the shared report. Execution plan, skill routing, consolidated decisions, changes, evidence, unresolved issues, review checkpoints and final status.

## Specific constraints
Do not grant another agent authority to merge, deploy or run migrations; respect least privilege and user approvals.

## Activation boundary and worked pattern
- **Use for:** Task: create a full responsive SaaS website with QA.
- **Do not use for:** Not this task: fix one CSS margin.
- Load [worked scenario](references/worked-scenario.md) only when a concrete example is useful.
