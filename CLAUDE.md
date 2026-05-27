# Skills Repository

A personal collection of Claude Code skills, developed and maintained by DC23.

## What This Repo Is

Each skill lives in `skills/<name>/` and contains at minimum a `SKILL.md` — the instruction file loaded when the skill is invoked. Some skills include a `PROVENANCE.md` noting upstream sources.

Skills installed into the Claude Code harness live in `.claude/skills/`. The `skills/` directory is the source; `.claude/skills/` is where the harness reads from.

## Skill Structure

```
skills/<name>/
  SKILL.md        # Required. Frontmatter + workflow instructions.
  PROVENANCE.md   # Optional. Upstream attribution and licence notes.
```

Frontmatter fields in `SKILL.md`:

- `name` — matches the directory name and the slash command
- `description` — used by the harness to decide when to auto-invoke; be specific
- `argument-hint` — shown in the UI when the user invokes the skill with arguments
- `disable-model-invocation` — set `true` to prevent recursive model calls (useful for review/audit skills)

## Working on Skills

Use `/skill-creator` to create, edit, evaluate, or benchmark skills. It handles the full lifecycle: drafting, evals, description optimisation, and packaging.

Use `/review-plugin` before installing any third-party skill.

## Agent skills

### Issue tracker

Issues are tracked in GitHub Issues on `DC23/skills`. See `docs/agents/issue-tracker.md`.

### Triage labels

Uses the five canonical triage labels with default strings. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout: one `DOMAIN_DICTIONARY.md` at the repo root, `docs/adr/` for decisions. See `docs/agents/domain.md`.

## Conventions

- British English in skill prose
- Keep skill instructions focused — one skill, one job
- Reference upstream sources in `PROVENANCE.md`, not in `SKILL.md`
- Eval output goes in `.claude/evals/` (gitignored)
