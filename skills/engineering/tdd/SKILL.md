---
name: tdd
description: Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.
---

## Before writing any code

Ask: "What behaviour do you want to implement or fix?" One clear behaviour. Don't write a test until you have it.

If a project TDD file exists (`tests/TDD.md` or `.claude/tdd.md`), read it first — it takes precedence.

Check what language and test runner the project uses. Adapt all commands accordingly — examples in this skill use Python/pytest, but the discipline applies to any stack.

## Mid-flow recovery

If this skill is invoked after implementation has already started — stop immediately. No more implementation until a failing test exists.

Assess the state:

**Small or uncommitted changes (a few minutes of work):** Prefer reverting. Undo the implementation, write the test first, confirm it fails, then re-implement. A clean cycle is worth more than saving a few lines. Ask the human whether to revert or proceed with characterisation.

**Substantial existing implementation:** Write characterisation tests — tests that capture what the code currently does, not what you wish it did. Run them, confirm they pass. Only then continue TDD from that foundation forward.

Either way: your next non-test action must be justified by a failing test you've already seen fail.

## Core principle

Watch the test fail. If you didn't see it fail, you don't know it tests anything.

A test that passes immediately proves nothing — it might be testing existing behaviour, or nothing at all.

## The cycle

**RED** — write one test for one behaviour. Stop. Do not write the implementation yet.

Run just that test. Confirm: it fails (not errors), for the right reason — feature missing, not a typo or import problem. Do not proceed until failure is confirmed.

```
# Python/pytest
pytest -x -k test_name_here
# JavaScript/Jest
npx jest --testNamePattern="test name here"
# Go
go test -run TestName ./...
# .NET
dotnet test --filter "TestName"
```

**GREEN** — write the minimal code to pass that test. Nothing more. Resist adding anything the test doesn't require — no extra methods, no anticipated cases. Run the full suite and confirm everything passes.

**REFACTOR** — ask: "Anything worth cleaning up — duplication, names, helpers?" If no, move on. If yes, clean up without adding behaviour. Tests stay green.

## Session protocol

The human's value is in scoping and direction, not running commands:

0. **Plan together** — human describes the behaviour; AI asks clarifying questions until the target is unambiguous
1. AI writes the failing test and runs it — confirms failure before proceeding
2. AI writes minimal implementation and runs the full suite — confirms everything passes
3. **Checkpoint** — AI asks: "Clean up anything, or what's next?" Human decides direction

Never write test + implementation together. That's not TDD — it's code with an attached test.

## Vertical slices

```
Wrong (horizontal):  test1, test2, test3 → impl1, impl2, impl3
Right (vertical):    test1 → impl1 → test2 → impl2 → test3 → impl3
```

Each cycle responds to what the last one taught you. Tests written before implementation answer "what should this do?" — tests written after answer "what does this do?"

## Mocking

Mock at system boundaries only: external APIs, network I/O, file system, time, randomness.

Don't mock your own modules. If internal code is hard to test without mocking it, the design is the problem — the coupling is what needs fixing. When you do mock, mock the complete data structure; partial mocks hide structural assumptions.

## Test quality

Name the behaviour: `test_rejects_empty_email`, not `test_email`. Test observable outcomes, not implementation steps. A test that breaks when you rename a private function is testing the wrong level.

## Python/pytest patterns

For multiple inputs to the same behaviour, use `@pytest.mark.parametrize` — one parametrized test rather than several near-identical ones.

Shared setup belongs in `conftest.py`. Don't repeat fixture logic across test files.

If a module doesn't exist yet, create a stub that raises `NotImplementedError` so the test fails for the right reason (missing feature) rather than an import error.

## Bug fixes

Write a failing test that reproduces the bug. Confirm the failure. Then fix the code. Never fix first — the test is proof the bug existed and now doesn't.

## When tests are hard to write

Difficulty is signal, not inconvenience:
- Interface too complex → simplify it
- Too many dependencies → inject them or decouple
- Wrong level → go higher to behaviour or lower to a pure function

## Anti-patterns

- **Testing mock behaviour** — asserting a mock was called tests the mock, not your code. Test outcomes.
- **Horizontal slicing** — all tests then all implementation. You end up testing assumed structure.
- **Over-mocking internals** — prefer real interfaces; mocking your own modules signals design coupling.
- **Implementation-detail tests** — if renaming a private function breaks a test, the test is wrong.
- **Test-only production methods** — if a method exists only to support tests, put it in test utilities.
