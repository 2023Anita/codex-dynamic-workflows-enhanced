# Real-World Use Cases

These examples show what this workflow is for. The point is not to make every task slower. The point is to make complex work inspectable, safer, and easier to finish.

## 1. Publishing This Project

Problem:

```text
I want to improve a local workflow skill, explain it clearly, add examples and images, then publish it as a GitHub project.
```

Why dynamic workflow helps:

- The task mixes writing, project design, image generation, repository structure, GitHub publishing, and verification.
- Some actions are safe local edits; others require approval, such as commit, push, and public repository creation.
- The final result must be understandable to people who clone it later.

Useful packets:

```text
1. Define the project positioning.
2. Write README, SKILL.md, examples, and references.
3. Generate and save explanatory images.
4. Verify install commands, image links, and script behavior.
5. Commit, create the GitHub repository, and push after approval.
```

What this prevents:

- Calling a local draft "published" too early.
- Mixing up a forked upstream project with an original rewritten project.
- Publishing without install instructions, examples, or safety boundaries.

## 2. GitHub Project Release For Beginners

Problem:

```text
A beginner has a local project and wants to put it on GitHub, but does not know what is safe to publish.
```

Why dynamic workflow helps:

- Beginners often need the agent to explain each step.
- Publishing is externally visible and should not happen silently.
- A secrets check and README check should happen before push.

Useful packets:

```text
1. Inspect the local folder.
2. Explain what will be public.
3. Prepare README, license, and examples.
4. Check for secrets, private data, and generated junk files.
5. Ask before commit, repository creation, and push.
```

Expected output:

- a ready README
- a small publish checklist
- clear distinction between local files, commit, push, and public GitHub URL

## 3. Doctor Literature Review Workflow

Problem:

```text
A physician wants to prepare a teaching session or review article and needs help structuring the research workflow.
```

Why dynamic workflow helps:

- Medical content needs evidence discipline.
- Search, appraisal, drafting, citation checking, and safety review are different tasks.
- The AI output should support clinician judgment, not replace it.

Useful packets:

```text
1. Define the clinical question and audience.
2. Build a search strategy.
3. Separate guidelines, reviews, trials, observational studies, and expert opinion.
4. Draft the teaching outline.
5. Verify claims and mark uncertainty.
```

Expected output:

- search strategy
- evidence map
- teaching outline
- citation verification checklist
- clear note that clinician review is required

## 4. Patient-Facing Education Draft

Problem:

```text
A team wants to draft patient education content, such as a plain-language explanation of sleep apnea screening.
```

Why dynamic workflow helps:

- Patient-facing content must avoid patient-specific diagnosis or treatment advice.
- Red flags and escalation language need special attention.
- A clinician should review the final draft before use.

Useful packets:

```text
1. Define audience and reading level.
2. Draft plain-language content.
3. Review for medical advice boundaries.
4. Add red flags and when-to-seek-care language.
5. Run readability and clinician-review checklist.
```

Expected output:

- educational draft
- safety limitations
- red-flag checklist
- clinician review checklist

## 5. Repository Audit Or Refactor

Problem:

```text
An agent needs to inspect a codebase, find risk, make a small change, and verify it without damaging unrelated work.
```

Why dynamic workflow helps:

- Discovery and implementation should be separate.
- The agent must avoid reverting unrelated changes.
- Tests and final verification should match the blast radius.

Useful packets:

```text
1. Read README, config, and entry files.
2. Identify the smallest safe change.
3. Implement within the touched module only.
4. Run targeted tests.
5. Summarize changed files, verification, and residual risk.
```

Expected output:

- scoped implementation
- focused tests or checks
- concise final report

## 6. Multi-Track Research Plus Writing

Problem:

```text
The user wants research, synthesis, examples, and a publishable article or guide.
```

Why dynamic workflow helps:

- Source gathering, claim checking, writing, and final editing can drift if done as one blob.
- The final answer needs to show evidence status.

Useful packets:

```text
1. Scope the audience and thesis.
2. Gather sources.
3. Build a claim map.
4. Draft the article.
5. Verify source support and edit for clarity.
```

Expected output:

- outline
- source-backed draft
- unsupported-claim list
- final version with caveats

## When Not To Use It

Skip the full workflow for:

- one-line command questions
- small edits with obvious scope
- quick explanations
- tasks where the user explicitly wants only an answer, not orchestration

Use the workflow when clarity, safety, verification, or multi-step execution matters.

## 7. Physician Teaching Session

Problem:

```text
A physician wants to prepare a teaching session from recent evidence, but needs the AI to keep search, appraisal, slides, and citation checks separate.
```

Why dynamic workflow helps:

- Clinical questions need scope control.
- Teaching messages should not overstate certainty.
- Citation checks and clinician review should happen before sharing.

Useful packets:

```text
1. Define the audience and clinical question.
2. Build a search and source-selection plan.
3. Create an evidence table.
4. Draft the teaching outline.
5. Verify citations and mark uncertainty.
6. Confirm clinician review before release.
```

## 8. Hospital Research Secretary Workflow

Problem:

```text
A hospital research office needs repeatable workflows for abstracts, teaching material, evidence summaries, and GitHub project packaging.
```

Why dynamic workflow helps:

- It creates a standard path for intake, packet assignment, review, and final reporting.
- It separates administrative formatting from scientific claims.
- It makes approval gates visible before external submission.

Useful packets:

```text
1. Intake project goal and target audience.
2. Identify required documents and data boundaries.
3. Draft structured outputs.
4. Verify citations, formatting, and missing fields.
5. Prepare final package for human sign-off.
```

## 9. AI Training Course

Problem:

```text
An instructor wants to teach doctors and beginners how to use AI agents safely for research, documentation, and GitHub publishing.
```

Why dynamic workflow helps:

- Learners can see the process instead of only the final answer.
- The same vocabulary works across medical, writing, and coding scenarios.
- The examples can become classroom exercises.

Useful packets:

```text
1. Explain goal and success criteria.
2. Demonstrate packet planning.
3. Show approval gates.
4. Run verification.
5. Ask learners to adapt a template.
```

## 10. Open-Source Project Release

Problem:

```text
A project owner wants to turn a local tool into a public GitHub project with README, examples, images, and safety notes.
```

Why dynamic workflow helps:

- Public release needs attribution, license, documentation, and link checks.
- Generated images and docs need to be saved into the repository, not left in a cache folder.
- Commit and push should happen only after approval.

Useful packets:

```text
1. Inspect project structure.
2. Write README and examples.
3. Generate and save images.
4. Check links and ignored files.
5. Commit and push after explicit approval.
```
