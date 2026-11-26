---
name: product-art-direction
description: "Use when defining, adapting or auditing product art direction, including approved brands, operational interfaces and thermal print. Hand token implementation to design-system-architect."
---

# product-art-direction

Apply the [shared execution and delivery guide](references/quality-gates.md). Read approved assets, existing tokens, audience, production channels and the actual workflow. Use audit mode for reviewing an approved design.

## Workflow

1. For an approved brand, use its master, tokens, type, color and identity rules. Show the smallest channel adaptations and raise exceptions for approval. When the brief calls for a new direction, compare two or three original options with real product content and explain the selection.
2. For operational products, prototype a representative daily task. Cover dense tables or queues, primary actions, feedback, denied or error states and realistic long content. Assess scanning, legibility and hierarchy at project widths. For marketing surfaces, prototype a hero and dense content where relevant.
3. For thermal print, use supported paper widths and the printer/driver's printable area, resolution and character encoding. Design for monochrome at physical size. Check contrast, wrapping, alignment, margins, accents, long item names, totals and barcode/QR scanability where used. Validate with the approved rendering path and a physical proof on the target device. Without hardware, preserve a physical-scale preview and mark actual print or scan verification BLOCKED. [Printer dimensions and printable area](https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/glossary.html)
4. Check asset rights, contrast and fidelity to the approved direction. Hand token and reusable component implementation to `design-system-architect`, operational flows to `premium-dashboard-builder` and printer trust-boundary checks to `secure-coding-baseline`.

## Deliverables

Use the shared report. Include direction, adaptations and rationale, representative prototype or audit evidence, token/component handoff and print proof where applicable.

For a worked example, see [direction and handoff](references/worked-scenario.md).
