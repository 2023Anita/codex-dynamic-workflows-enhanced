# Replicate A Workflow

Use this repository as a template for your own repeatable workflow.

## Step 1: Pick A Scenario

Choose one existing example:

- `examples/doctor-literature-review.md`
- `examples/patient-education-draft.md`
- `examples/beginner-github-project.md`

## Step 2: Copy The Structure

Keep these sections:

```text
Goal
Success criteria
Risks
Work packets
Approval gates
Verification
Final report
```

## Step 3: Replace The Content

Change the clinical topic, audience, project type, repository, or data source.

Do not remove approval gates if the workflow includes:

- medical content
- private data
- publication
- commit or push
- production deployment
- irreversible file operations

## Step 4: Add Verification

Verification should match the risk:

- Markdown link checks for docs
- tests for code
- citation checks for research
- clinician review for medical content
- secret scans for GitHub publishing

## Step 5: Run The Workflow

Use this prompt:

```text
Use $codex-dynamic-workflows-enhanced to plan and run this workflow step by step. Stop before risky actions and show verification evidence.
```
