# Dev Tooling Ideas

Captured 2026-05-26. Evolving notes on the skill-based session management tooling.

## Skills to build

### `session-start` skill

Mirror to `project-handoff`. Runs at the beginning of a coding session to bootstrap context from on-disk artefacts.

Goals:

- Low context impact — read selectively, not exhaustively
- Load memory index and DOMAIN_DICTIONARY.md
- Load the TDD skill
- Read the most recent handoff doc (summary/next-steps section, not the whole thing — implies handoff docs need a consistent structure)
- Read the most relevant open plan, if one exists
- Run the test suite to confirm baseline state
- Report ready

Drift-catching belongs in `project-handoff` (context of what was just done is available there). Session-start does a quick sanity check only — test pass/fail is the primary anchor.

The skill has two sections:

1. **Workflow sequence** — what the skill does on invocation (load artefacts, run tests, report ready)
2. **Standing instructions** — behavioural conventions that govern the session, replacing what would normally live in CLAUDE.md. Examples:
   - "When the user signals that past work is relevant, or when you're about to re-derive something, check docs/handoffs/INDEX.md first."
   - "Use the TDD skill for all implementation tasks."

### Fork of `grill-with-docs` skill

The upstream skill targets `CONTEXT.md`. Fork and adapt to:

- Target `DOMAIN_DICTIONARY.md` instead
- Potentially invite richer structure suited to a dictionary/domain model rather than a flat context dump

## Artefacts to standardise

### `DOMAIN_DICTIONARY.md` (replacing `CONTEXT.md`)

Captures the domain model and its language — entity relationships, key concepts, and the *why* behind terminology. Not a flat glossary. Name signals "look this up to understand the problem space."

### `docs/issues.md`

Canonical on-disk issue and bug tracker. Git-ignored. Gives handoff and session-start a consistent place to read and update open work, priorities, and known bugs. Currently missing from this project — nebulous state is a gap.

### Handoff doc structure

Needs a consistent summary block (current state / next steps) at a findable location so session-start can read just that section rather than the full document.

Current gap: `project-handoff` is prescriptive about sequence but not about document structure. A reference template bundled with the skill (co-located in the skill directory alongside SKILL.md) would fix this — the skill can reference or inline it as guidance when writing. Keeps structure and behaviour together rather than letting them drift apart.

### ADR index

Same pattern as the handoff index — a short description per entry makes the ADR directory scannable without opening each file. Avoids a treasure hunt when looking for a past decision. The grill-with-docs fork (or project-handoff) should maintain it alongside the ADR it just wrote.

## Design intent: skill as session-type declaration

Not all agent sessions are coding sessions, so a CLAUDE.md can't unconditionally run a coding workflow — it would load irrelevant context for writing or planning sessions. Invoking `session-start` is an explicit signal: "this is a coding session, get ready for that." Other session types get a different invocation or none at all.

The `session-start` / `project-handoff` pairing bookends a coding session. The pattern is composable: other session types could have their own skill pairings without interference.

The skill is also formalising a manual ritual — the same bootstrapping prompt typed at the start of every coding session. The current manual prompt is the starting point for the skill spec: capture it and refine from there.

## To Do

- organise this file. Right now it's a chaotic braindump of thoughts.
- build and priortise issues for this repo
