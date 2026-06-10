---
name: codex-dynamic-workflows-enhanced
description: Plan and run general-purpose dynamic AI-agent workflows for complex tasks that need explicit goals, work packets, approval gates, integration, verification, and beginner-friendly guidance. Use for software projects, audits, research, writing, medical education workflows, patient-facing draft workflows, GitHub publishing preparation, multi-track tasks, subagent-style orchestration, or any task where a clear workflow reduces risk and drift.
---

# Codex Dynamic Workflows Enhanced

Use this skill to turn complex work into a supervised workflow with clear success criteria, bounded work packets, approval gates, integration, and verification.

This is a general workflow skill. It can support medical, educational, software, research, and writing scenarios, but it is not limited to any one domain.

## Quick Decision Rule

Use the full workflow when at least two are true:

- The task has independent research, coding, writing, review, QA, or documentation tracks.
- The user is a beginner and needs visible steps.
- The task has safety, privacy, data, production, publication, or reputation risk.
- Verification should be separate from implementation.
- The output could become a reusable process.
- The user asks for a dynamic workflow, swarm, subagents, work packets, or orchestration.

If the task is small, do it directly and say full workflow orchestration is unnecessary.

## Operating Contract

When using this skill:

1. Restate the goal in one or two sentences.
2. Define success criteria before doing broad work.
3. Identify constraints, risks, and approval gates.
4. Split work into packets only when it reduces drift, risk, or confusion.
5. Keep each packet self-contained.
6. Integrate packet outputs into decisions; do not paste raw packet dumps as the final answer.
7. Verify with checks appropriate to the risk.
8. Report completed work, skipped checks, and remaining risks plainly.

## Standard Workflow Plan

Use this concise plan shape:

```text
Goal:
Success criteria:
Audience:
Current context:
Constraints:
Risks:
Approval required:
Workflow artifact path:
Work packets:
Integration policy:
Verification:
Final deliverable:
```

Add domain-specific fields only when needed:

- Medical or patient-facing: privacy, intended use, clinician review.
- Software: touched modules, test scope, rollback risk.
- GitHub publishing: license, secrets check, README readiness, push approval.
- Beginner education: vocabulary, first action, safe stopping points.

## Approval Gates

Ask one clear approval question before:

- deleting, overwriting, mass-renaming, or moving important files
- committing, pushing, force-pushing, tagging, releasing, or creating a public repo
- deploying, publishing, emailing, posting, or submitting forms
- using production APIs, billing systems, private accounts, or credentials
- uploading sensitive files, patient data, private documents, or secrets
- running broad codemods, migrations, or destructive database operations

For detailed examples, read `references/approval-gates.md`.

## Work Packets

Each packet should be independently understandable:

```text
Packet ID:
Objective:
Context:
Inputs:
Ownership:
Do:
Do not:
Expected output:
Verification:
```

Common packets:

- discovery
- requirements clarification
- implementation
- evidence or source review
- documentation
- safety or privacy review
- test and verification
- beginner explanation
- final release readiness

For packet examples, read `references/packet-patterns.md`.

## Scenario Guidance

Read `references/scenario-guides.md` when the task involves:

- a doctor or clinical researcher
- patient-facing educational content
- a beginner trying to publish or use a project
- a GitHub README or open-source release
- a multi-track software change

## Workflow Artifacts

When a task is large enough to benefit from persistent state, create:

```text
.workflow/<slug>/
|-- plan.md
|-- state.json
|-- orchestration.md
|-- packets/
|-- results/
`-- final-report.md
```

Use the bundled script:

```bash
python3 /path/to/codex-dynamic-workflows-enhanced/scripts/new_workflow.py "Task title"
```

## Verification

Choose the narrowest reliable check first, then broaden when risk warrants:

- unit tests, typecheck, lint, or build
- source citation check
- privacy or secrets scan
- browser or UI smoke test
- script dry run
- manual checklist
- final human review

For checklists, read `references/verification.md`.

## Final Response Shape

End with:

```text
Completed:
Evidence:
Verification:
Skipped checks:
Remaining risks:
Next step:
```

Keep the final answer concise and useful. The workflow should make the work clearer, not heavier.
