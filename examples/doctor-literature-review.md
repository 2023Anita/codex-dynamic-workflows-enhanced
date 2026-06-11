# Example: Doctor Literature Review

This example is for a physician preparing a teaching session, journal club, or review outline. The workflow helps structure the work, but it does not replace clinical judgment or current guidelines.

## Prompt

```text
Use $codex-dynamic-workflows-enhanced to plan a literature review workflow for a physician preparing a teaching session on perioperative anemia.
```

## Why This Fits The Workflow

Medical literature work has multiple risk points:

- the clinical question may be too broad
- evidence may be outdated
- guidelines may differ by region or specialty
- citations may be incomplete
- the final teaching message may overstate certainty

The workflow keeps these risks visible.

## Workflow

```text
Goal:
Create a literature review workflow for a physician-led teaching session.

Success criteria:
- PICO-style question
- search strategy
- evidence table
- teaching outline
- citation verification checklist
- clinician review note

Risks:
- outdated guidelines
- overstated clinical claims
- missing clinician review
- unclear distinction between evidence and opinion

Work packets:
1. scope clinical question and audience
2. design search strategy
3. appraise evidence levels
4. draft teaching outline
5. verify citations and safety language
6. prepare clinician-review checklist

Approval gates:
- confirm PICO question before searching
- confirm source inclusion criteria before synthesis
- confirm final teaching claims before sharing

Verification:
- source dates checked
- claims mapped to sources
- final output marked for clinician review
- uncertainty and limitations visible
```

## What Requires Human Confirmation

- The clinical question.
- Which guidelines or evidence sources are acceptable.
- Any final clinical interpretation.
- Any teaching material shared with learners or patients.

## Boundary Statement

Use this wording in final outputs:

```text
This material is for educational support and requires clinician review. It does not replace current guidelines, local policy, or professional judgment.
```
