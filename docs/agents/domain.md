# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`DOMAIN_DICTIONARY.md`** at the repo root
- **`docs/adr/`** — read ADRs that touch the area you're about to work in.

**If any of these files don't exist, proceed silently.** Don't flag their absence; don't suggest creating them upfront. Absence is normal — not every project needs a domain dictionary, and the artefacts are created lazily when terms or decisions actually get resolved. `/grill-with-domain` creates `DOMAIN_DICTIONARY.md`; new ADRs are written when decisions warrant them.

## File structure

Single-context repo:

```
/
├── DOMAIN_DICTIONARY.md
├── docs/adr/
│   ├── 0001-example-decision.md
│   └── ...
└── skills/
```

## Domain dictionary entry format

Entries use a second-level heading for the term. The definition is the only required element. Optional fields are added only when their omission would genuinely confuse a reader:

```markdown
## TermName

One precise sentence definition.

**Relationships:** [only when the entity's meaning depends on its connection to another term]
**Why this name:** [only when a competing term was rejected, or the choice is non-obvious]
```

Most entries will be a heading and a single sentence. Don't add optional fields formulaically.

## Use the dictionary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `DOMAIN_DICTIONARY.md`. Don't drift to synonyms the dictionary explicitly avoids.

If the concept you need isn't in the dictionary yet, that's a signal — either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/grill-with-domain`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (example decision) — but worth reopening because…_
