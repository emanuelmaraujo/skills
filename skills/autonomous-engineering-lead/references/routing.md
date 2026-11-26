# Routing matrix (initial: 2026-11-26)

Start from this table, then correct it with `$HOME/cezar-platform/var/scoreboard.md` (real success
rate, rework and review outcome per runner/model in this workspace). When the two disagree for a
task type with at least 5 settled tasks, the scoreboard wins; note it in the plan.

## Models verified as runnable headless in cezar (live probe, 2026-11-26)
Each was called headless as the `cezar` user and answered. Listed ≠ usable: re-probe after CLI updates.
- `claude` (Claude Max): `opus` (Opus 5.5), `fable` (Fable 5.2), `sonnet` (Sonnet 5.5), `haiku` (Haiku 5.5).
  Effort low…max. Fable spends the Max allowance fastest: only for the hardest problems.
- `codex` (ChatGPT Plus): `gpt-6.2-sol` (CLI default), `gpt-6.2-astra`, `gpt-6.1-terra`, `gpt-6-luna`
  (older `gpt-6.1-sol`, `gpt-6-*`, `gpt-5.6-*` still listed). Effort low…max.
- `antigravity` (Google AI Pro via `agy` 1.5.18): `gemini-4-carbon-*`, `gemini-4-neon-*`, `gemini-4-argon-*`,
  `gemini-4-hydrogen-*`, `gemini-3.8-flash-*`, `gemini-pro-orchestrator*`; the effort is the slug suffix.
  Gemini CLI is not usable: it no longer accepts a personal Google sign-in.

## Defaults by work type
| Work | First choice | Second choice | Notes |
|---|---|---|---|
| Supervision, planning, hard architecture | claude `opus` high | codex `gpt-6.2-astra` high | Routine coordination: claude `sonnet`; a problem two attempts failed: claude `fable` |
| Frontend, UI/UX, design system, a11y, mobile | claude `opus` (complex) / `sonnet` | codex `gpt-6.2-sol` | **Never antigravity** (guard-enforced) |
| Backend, APIs, DB, Supabase, business rules | codex `gpt-6.2-sol` high | antigravity `gemini-4-neon-high` (independent module) | |
| Payments, idempotency, reconciliation, auth, security fixes | codex `gpt-6.2-astra` high | claude `opus` | Cross-provider review mandatory |
| DevOps, CI/CD, infra, refactors, hard debugging, branch integration | codex `gpt-6.2-sol` high | claude `opus` | |
| Large-repo investigation, dependency analysis | antigravity `gemini-4-carbon-high` | codex `gpt-6.2-sol` | Long context |
| Tests, edge cases, RLS and multi-tenant audit, performance | antigravity `gemini-4-carbon-high` | codex | Audit is read-only |
| Docs, research, simple scans, early read-only investigations | antigravity `gemini-4-hydrogen-medium` / `gemini-3.8-flash-medium` | claude `haiku`, codex `gpt-6-luna` | Cheapest capable |
| Independent review | a provider different from the implementer | | Claude→Codex, Codex→Claude/Gemini Carbon, Gemini→Codex |

## Allowance
Check `liveUsage.limits` of your own task (five_hour, seven_day). Above 80% on a provider, route the next
non-frontend subtasks to another provider or a cheaper model of the same one, and say so in the plan.

## Escalation
Second failure on the same subtask: raise the model or effort within the provider (sonnet→opus,
codex sol→astra, neon→carbon, opus→fable). Third: switch provider. Then record a blocker; do not loop.

## Public evidence behind the defaults (to be confirmed)
Aggregators agree on the ordering but not on the numbers (November 2026). Terminal-Bench 4.1 (agent plus
model): Fable 5.2 and Opus 5.5 ~65.8%, GPT-6.2 Astra ~62.1%, GPT-6.2 Sol ~61.5%; Gemini 4 Carbon ~65% on
4.0. GPT-6.2 Sol lands within 0.4 points of Astra on FrontierCode 2.0 at about a fifth of the cost, hence the
default; Fable 5.2 leads FrontierCode 2.0 (50.2%) but its edge over Opus 5.5 on Terminal-Bench is small. SWE-bench Verified is saturated and its figures conflict. Neon is cheaper and
faster than Carbon at similar index scores; Hydrogen is the fastest and cheapest. These are model and
harness results, not this workspace's: the scoreboard is the tie-breaker.
