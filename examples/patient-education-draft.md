# Example: Patient Education Draft

This example is for drafting patient-facing educational material. The workflow keeps safety boundaries visible and requires clinician review before use.

## Prompt

```text
Use $codex-dynamic-workflows-enhanced to create a workflow for drafting patient education material about sleep apnea screening.
```

## Why This Fits The Workflow

Patient-facing content can accidentally become personalized medical advice. A dynamic workflow separates plain-language drafting from safety review.

## Workflow

```text
Goal:
Draft safe educational material for patients.

Success criteria:
- plain-language draft
- clear limitations
- red flags and when-to-seek-care language
- clinician review checklist
- readability review

Risks:
- accidentally giving patient-specific advice
- false reassurance
- missing urgent symptoms
- unclear escalation language
- content used before clinician review

Work packets:
1. define audience and reading level
2. draft plain-language content
3. safety review for advice boundaries
4. add red flags and escalation language
5. readability review
6. clinician review checklist

Approval gates:
- confirm audience and reading level before drafting
- confirm red flags before finalizing
- require clinician approval before use

Verification:
- no diagnosis or treatment instruction
- red flags present
- limitations visible
- final output marked as educational draft
```

## Red Flag Checklist

The workflow should ask whether the topic needs:

- urgent symptoms
- when-to-seek-care instructions
- emergency care language
- local contact or clinic pathway
- explicit note that the material is not a diagnosis

## Boundary Statement

Use this wording in final outputs:

```text
This is general educational information. It is not a diagnosis or treatment plan. Patients should consult a qualified clinician for personal medical advice.
```
