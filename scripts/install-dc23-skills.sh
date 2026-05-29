#!/bin/bash
# Install all DC23 engineering skills into the current project.
# Run from the project root. Requires Node.js (npx).
#
# Usage: install-dc23-skills.sh [--agent <name>] [--agent <name> ...]
#   --agent <name>    Target agent (may be repeated). Defaults to claude-code.
#   --agent DEFAULT   Use npx skills' own default (no --agent flag passed).
#
set -e

VERSION="v1.1.1"
BASE="https://github.com/DC23/skills/tree/${VERSION}/skills/engineering"

AGENTS=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --agent) AGENTS+=("$2"); shift 2 ;;
        *) echo "Usage: $0 [--agent <name>] ..." >&2; exit 1 ;;
    esac
done

AGENT_FLAGS=()
if [[ ${#AGENTS[@]} -eq 0 ]]; then
    AGENT_FLAGS=(--agent claude-code)
elif [[ ${#AGENTS[@]} -eq 1 && "${AGENTS[0]}" == "DEFAULT" ]]; then
    AGENT_FLAGS=()
else
    for a in "${AGENTS[@]}"; do
        AGENT_FLAGS+=(--agent "$a")
    done
fi

SKILLS=(
    begin-coding
    domain-review
    grill-with-docs
    project-handoff
    setup-dc23-skills
    tdd
    to-issues
    triage
)

for skill in "${SKILLS[@]}"; do
    npx skills add "${BASE}/${skill}" "${AGENT_FLAGS[@]}" --yes
done
