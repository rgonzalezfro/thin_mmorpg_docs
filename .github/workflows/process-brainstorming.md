---
name: Process brainstorming

on:
  push:
    branches:
      - main
    paths:
      - "00_Brainstorming/**/*.md"
  workflow_dispatch:
    inputs:
      base_sha:
        description: "Base commit to compare (required for manual runs)"
        required: false
        type: string
      head_sha:
        description: "Head commit to compare (defaults to the selected ref)"
        required: false
        type: string
  permissions:
    contents: read
  steps:
    - name: Build brainstorming change manifest
      id: change_manifest
      uses: actions/github-script@v9
      env:
        BASE_SHA: ${{ github.event.inputs.base_sha || github.event.before }}
        HEAD_SHA: ${{ github.event.inputs.head_sha || github.sha }}
      with:
        github-token: ${{ github.token }}
        script: |
          const base = process.env.BASE_SHA;
          const head = process.env.HEAD_SHA;
          const zeroSha = /^0+$/;

          if (!base || zeroSha.test(base)) {
            core.setFailed('A valid base SHA is required to build the brainstorming change manifest.');
            return;
          }

          const comparison = await github.rest.repos.compareCommits({
            owner: context.repo.owner,
            repo: context.repo.repo,
            base,
            head,
          });

          const files = (comparison.data.files || [])
            .filter((file) =>
              file.filename.startsWith('00_Brainstorming/') &&
              file.filename.toLowerCase().endsWith('.md')
            )
            .map((file) => ({
              path: file.filename,
              status: file.status,
              additions: file.additions,
              deletions: file.deletions,
              patch: file.patch || '[patch unavailable: inspect only this listed file if needed]',
            }));

          core.setOutput('change_manifest', JSON.stringify({
            base_sha: base,
            head_sha: head,
            files,
            instruction: files.length
              ? 'Process only the listed files and added/modified lines in their patches.'
              : 'No changed brainstorming Markdown files were found.',
          }));

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

jobs:
  pre-activation:
    outputs:
      change_manifest: ${{ steps.change_manifest.outputs.change_manifest }}

---

# Process New Brainstorming

Process the new or modified Markdown files under `00_Brainstorming/` and
propose the smallest coherent documentation update in a draft pull request.

The deterministic change manifest generated before this agent run is:

```json
${{ needs.pre_activation.outputs.change_manifest }}
```

This manifest is the only brainstorming input for this run. Process only the
listed files and the added or modified lines shown in their patches. Do not
scan, search, or read unrelated files under `00_Brainstorming/`. You may read
existing formal documents outside that folder for context when they are
related to the listed changes.

## Required context

Read `AGENTS.md` first. Then read the change manifest above, the relevant
category `_INDEX.md`, and existing documents that cover related concepts.
Preserve the original brainstorming files exactly as they are.

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

## Output contract

The workflow must never finish with `noop` after modifying repository files.

- Run `git status --short` and `git diff --stat` before finishing.
- If you create, update, rename, or delete any allowed documentation file, you
  MUST call `create_pull_request` with the resulting changes.
- `noop` is allowed only when the working tree has no documentation changes to
  submit.
- Do not treat a successful local `git diff` as persistence. Changes are
  discarded with the runner unless `create_pull_request` is called.
- If changes exist but the pull-request output cannot be called, report the
  failure instead of calling `noop`.

The result must be a reviewable draft PR whenever any allowed documentation file
was changed. Do not push directly to `main` and do not merge the PR.
