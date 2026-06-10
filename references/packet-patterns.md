# Packet Patterns

Use packets when separate passes reduce risk, speed up work, or make review easier.

## Discovery Packet

```text
Packet ID: discovery
Objective: Understand the current project, files, sources, or constraints.
Do: Read only the smallest useful context.
Do not: Modify files or assume architecture from filenames alone.
Expected output: Key facts, relevant files, uncertainty, suggested next packets.
Verification: Cite files, commands, or sources inspected.
```

## Implementation Packet

```text
Packet ID: implementation
Objective: Make the narrowest change that satisfies the success criteria.
Do: Follow local patterns and keep edits scoped.
Do not: Refactor unrelated code or revert other people's changes.
Expected output: Files changed and why.
Verification: Run targeted checks.
```

## Evidence Review Packet

```text
Packet ID: evidence-review
Objective: Gather and assess sources for claims.
Do: Separate strong evidence, weak evidence, and speculation.
Do not: Invent citations or hide conflicting evidence.
Expected output: Evidence table or claim map.
Verification: Source links, dates, and claim-to-source mapping.
```

## Beginner Explanation Packet

```text
Packet ID: beginner-guide
Objective: Convert the workflow into clear steps for a beginner.
Do: Explain first action, expected output, and safe stopping points.
Do not: Hide risky actions behind jargon.
Expected output: Plain-language guide with commands or examples.
Verification: Check that each step is actionable.
```

## Safety Review Packet

```text
Packet ID: safety-review
Objective: Find privacy, security, clinical, legal, publication, or operational risks.
Do: Identify approval gates and required human review.
Do not: Treat drafts as final advice or approved releases.
Expected output: Risk list and mitigations.
Verification: Checklist matched to the scenario.
```

## Final Verification Packet

```text
Packet ID: final-verification
Objective: Prove the result meets the success criteria.
Do: Run checks appropriate to the blast radius.
Do not: Claim completion when key checks were skipped.
Expected output: Passed checks, skipped checks, residual risk.
Verification: Command output, source evidence, or manual checklist.
```
