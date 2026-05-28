---
name: domain-review
description: Review pending domain candidate terms and decide whether to promote them into the domain dictionary, reject them, or defer. Use when the user wants to work through DOMAIN_CANDIDATES.md, refine the domain model, or review terms that have been flagged during previous sessions.
---

# Domain Review

Work through the pending entries in `docs/DOMAIN_CANDIDATES.md` and update the domain dictionary accordingly.

## Process

### 1. Load context

Read `docs/agents/domain.md` for format rules. Read `docs/DOMAIN_DICTIONARY.md` if it exists — you need to know what's already defined before evaluating candidates.

Read `docs/DOMAIN_CANDIDATES.md`. If the file does not exist or contains no `pending` entries, tell the user and stop.

### 2. Review each pending entry

Take entries one at a time. For each one, tell the user the term and its flagged note, then grill them to reach a decision. Ask questions one at a time, waiting for the answer before continuing:

- Is this a genuine domain concept — something domain experts and developers would use consistently — or is it an implementation detail or incidental vocabulary?
- Does it conflict with or duplicate an existing term in the dictionary? If so, should it become an alias or replace the existing term?
- What is the precise one-sentence definition?
- Does its meaning depend on its relationship to another term? (Only ask if this seems likely.)
- Is this the right name? Was an alternative considered and rejected? (Only ask if the choice seems non-obvious.)

Recommend an outcome for each question rather than leaving it entirely open.

### 3. Act on the decision

**Promote** — write the entry to `docs/DOMAIN_DICTIONARY.md` using the format in `docs/agents/domain.md`. Delete the entry from `docs/DOMAIN_CANDIDATES.md`.

**Reject** — update the entry's status line in `docs/DOMAIN_CANDIDATES.md` to:
```
**Status:** rejected — <reason>
```
Leave it in the file. Rejected entries prevent the same term being re-litigated in future sessions.

**Defer** — leave the entry as `pending`. Optionally append a short note under the existing text explaining what needs to be resolved before it can be decided.

### 4. ADR check

After all entries are processed, consider whether any decisions made during this session meet the ADR threshold:

1. Hard to reverse
2. Surprising without context
3. The result of a real trade-off

If so, write the ADR to `docs/adr/` and update `docs/adr/INDEX.md`. Use the format in `docs/agents/adr.md`.
