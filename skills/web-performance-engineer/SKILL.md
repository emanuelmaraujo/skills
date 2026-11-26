---
name: web-performance-engineer
description: "Use when optimizing web load and interaction performance including audits that measure LCP, INP, CLS, JS hydration and bundle size; not for purely SEO indexing."
---

# web-performance-engineer

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify real device/network conditions, priority journeys and the available measurement tools. Choose metrics that reflect the observed problem.

## Goal
Improve measured user experience while preserving content, SEO, accessibility and feature correctness.

## Procedure
1. Capture a reproducible baseline (URL, commit, device profile, network, cache, test run count); separate lab and field metrics. Use existing traces, browser developer tools or approved project instrumentation. Mark metrics that the available method cannot collect as BLOCKED.
2. Inspect LCP, INP, CLS and supporting diagnostics, waterfalls, render-blocking assets, JS cost, images, fonts and third-party scripts.
3. Prioritize by measured bottleneck and expected cost. In audit mode, report the baseline, evidence and prioritized opportunities. In implementation mode, optimize the affected path, then perform steps 4–5.
4. Avoid regressions in analytics, navigation, auth, SEO or visual fidelity. For WebGL/video, provide poster and adaptive loading.
5. Compare before/after under identical conditions and run functional tests. Report variance and unverified improvements.

## Deliverables
Use the shared report. Baseline, bottleneck analysis, diff, before/after metrics, trace location, acceptance against project budget and trade-offs.

## Specific constraints
Do not claim performance gains without comparable runs or optimize to synthetic scores at the expense of real UX.

## Activation boundary and worked pattern
- **Use for:** Task: reduce slow LCP on a product detail page.
- **Do not use for:** Not this task: fix robots.txt and canonical headers.
- Load [worked scenario](references/worked-scenario.md) only when a concrete example is useful.
