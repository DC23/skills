# Handoff: 2026-06-16-1600 Triage epic #46 and CLAUDE.md source/installed clarification

## Summary

**Baseline:** No automated test suite in use this session — skill files are markdown, no code artefacts. Two open PRs on GitHub ready for review and merge.

**Outstanding:**
- PR `feat/triage-epic-46` — triage skill changes for issues #32, #37, #47; awaiting maintainer review and merge
- PR `fix/claude-md-skills-source-clarification` — CLAUDE.md convention fix; awaiting maintainer review and merge

---

## What happened

### Epic #46 sub-issues implemented

Three `ready-for-agent` triage skill issues were implemented in a single commit on branch `feat/triage-epic-46`, all changes to `skills/engineering/triage/SKILL.md`:

**#37 — Exclude epics from triage**
- Epics silently excluded from all three "Show what needs attention" buckets
- New step 0 in "Triage a specific issue": detect `epic` label early, refuse with a redirect to `/grill-with-docs` or plan mode, apply no labels

**#47 — Apply `question` label when deferring for grilling**
- Step 4 extended: when an issue must be deferred because it requires further grilling before a state can be assigned, apply `question` + `needs-triage`
- Distinguishes "parked, needs a session" from "not yet looked at"

**#32 — Surface `/to-issues` for broad issues**
- `ready-for-agent` and `ready-for-human` outcome bullets rewritten to include a breadth check before writing a brief
- Heuristic signals described: enumerated deliverables, independently-verifiable acceptance criteria, multi-domain context risk
- Maintainer asked first; declines without friction

Agent briefs for all three issues were read for acceptance criteria. The brief for #47 included "update both source and installed skill files" — flagged as incorrect per the source/installed convention (see below).

### CLAUDE.md source/installed distinction

A mid-session intervention: I was about to edit `.claude/skills/triage/SKILL.md` (the installed copy) rather than `skills/engineering/triage/SKILL.md` (the source). Root cause: CLAUDE.md described the relationship but never stated the operational rule.

Fixed in commit `959c8eb` on branch `fix/claude-md-skills-source-clarification`:
- "What This Repo Is": strengthened to "source of truth / build artefact / never edit directly"
- "Working on Skills": leading bold rule added, with recovery action for briefs that say "update both"

This is the memo that was missing — the previous session's brief author and I both hit the same gap.

## Artefacts

- `skills/engineering/triage/SKILL.md` — all three issue changes
- `CLAUDE.md` — source/installed convention rule
- Branch `feat/triage-epic-46` (commit `375d99a`)
- Branch `fix/claude-md-skills-source-clarification` (commit `959c8eb`)
