# Model Routing

These defaults apply when the current Codex host exposes the named model IDs. They guide role selection; they do not install models or modify Codex runtime configuration.

| Work type | Model | Reasoning effort |
| --- | --- | --- |
| Bounded, low-risk processing and validation | `gpt-6-luna` | `max` |
| Workflow coordination and ordinary execution | `gpt-6-sol` | `medium` |
| Focused high-risk review | `gpt-6-sol` | `high` |

Keep each role's configured reasoning effort unchanged when updating a model generation. Check the model list for the current host before use. If a previous model family has no supported GPT-6 counterpart, use `gpt-6-sol` for balanced general-purpose work rather than inventing a model ID, and retain the original reasoning effort.
