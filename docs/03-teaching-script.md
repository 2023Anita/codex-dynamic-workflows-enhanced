# Teaching Script

This document can be used as a 60-90 minute teaching session for doctors, beginners, or technical teams.

## Learning Goals

By the end, learners should understand:

1. why complex AI work needs staged execution
2. what work packets, approval gates, and verification mean
3. how medical and beginner examples use the same workflow structure
4. how to replicate the workflow for their own project

## Session Outline

| Time | Topic | Asset |
|---:|---|---|
| 0-10 min | Why one-shot AI answers are risky | `assets/workflow-overview.png` |
| 10-25 min | Goal, criteria, packets, gates, verification | `assets/packet-gate-verification-loop.png` |
| 25-40 min | Doctor literature review workflow | `assets/doctor-literature-review.png` |
| 40-55 min | Patient education safety workflow | `assets/patient-education-workflow.png` |
| 55-70 min | Beginner GitHub publishing workflow | `assets/beginner-github-workflow.png` |
| 70-90 min | Adapt one workflow to a learner's own task | `examples/` |

## Figure Talking Points

### Workflow Overview

Use this image to explain the whole project in one sentence:

```text
A complex task becomes a visible chain of goal, criteria, packets, gates, verification, and final report.
```

### Packet Gate Verification Loop

Use this image to explain the repeatable core:

- packets make work smaller
- gates make risk visible
- verification makes output checkable

### Doctor Literature Review

Use this image to explain that AI can support literature review, but the clinician still owns interpretation and final judgment.

### Patient Education

Use this image to explain that patient-facing drafts need plain language, red flags, boundaries, and clinician review.

### Beginner GitHub

Use this image to explain local, committed, pushed, and published states. This is often the moment beginners understand why the agent must ask before publishing.

## Classroom Exercise

Ask learners to choose one task and fill this template:

```text
Goal:

Success criteria:

Risks:

Work packets:
1.
2.
3.

Approval gates:

Verification:
```
