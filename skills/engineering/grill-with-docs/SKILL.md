---
name: grill-with-docs
description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (DOMAIN_DICTIONARY.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against the project's established language and documented decisions.
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Domain awareness

During codebase exploration, also look for existing documentation:

- `docs/DOMAIN_DICTIONARY.md` — domain model, entity relationships, terminology and the *why* behind naming choices
- `docs/adr/` — architectural decisions; read ADRs that touch the area being discussed

Create files lazily — only when you have something to write. If `docs/adr/` does not exist, create it when the first ADR is needed.

Format rules for both files are in `docs/agents/domain.md` and `docs/agents/adr.md`.

## During the session

### Challenge against the dictionary

When the user uses a term that conflicts with the existing language in `docs/DOMAIN_DICTIONARY.md`, call it out immediately. "Your dictionary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Stage resolved terms

When a term is resolved, identify whether it qualifies as Ubiquitous Language: domain entities, relationships, and named processes that domain experts and developers would use consistently — not implementation details or incidental vocabulary. Be conservative — fewer, well-chosen candidates are more useful than a long list of noise.

For each qualifying term, append a candidate entry to `docs/DOMAIN_CANDIDATES.md` (creating the file if absent) using the format in `docs/agents/domain.md`. Do not write directly to `docs/DOMAIN_DICTIONARY.md` — terms are promoted into the dictionary only via the `domain-review` skill.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in `docs/agents/adr.md`.
