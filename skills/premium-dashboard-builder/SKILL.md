---
name: premium-dashboard-builder
description: "Use when implementing data-heavy administrative dashboards, tables, workflows and operational interfaces; not for marketing landing pages."
---

# premium-dashboard-builder

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify operator roles, frequency of use and critical decisions. Select the interface patterns that fit the available data and required actions.

## Goal
Optimize information hierarchy, operational speed, trust and safe actions; aesthetics support task completion.

## Procedure
1. Map top user jobs, roles, critical data and decision frequency; inspect current routes, APIs, auth and design components.
2. Define information architecture, navigation labels, page hierarchy, filters, search and state persistence in URL where appropriate.
3. Design representative real-data layouts including skeleton, empty, partial, error, permission-denied, stale and slow-network states.
4. Ensure tabular density, keyboard focus, touch targets, responsive overflow and readable chart alternatives.
5. For destructive/bulk actions, add confirmations, permissions and idempotent request handling appropriate to existing APIs.
6. Validate with realistic high-volume and long-text fixtures. Open critical routes such as Orders as a restricted test user. Check the visible permission-denied state, safe navigation and absence of protected data, then exercise an allowed role. Instrument critical actions without sensitive data.

## Deliverables
Use the shared report. Page map, components, interaction specification, state matrix, authorization assumptions, visual QA and functional test evidence.

## Specific constraints
Verify backend behavior through its normal entry points. Enforce authorization on the server and avoid sending privileged data to restricted sessions.

## Activation boundary and worked pattern
- **Use for:** Task: implement a promotions moderation queue and filters.
- **Do not use for:** Not this task: add a marketing hero section.
- Load [worked scenario](references/worked-scenario.md) only when the task needs a concrete example or output structure.
