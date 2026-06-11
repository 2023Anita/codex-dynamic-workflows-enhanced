# Example: Beginner GitHub Project

This example is for a beginner who has a local folder and wants to publish it safely on GitHub.

## Prompt

```text
Use $codex-dynamic-workflows-enhanced to help a beginner prepare a local project for GitHub release.
```

## Why This Fits The Workflow

Publishing to GitHub has visible external effects. Beginners often confuse:

- local files
- staged files
- committed files
- pushed branches
- public repositories

The workflow makes each state explicit and asks before risky actions.

## Workflow

```text
Goal:
Prepare a beginner-friendly GitHub project release plan.

Success criteria:
- README explains the project
- install and first-run steps exist
- example exists
- license exists
- secrets check is complete
- publish actions require approval

Risks:
- publishing secrets
- unclear attribution
- commands that do not match actual files
- confusing local commit with pushed GitHub state
- making a private draft public too early

Work packets:
1. inspect local files
2. draft README
3. check license and attribution
4. run secrets and structure checks
5. explain commit/push/repo creation steps
6. ask before public publishing

Approval gates:
- before git commit
- before git push
- before creating a public repository
- before uploading private files

Verification:
- README commands match files
- no sensitive strings found in tracked files
- ignored files are excluded
- no commit or push without approval
```

## Beginner Explanation

Use this language:

```text
Local means the file is only on your machine.
Committed means Git saved a local snapshot.
Pushed means the snapshot is on GitHub.
Published means other people can access it according to the repository visibility.
```
