---
name: design-system-architect
description: "Use when implementing or auditing reusable design tokens, typography, spacing and component variants; not when just selecting an artistic direction."
---

# design-system-architect

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Inventory existing components and design conventions across the target surfaces. Start from the smallest reusable decisions that fit the current platform and implementation.

## Goal
Create coherent design decisions from the actual product and code rather than mixing incompatible template styles.

## Procedure
1. Inspect current CSS variables, theme providers, CSS or framework configuration, component tree, screenshots, brand assets and existing DESIGN.md.
2. Inventory inconsistencies: type scale, spacing, radii, elevations, colors, focus, semantic state colors, density and breakpoints.
3. Propose a small semantic token layer with contrast-safe light/dark values and component variants; preserve existing public contracts where possible.
4. In implementation mode, build a representative vertical slice: typography, buttons, cards, inputs, navigation and states, without mass rewriting unrelated screens.
5. In audit mode, report observed inconsistencies and proposed token or variant changes. In implementation mode, document naming, migration guidance and tests. Check keyboard, zoom, high contrast and forced-colors as relevant.
6. Validate across desktop/mobile and report visual regressions and backward compatibility.

## Deliverables
Use the shared report. Design inventory, token schema, component conventions, DESIGN.md additions, migration plan, screenshots and open decisions.

## Specific constraints
A new design system requires an explicit product goal; never erase established brand identifiers by default.

## Activation boundary and worked pattern
- **Use for:** Task: standardize spacing and button variants across existing interface screens.
- **Do not use for:** Not this task: invent a new visual brand without implementation.
- Load [worked scenario](references/worked-scenario.md) only when the task needs a concrete example or output structure.
