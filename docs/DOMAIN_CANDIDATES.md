# Domain Candidates

## Source Skill

**Status:** pending
**Source:** docs/handoffs/2026-06-16-1600-triage-epic-46-claude-md.md

A skill as it exists in `skills/engineering/<name>/` — the authoritative, editable copy. Distinct from the installed skill. The confusion between the two caused a mid-session intervention and a CLAUDE.md fix this session.

## Installed Skill

**Status:** pending
**Source:** docs/handoffs/2026-06-16-1600-triage-epic-46-claude-md.md

A skill as it exists in `.claude/skills/<name>/` — the copy the harness invokes at runtime. Populated by the install script from the source skill. Never edited directly.

## Agent Brief

**Status:** pending
**Source:** docs/handoffs/2026-06-05-1600-issues-24-31-tdd-reflection.md

The structured specification produced by the triage skill for a `ready-for-agent` issue. An Agent Brief provides enough behavioural detail, acceptance criteria, and constraints that an agent can implement without requiring step 0 of the TDD session protocol to fire. Distinct from a general issue description in that it is deliberately complete — triage is the gate that makes it so.
