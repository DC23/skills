---
name: project-handoff
description: Summarise the current session and update project documents so the work can continue efficiently in a fresh session. Use at the end of a session when the user indicates that work in the current session is complete, that it's time for a project handoff, or that the session is done/over/finished.
argument-hint: "What will the next session be used for?"
---

## Workflow

1. Update project memory with any new information from the session.
2. Check whether an incomplete plan exists. If so, save it to `./docs/plans/` and reference it in the handoff document.
3. For each plan referenced or touched during this session, update its status tag in `docs/plans/INDEX.md`. Valid tags are `[pending]`, `[partial]`, or `[done]`. When the outcome is clear from the session, apply the tag directly; when uncertain, ask the user before writing. If `docs/plans/INDEX.md` does not exist, skip this step silently.
4. Check whether any critical decisions were made that are not yet captured in an ADR. If so, create a new ADR in `./docs/adr/` following the format in `docs/agents/adr.md`. Maintain the ADR index. Reference it in the handoff document.
5. Identify candidate Ubiquitous Language terms that emerged this session. The standard is DDD Ubiquitous Language: domain entities, relationships, and named processes that domain experts and developers would use consistently — not implementation details or incidental vocabulary. For each candidate: check whether it is already defined in `docs/DOMAIN_DICTIONARY.md` (it may already be in context from `session-start`); if not defined, append an entry to `docs/DOMAIN_CANDIDATES.md` (create the file if absent) using the format in `docs/agents/domain.md`. Be conservative — fewer, well-chosen candidates are more useful than a long list of noise.
6. Write the handoff document to `./docs/handoffs/` following the template at `docs/handoffs/TEMPLATE.md`:
   - Summary block first (Baseline and Outstanding fields, as defined in the template)
   - Free-form narrative sections below — use whatever headings suit the session
   - List outstanding work only for items explicitly present in the session: uncommitted code, incomplete plan steps, things the user flagged as not done. Do not invent next steps. Omit the Outstanding field entirely if nothing is outstanding.
   - Reference existing artefacts (plans, ADRs, commits, diffs) by path or URL; do not duplicate their content
   - Use the vocabulary from `docs/DOMAIN_DICTIONARY.md` consistently
   - Redact any sensitive information (API keys, passwords, PII)
   - If arguments were passed, treat them as the next session's focus and tailor the document accordingly
   - Append a one-line entry to `./docs/handoffs/INDEX.md` — filename link plus a short list of searchable topics and artefacts (enough to locate the file without opening it)

## Filename Format

Use the following format for plan and handoff filenames:
`YYYY-MM-DD-HHMM-description.md`

Where:
- `YYYY` is the 4-digit year
- `MM` is the 2-digit month
- `DD` is the 2-digit day
- `HHMM` is the 4-digit time in 24-hour format (hours and minutes)
- `description` is a brief, hyphen-separated description of the handoff content (e.g. "equipment-extraction")
