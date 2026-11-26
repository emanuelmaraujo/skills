# Routing matrix (initial: 2026-11-26)

Start from this table, then correct it with `$HOME/cezar-platform/var/scoreboard.md` (real success
rate, rework and review outcome per runner/model in this workspace). When the two disagree for a
task type with at least 5 settled tasks, the scoreboard wins; note it in the plan.

## Models verified as runnable headless in cezar (2026-11-26)
- `claude` (Claude Max login): `opus` (Opus 5.5), `sonnet` (Sonnet 5.5), `haiku`. Effort low to max.
- `codex` (ChatGPT login, Codex CLI 0.172): `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-6-astra`, `gpt-6-sol`,
  `gpt-6-luna`, `gpt-5.6-*`; effort low…max (sol/terra/astra also `ultra`).
- `antigravity` (Google AI Pro via `agy` 1.5.18): `gemini-4-carbon-{low,medium,high}`,
  `gemini-4-neon-{low,medium,high,xhigh}`, `gemini-4-hydrogen-{low,…,xhigh}`, `gemini-4-argon-*`,
  `gemini-3.8-flash-*`. The effort is the slug suffix. Gemini CLI is not usable: it no longer accepts a
  personal Google sign-in.

## Defaults by work type
| Work | First choice | Second choice | Notes |
|---|---|---|---|
| Supervision, planning, hard architecture | claude `opus` | codex `gpt-6.1-sol` high | Routine coordination: claude `sonnet` |
| Frontend, UI/UX, design system, a11y, mobile | claude `opus` (complex) / `sonnet` | codex `gpt-6.1-sol` | **Never antigravity** (guard-enforced) |
| Backend, APIs, DB, Supabase, business rules | codex `gpt-6.1-sol` high | antigravity `gemini-4-neon-high` (independent module) | |
| Payments, idempotency, reconciliation, auth, security fixes | codex `gpt-6.1-sol` xhigh | claude `opus` | Cross-provider review mandatory |
| DevOps, CI/CD, infra, refactors, hard debugging, branch integration | codex `gpt-6.1-sol` high | claude `opus` | |
| Large-repo investigation, dependency analysis | antigravity `gemini-4-carbon-high` | codex | Long context |
| Tests, edge cases, RLS and multi-tenant audit, performance | antigravity `gemini-4-carbon-high` | codex | Audit is read-only |
| Docs, research, simple scans | antigravity `gemini-4-hydrogen-medium` or `gemini-3.8-flash-medium` | claude `haiku` | Cheapest capable |
| Independent review | a provider different from the implementer | | Claude→Codex, Codex→Claude/Gemini Carbon, Gemini→Codex |

## Escalation
Second failure on the same subtask: raise the model or effort within the provider (sonnet→opus,
codex high→xhigh, neon→carbon). Third: switch provider. Then record a blocker; do not loop.

## Public evidence behind the defaults (to be confirmed)
Aggregators agree on the ordering but not on the numbers (November 2026): Opus 5.5 leads Terminal-Bench
4.0 (~65–66%), Gemini 4 Carbon is close behind (~65%), GPT-6.1 Sol trails on Terminal-Bench 4.1 (~61%,
Codex at max effort). SWE-bench Verified is saturated and its figures conflict. Neon is cheaper and
faster than Carbon at similar index scores; Hydrogen is the fastest and cheapest. These are model and
harness results, not this workspace's: the scoreboard is the tie-breaker.
