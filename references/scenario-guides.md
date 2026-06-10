# Scenario Guides

These guides show how the same general workflow adapts to different audiences. Do not turn the workflow into a domain-only process; add only the fields needed for the scenario.

## Doctor Or Clinical Researcher

Use when the user is preparing medical education, literature review, research planning, protocol drafting, or healthcare AI documentation.

Add fields:

```text
Clinical context:
Intended use:
Audience:
Data sensitivity:
Evidence standard:
Human review:
```

Example:

```text
Goal: Plan a literature review workflow for perioperative anemia teaching.
Success criteria: Search strategy, evidence table, teaching outline, citation verification checklist.
Risks: Outdated guidelines, overgeneralized clinical claims, missing clinician review.
Packets: scope, search strategy, evidence appraisal, teaching outline, citation check.
Verification: guideline dates checked, claims mapped to sources, clinician review marked required.
```

## Patient-Facing Draft

Use when drafting content that patients may read. Keep it educational and non-patient-specific.

Add fields:

```text
Audience reading level:
Not medical advice statement:
Red flags:
Clinician review:
```

Example:

```text
Goal: Draft a workflow for patient education material about sleep apnea screening.
Success criteria: Plain-language draft, red flags, when-to-seek-care language, clinician review checklist.
Risks: Giving patient-specific advice, false reassurance, missing urgent symptoms.
Packets: audience, plain-language draft, safety review, readability review, clinician checklist.
Verification: no diagnosis or treatment instructions, red flags present, limitations visible.
```

## Beginner GitHub Project

Use when a beginner wants to publish, fork, install, or understand a project.

Add fields:

```text
Beginner goal:
First safe step:
Terms to explain:
Public actions requiring approval:
```

Example:

```text
Goal: Help a beginner prepare a GitHub project for public release.
Success criteria: README, install steps, example, license, secrets check, publish plan.
Risks: accidentally publishing secrets, confusing local commit with pushed repo, unclear install path.
Packets: inspect files, README draft, license and attribution, secrets check, publishing guide.
Verification: no secrets found in tracked files, README commands match files, push requires approval.
```

## Software Change

Use for implementation, refactor, tests, migrations, or bug fixes.

Add fields:

```text
Touched modules:
Behavioral contract:
Rollback risk:
Test scope:
```

Example:

```text
Goal: Refactor authentication middleware without changing behavior.
Success criteria: Existing tests pass, new focused tests cover edge cases, API behavior unchanged.
Risks: session regression, security bug, unrelated cleanup.
Packets: discovery, implementation, tests, security review, final verification.
Verification: unit tests, typecheck, targeted route smoke test.
```

## Public Writing Or README

Use for documentation, course pages, tutorials, and release materials.

Add fields:

```text
Audience:
Promise:
Proof:
Install or first-use path:
Attribution:
```

Example:

```text
Goal: Improve a README so users can clone and run the project.
Success criteria: clear positioning, install command, first example, limitations, license.
Risks: overstating originality, missing attribution, commands that do not work.
Packets: audience framing, quick start, examples, safety/limitations, verification.
Verification: commands checked or marked untested, links valid, attribution present.
```
