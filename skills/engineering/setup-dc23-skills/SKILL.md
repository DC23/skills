---
name: setup-dc23-skills
description: Sets up an `## Agent skills` block in CLAUDE.md/AGENTS.md and `docs/agents/` so the DC23 engineering skills know this repo's issue tracker (GitHub or local markdown), triage label vocabulary, and domain doc layout. Also seeds `docs/handoffs/TEMPLATE.md`, ADR conventions, and plans conventions. Run before first use of `to-issues`, `triage`, `project-handoff`, `grill-with-docs`, `domain-review`, or `session-start` — or if those skills appear to be missing context about the issue tracker, triage labels, or domain docs.
disable-model-invocation: true
---

# Setup DC23 Skills

Scaffold the per-repo configuration that the DC23 engineering skills assume:

- **Issue tracker** — where issues live (GitHub by default; local markdown is also supported)
- **Triage labels** — the strings used for the five canonical triage roles
- **Domain docs** — where `docs/DOMAIN_DICTIONARY.md` and ADRs live, and the consumer rules for reading them

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config` — is this a GitHub repo? Which one?
- `AGENTS.md` and `CLAUDE.md` at the repo root — does either exist? Is there already an `## Agent skills` section in either?
- `docs/DOMAIN_DICTIONARY.md`
- `docs/adr/`
- `docs/handoffs/`
- `docs/agents/` — does this skill's prior output already exist?
- `.scratch/` — sign that a local-markdown issue tracker convention is already in use

### 2. Present findings and ask

Summarise what's present and what's missing. Then walk the user through the three decisions **one at a time** — present a section, get the user's answer, then move to the next. Don't dump all three at once.

Assume the user does not know what these terms mean. Each section starts with a short explainer (what it is, why these skills need it, what changes if they pick differently). Then show the choices and the default.

**Section A — Issue tracker.**

> Explainer: The "issue tracker" is where issues live for this repo. Skills like `to-issues` and `triage` read from and write to it — they need to know whether to call `gh issue create`, write a markdown file under `.scratch/`, or follow some other workflow you describe. Pick the place you actually track work for this repo.

Default posture: these skills were designed for GitHub. If a `git remote` points at GitHub, propose that. If a `git remote` points at GitLab (`gitlab.com` or a self-hosted host), propose GitLab. Otherwise (or if the user prefers), offer:

- **GitHub** — issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab** — issues live in the repo's GitLab Issues (uses the [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Local markdown** — issues live as files under `.scratch/<feature>/` in this repo (good for solo projects or repos without a remote)
- **Other** (Jira, Linear, etc.) — ask the user to describe the workflow in one paragraph; the skill will record it as freeform prose

**Section B — Triage label vocabulary.**

> Explainer: When the `triage` skill processes an incoming issue, it moves it through a state machine — needs evaluation, waiting on reporter, ready for an AFK-agent to pick up, ready for a human, or won't fix. To do that, it needs to apply labels (or the equivalent in your issue tracker) that match strings *you've actually configured*. If your repo already uses different label names (e.g. `bug:triage` instead of `needs-triage`), map them here so the skill applies the right ones instead of creating duplicates.

The five canonical roles:

- `needs-triage` — maintainer needs to evaluate
- `needs-info` — waiting on reporter
- `ready-for-agent` — fully specified, AFK-ready (an agent can pick it up with no human context)
- `ready-for-human` — needs human implementation
- `wontfix` — will not be actioned

Default: each role's string equals its name. Ask the user if they want to override any. If their issue tracker has no existing labels, the defaults are fine.

**Section C — Domain docs.**

> Explainer: Skills like `tdd`, `grill-with-docs`, `domain-review`, `project-handoff`, and `session-start` read a `docs/DOMAIN_DICTIONARY.md` file to understand the project's domain language — entity relationships, terminology decisions, and the *why* behind naming choices. They also read `docs/adr/` for past architectural decisions. This skill will create the `docs/agents/domain.md` file that tells those skills where to look and how to interpret what they find. No decisions are required — just confirm this layout matches your repo's structure.

The DC23 skills always use a single-context layout:

```
docs/
├── DOMAIN_DICTIONARY.md
└── adr/
```

Confirm this matches the target repo. If the user has a significantly different structure, note it and proceed as close to this layout as possible.

Note: `docs/DOMAIN_DICTIONARY.md` is created lazily by `/grill-with-docs`, not by this skill. Its absence is normal.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The contents of `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, `docs/agents/domain.md`

Let them edit before writing.

### 4. Write

**Pick the file to edit:**

- If `CLAUDE.md` exists, edit it.
- Else if `AGENTS.md` exists, edit it.
- If neither exists, ask the user which one to create — don't pick for them.

Never create `AGENTS.md` when `CLAUDE.md` already exists (or vice versa) — always edit the one that's already there.

If an `## Agent skills` block already exists in the chosen file, update its contents in-place rather than appending a duplicate. Don't overwrite user edits to the surrounding sections.

The block:

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout: `docs/DOMAIN_DICTIONARY.md`, `docs/adr/` for decisions. See `docs/agents/domain.md`.
```

Then write the docs files using the seed templates in this skill folder:

- [issue-tracker-github.md](./assets/issue-tracker-github.md) — GitHub issue tracker
- [issue-tracker-gitlab.md](./assets/issue-tracker-gitlab.md) — GitLab issue tracker
- [issue-tracker-local.md](./assets/issue-tracker-local.md) — local-markdown issue tracker
- [triage-labels.md](./assets/triage-labels.md) — label mapping
- [domain.md](./assets/domain.md) — domain doc consumer rules + layout

For "other" issue trackers, write `docs/agents/issue-tracker.md` from scratch using the user's description.

Additionally, write these files silently (no user decision required — they are fixed-format Phase 1 artefacts):

- `docs/agents/adr.md` from [adr.md](./assets/adr.md)
- `docs/agents/plans.md` from [plans.md](./assets/plans.md)
- `docs/handoffs/TEMPLATE.md` from [handoff-template.md](./assets/handoff-template.md) — create `docs/handoffs/` if needed

Do not overwrite any of these files if they already exist and contain user content — check first and skip or ask.

**If GitHub is the chosen issue tracker, ensure the five canonical triage labels exist on the repo:**

1. Run `gh label list --json name --jq '[.[].name]'` to get the current label names.
2. For each of the five label strings from the triage-labels mapping, check if it is already present.
3. Create any that are missing with `gh label create`. Use these defaults:

   | Label             | Colour   | Description                                      |
   |-------------------|----------|--------------------------------------------------|
   | `needs-triage`    | `F5A623` | Maintainer needs to evaluate this issue          |
   | `needs-info`      | `5D93C4` | Waiting on reporter for more information         |
   | `ready-for-agent` | `1BC97E` | Fully specified, ready for an AFK agent          |
   | `ready-for-human` | `E8734A` | Requires human implementation                    |
   | `wontfix`         | `6B6B6B` | Will not be actioned                             |

   Example: `gh label create "needs-triage" --color "F5A623" --description "Maintainer needs to evaluate this issue"`

   Skip any label that already exists — do not update its colour or description.

**Also ensure the three category labels exist on the repo:**

   | Label         | Colour   | Description                              |
   |---------------|----------|------------------------------------------|
   | `bug`         | `d73a4a` | Something isn't working                  |
   | `enhancement` | `a2eeef` | A feature request from the community     |
   | `roadmap`     | `B090EB` | A planned feature on the project roadmap |

   Same rule: skip any that already exist — do not update colour or description.

### 5. Done

Tell the user the setup is complete and which DC23 engineering skills will now read from these files: `to-issues`, `triage`, `project-handoff`, `grill-with-docs`, `domain-review`, `session-start`.

Mention they can edit `docs/agents/*.md` directly later — re-running this skill is only necessary if they want to switch issue trackers or restart from scratch.
