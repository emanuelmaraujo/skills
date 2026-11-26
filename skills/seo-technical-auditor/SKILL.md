---
name: seo-technical-auditor
description: "Use for technical SEO discovery, indexing, crawl signals, canonical tags and sitemaps; not for tuning Web Vitals without indexing impact."
---

# seo-technical-auditor

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify target search surfaces, rendering behavior, URL inventory and indexing intent. Restrict conclusions to the evidence available for this site.

## Purpose
Diagnose verifiable blockers to search discoverability, without guaranteeing search rankings.

## Workflow
1. Inspect the real site, its critical routes, response headers, rendered HTML, robots.txt, sitemaps and canonical/noindex rules; establish public and authenticated boundaries.
2. Build a sample URL matrix for 200/3xx/4xx, mobile, JavaScript rendering, duplicate pages and hreflang. Prefer first-party search diagnostics if access is authorized.
3. Distinguish observed defects from hypotheses and third-party claims. Rank fixes by expected business impact and reproduction evidence.
4. In audit mode, give the prioritized correction and verification plan. If implementation is requested, apply the smallest authorized correction and recrawl or retest. Search engines control indexing.

## Deliverables
Use the shared report. URL audit table, reproduction, indexability/technical findings, priority, tests, uncertainty and verification plan.

## Special safeguard
Never treat robots.txt as security, or claim immediate SEO gains or guaranteed indexing.

## Activation boundary and worked pattern
- **Use for:** Task: diagnose a category URL excluded from search indexing.
- **Do not use for:** Not this task: fix a frontend interaction delay.
- Load [worked scenario](references/worked-scenario.md) only when a concrete example is useful.
