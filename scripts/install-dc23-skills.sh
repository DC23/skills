#!/bin/bash
# Install all DC23 engineering skills into the current project.
# Run from the project root. Requires Node.js (npx).
#
set -e

VERSION="v1.0.0"
BASE="https://github.com/DC23/skills/tree/${VERSION}/skills/engineering"

npx skills add "${BASE}/begin-coding" --agent claude-code --yes
npx skills add "${BASE}/domain-review" --agent claude-code --yes
npx skills add "${BASE}/grill-with-docs" --agent claude-code --yes
npx skills add "${BASE}/project-handoff" --agent claude-code --yes
npx skills add "${BASE}/setup-dc23-skills" --agent claude-code --yes
npx skills add "${BASE}/tdd" --agent claude-code --yes
npx skills add "${BASE}/to-issues" --agent claude-code --yes
npx skills add "${BASE}/triage" --agent claude-code --yes
