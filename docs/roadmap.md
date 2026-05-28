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
| `setup-dc23-skills` | Done | 2 | Artefact formats (Phase 1) |
| `to-issues` | Done (DC23 revision) | 2 | `setup-dc23-skills` |
| `project-handoff` | Heavy revision | 3 | Artefact formats (Phase 1) |
| `grill-with-docs` | Done (DC23 fork) | 4 | `DOMAIN_DICTIONARY.md` format |
| `domain-review` | Done (new skill) | 4 | `DOMAIN_DICTIONARY.md` format |
| `triage` | Substantial revision | 4b | `setup-dc23-skills`, `grill-with-docs` |
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

Status: implementation complete

Built `setup-dc23-skills`: interactive and prompt-driven, modelled on `setup-matt-pocock-skills`. Walks the user through three decisions (issue tracker, triage labels, domain docs). Domain docs section targets `DOMAIN_DICTIONARY.md` instead of `CONTEXT.md`. Seed templates for all Phase 1 artefacts (`docs/agents/domain.md`, `adr.md`, `plans.md`, `docs/handoffs/TEMPLATE.md`) are bundled in `assets/` within the skill directory.

`to-issues` received a full DC23 revision (beyond the originally scoped one-liner): neutral HITL/AFK framing (removed "prefer AFK over HITL"), per-type triage label assignment on publish (HITL → `ready-for-human`, AFK → `ready-for-agent`), `DOMAIN_DICTIONARY.md` vocabulary reference, and `## Type` field added to the issue body template. Proper source created at `skills/engineering/to-issues/`.

### Phase 3 — Update `project-handoff` (DC23/skills#11)

Status: implementation complete

Update the existing skill to write to the new artefacts:

- Domain terms: the skill **flags** candidate terms in the handoff document ("these terms appeared this session and may warrant dictionary entries") rather than writing them to `DOMAIN_DICTIONARY.md` directly. `domain-review` is the write path for the dictionary; `project-handoff` feeds it a backlog. This keeps handoff lightweight and dictionary entries properly reasoned.
- Handoff output follows the Phase 1 template; the skill references it explicitly
- ADR index is maintained alongside each new ADR entry

#### Notes from user

- domain terms can't be flagged into harness memory. I work across machines, or with small teams. The implementation of candidate terms needs a source controlled backlog file in the project, so it's persistent and shared. Once reviewed and added to the domain dictionary, they can be deleted but if reviewed and not added then perhaps they should be retained with a reason for why they weren't added. This can avoid reprosecuting the same terms again later. Or maybe they are an alias or duplicate, and added to the domain dictionary as aliases to avoid.

### Phase 4 — `grill-with-docs` and `domain-review` (DC23/skills#12)

Two skills, not one. Planning revealed that "grill a plan using domain docs" and "maintain the domain model" are distinct jobs that shouldn't share a name or a skill.

**`grill-with-docs`** — DC23 fork of mattpocock's `grill-with-docs`. Swaps `CONTEXT.md` → `docs/DOMAIN_DICTIONARY.md`, removes multi-context branch, points format references at `docs/agents/domain.md` and `docs/agents/adr.md`. Episodic; triggered before major work or new project phases to stress-test a plan against established language.

**`domain-review`** — Original skill. Works through `docs/DOMAIN_CANDIDATES.md` entries one at a time, grilling the user on each to decide: promote to the dictionary, reject with reason (retained to prevent re-litigation), or defer. The primary write path for `docs/DOMAIN_DICTIONARY.md`; `project-handoff` feeds it candidates.

### Phase 4b — Revise `triage` (DC23/skills#14)

Status: implementation complete

**Category model** — extended from two categories to three: `bug`, `enhancement` (community-requested), and `roadmap` (planned project work). `roadmap` wontfix path skips `.out-of-scope/`; `.out-of-scope/` check in gather-context is also skipped for roadmap issues.

**Reference updates** — `/setup-matt-pocock-skills` → `/setup-dc23-skills`. The `/grill-with-docs` reference was already correct.

**ADR linkage** — `OUT-OF-SCOPE.md` now includes guidance on referencing a relevant ADR in the reason section when a rejection is grounded in an architectural decision. No bidirectional linkage from ADRs.

**Category labels** — `setup-dc23-skills` extended to ensure `bug`, `enhancement`, and `roadmap` labels exist on GitHub repos alongside the existing triage state labels.

**Missing triage labels** (noted in issue): not a triage skill problem — resolved by running `/setup-dc23-skills`.

### Phase 5 — `session-start` (DC23/skills#13)

Build the session-open counterpart to `project-handoff`. The skill has two distinct sections:

**Workflow** — what the skill does on invocation:

1. Load memory index
2. Load `docs/DOMAIN_DICTIONARY.md`
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

- **`improve-codebase-architecture`** — find architecture improvement opportunities informed by domain language and ADRs. References `CONTEXT.md` explicitly; would need the same `DOMAIN_DICTIONARY.md` adaptation already done for `grill-with-docs`. Low effort once that pattern is established.
- **`to-prd`** — turn conversation context into a PRD submitted as a GitHub issue. Self-contained; unlikely to need more than a bootstrap skill reference update.
- **`zoom-out`** — prompt the agent for broader context on an unfamiliar section of code. Very lightweight; may need no modification at all.

Deferred with no immediate use: `diagnose`, `prototype`.

---

## Open questions

- **`docs/issues.md`** — the original braindump flagged this as an on-disk issue tracker for projects without a remote. No clear design yet and the repo uses GitHub Issues. Left out of scope until there is a concrete use case.
- **Utility skills directory name** — resolved during Phase 0: `skills/utility/`.
