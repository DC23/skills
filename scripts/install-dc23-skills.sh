#!/bin/bash
# Install all DC23 engineering skills into the current project.
# Run from the project root. Requires Node.js (npx).
#
# Note: URLs pin to the main branch and will always pull the latest revision.
# For a reproducible install, replace 'main' with a commit SHA or tag.
set -e

npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/begin-coding --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/domain-review --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/grill-with-docs --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/project-handoff --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/setup-dc23-skills --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/tdd --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/to-issues --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/main/skills/engineering/triage --agent claude-code --yes
