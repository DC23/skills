# Issue tracker: GitHub

Issues and PRDs for this repo live as GitHub issues. Use the `gh` CLI for all operations.

## Conventions

- **Create an issue**: `gh issue create --title "..." --body "..."`. Use a heredoc for multi-line bodies.
- **Read an issue**: `gh issue view <number> --comments`, filtering comments by `jq` and also fetching labels.
- **List issues**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` with appropriate `--label` and `--state` filters.
- **Comment on an issue**: `gh issue comment <number> --body "..."`
- **Apply / remove labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

Infer the repo from `git remote -v` — `gh` does this automatically when run inside a clone.

## When a skill says "publish to the issue tracker"

Create a GitHub issue.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --comments`.

## Issue relationships

GitHub issue relationships (sub-issues and blocked-by) are managed via the GraphQL API. Use `gh api graphql` with the mutations below.

**Get node IDs** (required before any mutation):

```bash
gh api graphql -f query='{ repository(owner: "OWNER", name: "REPO") { issue(number: N) { id } } }'
```

**Sub-issue relationships:**

```bash
# Make CHILD a sub-issue of PARENT
gh api graphql -f query='mutation { addSubIssue(input: {issueId: "PARENT_ID", subIssueId: "CHILD_ID"}) { issue { number } subIssue { number } } }'

# Remove CHILD from PARENT's sub-issues
gh api graphql -f query='mutation { removeSubIssue(input: {issueId: "PARENT_ID", subIssueId: "CHILD_ID"}) { clientMutationId } }'
```

**Blocked-by relationships:**

```bash
# Mark ISSUE as blocked by BLOCKER
gh api graphql -f query='mutation { addBlockedBy(input: {issueId: "ISSUE_ID", blockingIssueId: "BLOCKER_ID"}) { clientMutationId } }'

# Remove blocked-by relationship
gh api graphql -f query='mutation { removeBlockedBy(input: {issueId: "ISSUE_ID", blockingIssueId: "BLOCKER_ID"}) { clientMutationId } }'
```

Skills that create batches of related issues (e.g. epic breakdowns via `to-issues`) should use these mutations to wire up parent and dependency relationships automatically after creating the issues.
