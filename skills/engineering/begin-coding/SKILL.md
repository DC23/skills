---
name: begin-coding
description: Start a coding session by loading project context, domain model, and session conventions, then confirming the baseline test state. Use at the start of a session when the user says "begin coding", "start the session", "let's begin", or invokes /begin-coding.
---

## Workflow

Run these steps once on invocation, in order. Do not begin any implementation work until step 7 is complete.

1. **Load project memory** — read the project memory index if one exists. Note any standing guidance relevant to this session.

2. **Load domain model** — if `docs/DOMAIN_DICTIONARY.md` exists, read it. This vocabulary is in effect for the session.

3. **Activate TDD** — the `/tdd` skill governs all implementation this session. Read it now if it is not already in context.

4. **Read the last handoff summary** — if `docs/handoffs/INDEX.md` exists, open it and locate the most recent entry. Open that handoff file and read the **Summary block only** — the content above the first `---` separator (Baseline and Outstanding fields). Do not read further.

5. **Load the active plan** — if the handoff references a plan file in `docs/plans/`, read that plan. If no plan is referenced but plan files exist, ask the user which one is relevant to today's work.

6. **Run the test suite** — run the project's test command. Confirm a clean baseline. If tests are failing, report this immediately and do not proceed until the user has acknowledged the state.

7. **Report ready** — two to three sentences: current baseline state, what was outstanding from the last session (if anything), and the active plan or today's focus. Then wait for direction.

## Standing instructions

These conventions are in effect for the whole session, until `/project-handoff` is invoked.

- **Before re-deriving past work**: check `docs/handoffs/INDEX.md`. If a prior handoff covers the topic, read its Summary block before asking the user.
- **All implementation uses TDD**: red-green-refactor per `/tdd`. No implementation without a failing test.
- **Domain vocabulary**: use terms from `docs/DOMAIN_DICTIONARY.md` consistently. Flag terms that appear repeatedly and may warrant a dictionary entry — they become candidates at handoff.
- **Before architectural decisions**: check `docs/adr/INDEX.md`. If a relevant ADR exists, read it before proceeding.
- **If deeper session context is needed**: read the relevant handoff document in full. The narrative sections contain referenced artefacts, decisions, and context not captured in the Summary block.
