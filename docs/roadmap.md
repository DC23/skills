# Dev-Tooling Skill Ecosystem Roadmap

*Supersedes `dev-tooling-ideas.md`. See that file for the original braindump.*

---

## Vision

A coding session has a shape: it starts, it runs, it ends. The skills in this ecosystem follow that shape explicitly. Invoking `session-start` is a declaration — *this is a coding session, get ready for that*. It bootstraps context from on-disk artefacts, loads behavioural conventions, and confirms the baseline test state. `project-handoff` closes the session, updating artefacts and writing a structured handoff document so the next session can pick up without re-deriving context.

This pairing is the core pattern. It is composable: other session types could have their own bookend skills without interference, and `CLAUDE.md` stays clean because session-specific conventions live in the skill, not the config file.

The skills depend on standardised on-disk artefacts. Those artefacts — a domain dictionary, indexed handoff documents, an ADR index — are designed to be read selectively. A skill loads the summary block of the last handoff, not the whole document. It reads the domain dictionary to understand terminology, not to scan a flat glossary. The structure carries meaning; the names signal intent.

This ecosystem is heavily inspired by [Matt Pocock's engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering). Where skills are derived from that work, provenance is recorded in `PROVENANCE.md` files alongside the skill. The licence is compatible (MIT).

---

## Ecosystem map

### Skills

| Skill | Status | Phase | Depends on |
| --- | --- | --- | --- |
| `tdd` | Done (heavy revision) | — | — |
| `setup-dc23-skills` | To build | 2 | Artefact formats (Phase 1) |
| `to-issues` | Minor revision | 2 | `setup-dc23-skills` |
| `project-handoff` | Heavy revision | 3 | Artefact formats (Phase 1) |
| `grill-with-domain` | To build | 4 | `DOMAIN_DICTIONARY.md` format |
| `triage` | Substantial revision | 4b | `setup-dc23-skills`, `grill-with-domain` |
| `session-start` | To build | 5 | Handoff template, `DOMAIN_DICTIONARY.md`, `tdd` |

`setup-matt-pocock-skills` is superseded by `setup-dc23-skills` for this ecosystem. `to-issues` and `triage` are installed from mattpocock/skills and will be revised in place.

### Artefacts

| Artefact | Purpose | Defined in |
| --- | --- | --- |
| `DOMAIN_DICTIONARY.md` | Domain model, entity relationships, terminology and the *why* behind it. Replaces `CONTEXT.md`. | Phase 1 |
| `docs/handoffs/TEMPLATE.md` | Canonical handoff document structure; consistent summary block for selective reading. | Phase 1 |
| ADR index format | One-line scannable entry per ADR; maintained alongside each new record. | Phase 1 |

---

## Phased plan

Each phase has its own planning session before implementation begins. The phases below define scope and sequencing; the details get unpacked when each phase starts.

### Phase 0 — Reorganise skill directories

Status: implementation complete

Mirror the mattpocock repository layout: engineering skills in a subdirectory, general utility skills in a separate one.

- Create `skills/engineering/` and move `tdd/` and `project-handoff/` into it
- Add `skills/engineering/README.md`
- Create a directory for general utility skills (name TBD) and move `review-plugin/` into it, with its own README
- All new engineering skills land in `skills/engineering/` from the start

### Phase 1 — Standardise artefacts (DC23/skills#9)

Status: implementation complete

Design the artefact formats before any skill is written or updated. This phase is primarily a design and writing session, not implementation.

1. **`DOMAIN_DICTIONARY.md` format** — define sections, distinguish the structure from a flat glossary, establish what moves here from `CONTEXT.md` and what doesn't. The name implies richer structure: entity relationships, concept definitions, and the *why* behind terminology choices, not just a vocabulary list.
2. **Handoff doc template** — define the standard summary block (fields, location, length constraints). Stored as `docs/handoffs/TEMPLATE.md`. Both `project-handoff` and `session-start` depend on this being stable.
3. **ADR index format** — one-line entry per ADR: filename link plus searchable topics. Simple, but needs a canonical form before skills start maintaining it.

### Phase 2 — `setup-dc23-skills` and `to-issues` (DC23/skills#10)

Build the bootstrapper that creates the Phase 1 artefacts in any new project. Writing the setup skill forces the artefact formats to be fully specified — the seed templates bundled with the skill are the canonical definitions.

Modelled on `setup-matt-pocock-skills`: interactive and prompt-driven, not a deterministic script. Walks the user through three decisions (issue tracker, triage labels, domain docs) and writes the configuration. Domain docs section targets `DOMAIN_DICTIONARY.md` instead of `CONTEXT.md`. Seed templates for all Phase 1 artefacts are co-located in the skill directory.

`docs/agents/domain.md` in this repo is both the live instruction file for agent sessions and the staging source for the seed file bundled with this skill. When building `setup-dc23-skills`, copy it as the seed and remove the `skills/` entry from the file structure diagram (the only repo-specific line).

Also in this phase: update `to-issues` — one line, replacing the `/setup-matt-pocock-skills` reference with `/setup-dc23-skills`. No other changes needed.

### Phase 3 — Update `project-handoff` (DC23/skills#11)

Update the existing skill to write to the new artefacts:

- Domain terms: the skill **flags** candidate terms in the handoff document ("these terms appeared this session and may warrant dictionary entries") rather than writing them to `DOMAIN_DICTIONARY.md` directly. `grill-with-domain` is the write path for the dictionary; `project-handoff` feeds it a backlog. This keeps handoff lightweight and dictionary entries properly reasoned.
- Handoff output follows the Phase 1 template; the skill references it explicitly
- ADR index is maintained alongside each new ADR entry

### Phase 4 — `grill-with-domain` (DC23/skills#12)

Fork `grill-with-docs` to target `DOMAIN_DICTIONARY.md`. The grilling questions need adapting for domain-model structure (entity relationships, terminology decisions, the *why* behind names) rather than a flat context dump. The skill also maintains the ADR index on decisions crystallised during the session.

### Phase 4b — Revise `triage` (DC23/skills#14)

More than a reference update. Two areas of work:

**Category model** — extend from two categories (`bug`, `enhancement`) to three: `bug`, `enhancement` (community-requested), and `roadmap` (planned project work). The distinction is semantically meaningful — a roadmap issue doesn't require community validation or the same fleshing-out process as a cold feature request, and it's a common pattern across projects.

**Reference updates** — replace `/setup-matt-pocock-skills` with `/setup-dc23-skills` and `/grill-with-docs` with `/grill-with-domain`.

Note: the state role labels (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`) are absent from the repo — likely due to an interrupted setup session rather than a deliberate omission. Confirm whether `setup-dc23-skills` needs to own this or whether it's handled by completing setup.

### Phase 5 — `session-start` (DC23/skills#13)

Build the session-open counterpart to `project-handoff`. The skill has two distinct sections:

**Workflow** — what the skill does on invocation:
1. Load memory index
2. Load `DOMAIN_DICTIONARY.md`
3. Load `tdd` skill
4. Read the summary block from the most recent handoff doc (not the full document — this is why the Phase 1 template matters)
5. Read the most relevant open plan, if one exists
6. Run the test suite and confirm baseline state
7. Report ready

**Standing instructions** — behavioural conventions that govern the session, replacing what would otherwise clutter `CLAUDE.md`:
- Check `docs/handoffs/INDEX.md` before re-deriving past work
- Use `tdd` for all implementation tasks
- Other session conventions as they emerge

---

## Someday-maybe

Skills from the mattpocock engineering ecosystem not in the active roadmap:

- **`improve-codebase-architecture`** — find architecture improvement opportunities informed by domain language and ADRs. References `CONTEXT.md` explicitly; would need the same `DOMAIN_DICTIONARY.md` adaptation as `grill-with-domain`. Low effort once that pattern is established.
- **`to-prd`** — turn conversation context into a PRD submitted as a GitHub issue. Self-contained; unlikely to need more than a bootstrap skill reference update.
- **`zoom-out`** — prompt the agent for broader context on an unfamiliar section of code. Very lightweight; may need no modification at all.

Deferred with no immediate use: `diagnose`, `prototype`.

---

## Open questions

- **`docs/issues.md`** — the original braindump flagged this as an on-disk issue tracker for projects without a remote. No clear design yet and the repo uses GitHub Issues. Left out of scope until there is a concrete use case.
- **Utility skills directory name** — to be decided during Phase 0, with the full range of skills that will eventually live there in mind (including skills with GPL constraints not yet in this repo).
