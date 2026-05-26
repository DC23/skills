---
name: review-plugin
description: Review a third-party Claude Code plugin or skill for security, intrusiveness, and trustworthiness. Use when the user provides a GitHub URL or name of a plugin or skill they are considering installing.
disable-model-invocation: true
---

Review the Claude Code plugin or skill at: $ARGUMENTS

Fetch the repository (README, SKILL.md, any files under `hooks/`, `skills/`, `mcp/`, or plugin manifests). Then produce a structured report:

## Identity
- Name, author, stated purpose
- Install method (marketplace, curl|bash, manual, etc.)

## Components
List every component it installs and what it does:
- **Skills** — commands added, auto-invocation triggers
- **Hooks** — which lifecycle events (SessionStart, UserPromptSubmit, etc.), what they inject or modify
- **MCP servers** — what they connect to, how they're launched (npx -y, local binary, etc.)
- **Agents** — any custom subagents
- **File footprint** — does it write into repos, other tool configs, or system paths?

## Risk Flags
Assess each of the following and note if present:
- Silent context injection (hooks that modify Claude's context without user action)
- Per-prompt hooks (runs on every message)
- MCP middleware (sits between Claude and other MCP servers)
- Network calls (fetches remote content at runtime, live-updating behavior)
- Broad installer footprint (modifies configs for other tools or writes into repos)
- Unverified package execution (e.g. `npx -y` without pinned version)
- Privilege escalation or filesystem access beyond the project
- Cross-repo dependencies (if a subdirectory URL was provided, check whether the skill references shared utilities, scripts, or resources elsewhere in the parent repo that wouldn't be visible from the scoped URL — flag these if found)

## Verdict
A plain-language summary: is this safe to install, worth the tradeoff, or best avoided — and why.
