---
name: seo-structured-data-engineer
description: "Use when writing or validating Schema.org JSON-LD, Product or Offer metadata, breadcrumbs and rich-result markup; not for generic keyword research."
---

# seo-structured-data-engineer

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify the content entities and eligible markup for the target surface. Map published facts to the schema and validate against visible content.

## Purpose
Produce machine-readable claims that exactly reflect visible, trusted site content.

## Workflow
1. Inventory page type, canonical URL, actual visible data and source-of-truth fields.
2. Check current Schema.org and target search-engine primary documentation for schema eligibility and required fields.
3. Generate safe typed JSON-LD with escaped values, omitting unavailable facts instead of inventing prices, ratings, inventory or promotions.
4. Validate syntax and rich-result criteria using available tools, then test price/availability updates, SSR HTML output and canonical consistency.

## Deliverables
Use the shared report. JSON-LD and source mapping, validation evidence, relevant URLs, missing fields, expected update strategy and limitations.

## Special safeguard
A valid schema does not guarantee rich results. Never fabricate Product availability, ratings or offers.

## Activation boundary and worked pattern
- **Use for:** Task: add valid Product and Offer structured data to a real product page.
- **Do not use for:** Not this task: brainstorm blog topics.
- Load [worked scenario](references/worked-scenario.md) only when a concrete example is useful.
