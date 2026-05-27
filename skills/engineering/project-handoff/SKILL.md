---
name: project-handoff
description: Summarise the current session and update project documents so the work can continue efficiently in a fresh session. Use at the end of a session when the user indicates that work in the current session is complete, that it's time for a project handoff, or that the session is done/over/finished.
argument-hint: "What will the next session be used for?"
---

## Workflow

1. Update project memory with any new information from the session.
2. Check whether an incomplete plan exists. If so, save it to `./docs/plans/` and reference it in the handoff document.
3. Check whether any critical decisions were made that are not yet captured in an ADR. If so, create a new ADR in `./docs/adr/` following the template and naming convention defined in `/grill-with-docs`. Reference it in the handoff document.
4. Check whether any new domain terms or concepts emerged in the session. If so, add entries to `./docs/CONTEXT.md` following the format defined in `/grill-with-docs`.
5. Write the handoff document to `./docs/handoffs/`:
   - Summarise the session
   - List outstanding work — but only items explicitly present in the session: uncommitted code, incomplete plan steps, things the user flagged as not done. Do not invent next steps. If nothing is outstanding, omit the section entirely.
   - Reference existing artifacts (PRDs, plans, ADRs, commits, diffs) by path or URL; do not duplicate their content
   - Consult `./docs/CONTEXT.md` for established terminology and use it consistently
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
