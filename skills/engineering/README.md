# Engineering Skills

These skills are built around how I prefer to work with an AI coding agent. Quality over speed, code I can still read six months later, human oversight at the decisions that matter. Writing code isn't the bottleneck anymore — understanding what's been built is. Fine-grained commits, readable PRs, TDD, and DDD are how I try to keep that from getting away from me.

I've been heavily inspired by the fantastic work of Matt Pocock. If you're reading this, then you definitely need to look at his [Skills](https://github.com/mattpocock/skills). You'll recognise many of the skill names, but my versions are different - changes noted in the provenance files. I think of this as "pseudo-forking". I didn't fork Matt's actual repo because it's huge and Matt is prolific. I only wanted a few needles, not the entire haystack.

---

Skills are ordered by use in a session.

- **[setup-dc23-skills](./setup-dc23-skills/SKILL.md)** — Bootstrap a new project with the DC23 engineering skill configuration: issue tracker, triage labels, domain docs, and handoff template.
- **[begin-coding](./begin-coding/SKILL.md)** — Start a coding session by loading project context, domain model, and session conventions, then confirming the baseline test state.
- **[grill-with-docs](./grill-with-docs/SKILL.md)** — Stress-test a plan against the project's established domain language and documented decisions; updates the domain dictionary and ADRs inline as terms resolve.
- **[to-issues](./to-issues/SKILL.md)** — Break a plan into independently-grabbable vertical-slice issues on the project issue tracker.
- **[tdd](./tdd/SKILL.md)** — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
- **[project-handoff](./project-handoff/SKILL.md)** — Summarise the current session and update project documents so work can continue efficiently in a fresh session.
- **[domain-review](./domain-review/SKILL.md)** — Work through pending domain candidate terms one at a time, promoting, rejecting, or deferring each into the domain dictionary.
- **[triage](./triage/SKILL.md)** — Move issues through a triage state machine: classify, reproduce, grill, brief, and close.
