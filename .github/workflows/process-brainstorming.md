---
name: Process brainstorming

on:
  push:
    branches:
      - main
    paths:
      - "00_Brainstorming/**/*.md"
  workflow_dispatch:

permissions:
  contents: read
  pull-requests: read
  copilot-requests: write

engine: copilot
# Change this value to another model available to your Copilot plan.
model: gpt-5-mini
max-turns: 30
timeout-minutes: 20

safe-outputs:
  create-pull-request:
    title-prefix: "[docs] "
    branch-prefix: "automation/brainstorming-"
    draft: true
    labels:
      - documentation
      - brainstorming
---

# Process New Brainstorming

Process the new or modified Markdown files under `00_Brainstorming/` and
propose the smallest coherent documentation update in a draft pull request.

## Required context

Read `AGENTS.md` first. Then read the complete changed brainstorming files,
the relevant category `_INDEX.md`, and existing documents that cover related
concepts. Preserve the original brainstorming files exactly as they are.

## Allowed changes

You may create or update documents only in:

- `01_Core_Systems/`
- `02_Content_Entities/`
- `03_Tech_Specs/`
- `04_Game_Loops/`
- `05_Tasks_Roadmap/`

You may update the relevant `_INDEX.md` files when adding or moving formal
documents. Do not modify `00_Brainstorming/`, `AGENTS.md`, `README.md`,
`.github/`, `.mkdocs/`, `client/`, or `server/`.

## Documentation rules

- Keep every proposal in `status: draft`.
- Never create or change a document to `status: approved` or `deprecated`.
- Use the existing frontmatter schema required by `AGENTS.md`.
- Include `source_brainstorm: "00_Brainstorming/<source-file>.md"`.
- Reuse existing terminology and update an existing document instead of creating duplicates.
- Add explicit `Preguntas Pendientes para el Equipo` when the source leaves a decision unresolved.
- Add dependencies only when the relationship is clear from the existing documentation.
- Do not invent numbers, formulas, rules, names, requirements, or technical decisions.
- Keep the original source context and do not rewrite brainstorming into a decision.

## Review requirements

Before proposing the pull request, check frontmatter, category placement,
source references, duplicate concepts, index entries, WikiLinks, and the diff.
The result must be a reviewable draft PR. Do not push directly to `main` and do
not merge the PR.
