# Worked scenario — engineering-tdd-implementer

## Appropriate request
Task: fix an API validation bug using behavior-first tests.

## Near-miss request
Not this task: review a finished PR for code smells.

## Domain-specific procedure
Write an independent failing example at a stable boundary. Check it fails for the expected reason, add the least code to pass, then add one edge case. Do not infer a green test from static inspection. Only refactor after the existing behavior tests pass.

## Required output
Test name, failing and passing command output if run, changed files and untested cases.

Demonstrative scenario only. Do not claim this scenario has been executed by a model.
