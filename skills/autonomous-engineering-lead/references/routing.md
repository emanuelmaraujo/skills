# Routing policy (2026-11-26)

Decide every subtask on five inputs, in this order, and write the choice and its reason in the plan:
**hard rules → risk → complexity → availability → measured performance.** Tools needed are a filter
inside each step. All three providers are first-class executors; none is "only a reviewer".

## 1. Hard rules (never overridden)
- Frontend (components, pages, styles, templates, design tokens, UI copy in components): **claude or
  codex only**. The scope guard fails any run where antigravity changed such a file, fallback included.
  Gemini may audit, test and propose frontend changes in docs.
- The reviewer is a provider different from the implementer, on the rotation claude→codex, codex→antigravity, antigravity→claude.
- All three providers work at once: each owns a front in flight together.
- A subtask that needs a tool a runner lacks in this workspace goes to a runner that has it
  (browser automation: claude or codex; everything else: all three).

## 2. Risk
| Risk | Areas | Minimum |
|---|---|---|
| High | payments, auth, tenant isolation, migrations, real data, security fixes, infra | implementer at the "strong" tier, effort high; cross-provider review mandatory; human gate for anything irreversible |
| Medium | business rules, APIs, integrations, concurrency | "standard" tier, effort medium-high; workflow review |
| Low | docs, copy, tests for existing behavior, mechanical refactors, investigations | "fast" tier |

## 3. Complexity → tier → model
| Tier | When | claude | codex | antigravity |
|---|---|---|---|---|
| Exceptional | two strong attempts failed, or a novel hard design/debugging problem | `fable` high | `gpt-6.2-astra` xhigh | `gemini-4-carbon-high` |
| Strong | cross-module design, hard debugging, high risk | `opus` high | `gpt-6.2-astra` high | `gemini-4-carbon-high` |
| Standard | a well-specified feature or fix in one area | `sonnet` / `opus` medium | `gpt-6.2-sol` medium-high | `gemini-4-neon-high` |
| Fast | investigations, docs, scans, simple tests | `haiku` | `gpt-6-luna` | `gemini-4-hydrogen-medium`, `gemini-3.8-flash-medium` |

Roles: the **manager** is claude `sonnet`. The **technical lead** of a complex task is claude `opus`;
a backend-only front may be led by codex `gpt-6.2-sol` or antigravity `gemini-4-carbon-high` (that lead
dispatches its own children). **Executors:** codex `gpt-6.2-sol` is the generalist; antigravity
`gemini-4-carbon-high` / `gemini-4-neon-high` are main engineering executors for backend, data, tests,
performance and large-repo work; claude owns frontend and hard architecture.
**Escalation:** second failure → next tier, same provider (sonnet→opus→fable, sol→astra, neon→carbon);
third → another provider; then a named blocker. Never loop.

## 4. Availability (the signals that exist — never API list prices)
- Your task's `liveUsage.limits` (`five_hour`, `seven_day` utilization and `resetsAt`) for claude, and
  the usage-limit stops recorded on runs for every provider (`cezar usage` on the cockpit host).
- Above 80% in a provider's short window: send the next non-frontend subtasks to another provider or a
  lower tier; frontend waits for claude/codex rather than going to antigravity.
- A provider that stopped on a usage limit is unavailable until its reset; cezar resumes the stopped run
  at the reset (`autoResumeOnUsageLimit`).
- Spread parallel children across providers so one allowance is not the bottleneck.

## 5. Measured performance (decides ties, then overrides the table)
`$HOME/cezar-platform/var/scoreboard.md` gives per runner·model: tasks, success, failures, median time,
rework iterations and review verdicts received. With ≥5 settled tasks of a work type, the scoreboard
wins over this table; record it in the plan.

## Models verified in cezar (2026-11-26)
Headless probe answered for each, as the `cezar` user. A probe is not operational proof: the
homologation runs record which models completed real tasks (see the platform's HOMOLOGACAO.md).
- claude (Claude Max): `opus` (Opus 5.5), `fable` (Fable 5.2), `sonnet` (Sonnet 5.5), `haiku` (Haiku 5.5).
- codex (ChatGPT Plus): `gpt-6.2-sol` (CLI default), `gpt-6.2-astra`, `gpt-6.1-terra`, `gpt-6-luna`.
- antigravity (Google AI Pro via `agy`): `gemini-4-carbon-high`, `gemini-4-neon-medium`,
  `gemini-4-argon-medium`, `gemini-4-hydrogen-low`, `gemini-3.8-flash-low`, `gemini-pro-orchestrator`
  (other effort suffixes listed). Gemini CLI is unusable: it no longer accepts a personal sign-in.

## Public evidence (background only)
Terminal-Bench 4.1 (agent plus model, Nov 2026): Fable 5.2 and Opus 5.5 ~65.8%, GPT-6.2 Astra ~62.1%,
GPT-6.2 Sol ~61.5%; Gemini 4 Carbon ~65% on 4.0. GPT-6.2 Sol is within 0.4 points of Astra on
FrontierCode 2.0. Fable 5.2 leads FrontierCode 2.0 but its Terminal-Bench edge over Opus is small. These
are harness results, not this workspace's.
