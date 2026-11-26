---
name: web-3d-experience-builder
description: "Use when implementing interactive 3D product viewers or website scenes in a browser; not for offline 3D rendering only."
---

# web-3d-experience-builder

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify device needs, assets, interaction goals and performance limits. Choose the rendering approach based on the stack and fallback requirements.

## Goal
Deliver optional and performant 3D that demonstrates real products without obstructing content or conversion.

## Procedure
1. Confirm that 3D solves a user need; inspect assets and permissions, target platforms, SSR constraints and existing stack.
2. Choose between the existing renderer, an approved self-contained viewer or a static rendering using maintenance and performance trade-offs. If WebGL or new dependencies are prohibited, use existing assets with native HTML controls and identify any interaction that remains blocked.
3. Separate 3D canvas from accessible HTML navigation, controls, labels and product copy; implement loading poster and graceful fallback.
4. Compress models/textures, lazy-load offscreen scenes, limit draw calls/pixel ratio and account for context loss.
5. Provide a non-WebGL or reduced-motion fallback; controls must support touch and keyboard alternatives when essential.
6. Benchmark on representative mobile hardware and slow networks, and test error/asset loss and route cleanup.

## Deliverables
Use the shared report. Viewer or scene, fallback, asset provenance, GPU budget and measured results, screenshots/video if actually captured.

## Specific constraints
Never make critical product information accessible only in canvas or use unlicensed models.

## Activation boundary and worked pattern
- **Use for:** Task: build an optional 3D rotatable product viewer.
- **Do not use for:** Not this task: render a static product image.
- Load [worked scenario](references/worked-scenario.md) only when the task needs a concrete example or output structure.
