# Approval Gates

Approval gates keep the workflow safe. Ask before doing actions that are hard to undo, externally visible, private, expensive, or risky.

## Local Files

Ask before:

- deleting files or directories
- mass-renaming or moving many files
- overwriting user-created content
- modifying global configuration

Usually safe without extra approval:

- reading files needed for the task
- creating a local draft in the current workspace
- running non-destructive checks

## Git And GitHub

Ask before:

- `git commit`
- `git push`
- force push
- creating branches when the user did not ask for Git work
- opening pull requests
- creating public repositories
- changing repository visibility
- tagging releases

Report states separately:

- local files changed
- staged
- committed
- pushed
- PR opened
- merged
- deployed or published

## External Systems

Ask before:

- sending emails or messages
- posting to social media
- submitting forms
- deploying
- publishing websites
- calling production APIs
- changing billing, user accounts, permissions, or production data

## Sensitive Data

Ask before using:

- credentials, tokens, API keys, or secrets
- private documents
- patient or client data
- company internal data
- browser history or private pages

Default to de-identified examples, local drafts, and read-only inspection.
