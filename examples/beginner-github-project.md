# Example: Beginner GitHub Project

Prompt:

```text
Use $codex-dynamic-workflows-enhanced to help a beginner prepare a local project for GitHub release.
```

Workflow:

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

Work packets:
1. inspect local files
2. draft README
3. check license and attribution
4. run secrets and structure checks
5. explain commit/push/repo creation steps

Verification:
- README commands match files
- no sensitive strings found in tracked files
- no commit or push without approval
```
