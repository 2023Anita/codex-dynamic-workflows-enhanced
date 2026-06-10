# Verification

Verification should match the task risk. Do not run expensive or broad checks when a narrow check proves the change, but do not under-check high-risk work.

## General Checklist

- Success criteria are explicit.
- Work packets map to the success criteria.
- Approval gates were respected.
- Final output separates facts, assumptions, and recommendations.
- Skipped checks are named.
- Remaining risks are visible.

## Code Checklist

- Relevant tests run.
- Typecheck or lint run when available.
- Build run when the change affects packaging or frontend output.
- Manual smoke test run for user-facing flows when practical.
- Unrelated files were not modified.

## Research And Writing Checklist

- Sources are cited or claims are marked unverified.
- Dates are checked for time-sensitive claims.
- Direct quotes are short and necessary.
- Conflicting evidence is not hidden.
- The output matches the requested audience.

## Medical Or Patient-Facing Checklist

- No patient-specific diagnosis, treatment, or triage is provided.
- Patient data or PHI is not copied into unsafe contexts.
- Content is marked educational when appropriate.
- Red flags and clinician review are included when patient-facing.
- Evidence strength and uncertainty are visible.

## GitHub Publishing Checklist

- README explains what the project is and who it is for.
- Install and quick-start steps match the actual files.
- License exists.
- Attribution is included when needed.
- Secrets, tokens, private URLs, and sensitive data are absent.
- Commit, push, repository creation, and publishing actions had explicit approval.
