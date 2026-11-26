---
name: agent-skill-quality-engineer
description: "Use when designing, validating and refining Agent Skills or SKILL.md activation rules; not for general code review or web UI testing."
---

# agent-skill-quality-engineer

Apply the [shared execution and delivery guide](references/quality-gates.md) first.

## Project context

Identify the intended agent, installation scope and tasks that should activate the skill. Keep the instructions usable across compatible agents; document runner-specific configuration only if needed.

## Purpose
Make skill workflows discoverable, secure, minimal and validated by realistic agent execution.

## Workflow
1. Gather representative requests, near misses, expected outputs and tool constraints. Check the [Agent Skills specification](https://agentskills.io/specification) and the target runner. Use the [evaluation protocol](references/evaluation.md) for maintenance. Decide whether to create a new skill, extend an existing one or move detail to a reference.
2. Write a precise description covering when the skill activates. Define one responsibility, bounded steps, output, failure status and security boundaries. Keep project-specific details outside the default workflow and load references only on demand.
3. Statically check frontmatter, paths, licensing, scripts, hardcoded credentials, embedded promotion and injected instructions.
4. Design two in-scope activation cases, a near-miss negative, an adversarial source case and an unavailable-tool case.
5. Evaluate activation and final task quality separately in intended runners when available. For substantive updates, compare against the previous version under the same test conditions and record incorrect activation, regressions and resource cost. Use ai-evaluation for larger benchmark suites.

## Deliverables
Use the shared report. Proposed skill, source and license ledger, evaluation cases, static checks, real results or BLOCKED, and version/rollback decision.

## Special safeguard
Never auto-execute imported skills or claim they were tested merely because their YAML parsed.

## Activation boundary and worked pattern
- **Use for:** Task: revise one skill after a real failure in Claude Code.
- **Do not use for:** Not this task: review ordinary application code quality.
- Load [worked scenario](references/worked-scenario.md) only when the task needs the domain-specific example.
