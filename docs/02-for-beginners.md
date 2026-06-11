# For Beginners

This workflow is for people who want the AI agent to show the path instead of hiding all work inside one answer.

## Key Terms

**Goal**  
What you want to finish.

**Success criteria**  
How you know the work is done.

**Work packet**  
A small piece of the task that can be checked.

**Approval gate**  
A point where the agent must stop and ask before doing something risky.

**Verification**  
A check that proves the result is more trustworthy.

**Final report**  
A short summary of what happened, what passed checks, and what remains uncertain.

## Example

Instead of saying:

```text
Make my project good and put it on GitHub.
```

Use:

```text
Use $codex-dynamic-workflows-enhanced to help me prepare this project for GitHub. Explain each step before risky actions.
```

The agent should then separate:

- reading local files
- writing README
- checking for secrets
- staging files
- committing
- pushing
- publishing

Commit and push should not happen without your explicit confirmation.
