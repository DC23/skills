#!/bin/bash
# Install all DC23 engineering skills into the current project.
# Run from the project root. Requires Node.js (npx).
#
set -e

npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/begin-coding --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/domain-review --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/grill-with-docs --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/project-handoff --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/setup-dc23-skills --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/tdd --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/to-issues --agent claude-code --yes
npx skills add https://github.com/DC23/skills/tree/v1.0.0/skills/engineering/triage --agent claude-code --yes
