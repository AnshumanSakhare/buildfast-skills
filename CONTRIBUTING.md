# Contributing to BuildFast Skills

BuildFast Skills favors a small number of complete, testable workflows over a large catalog of generic prompt files.

## What makes a useful contribution

- Tighten a trigger description so the skill activates for the right requests.
- Add decision-making guidance that materially improves the result.
- Replace repeated, error-prone work with a focused script or starter asset.
- Add a reference that is needed for one real operating mode.
- Strengthen build, behavioral, accessibility, or output verification.
- Fix stale paths, misleading requirements, or broken examples.

New skills should produce a concrete outcome and contain enough method for another assistant to reproduce it. A new folder must use lowercase kebab-case, end in `-skill`, and keep the frontmatter `name` identical to the folder name.

## Package shape

```text
my-skill/
├── SKILL.md             required
├── README.md            required in this public catalog
├── agents/openai.yaml   optional UI metadata
├── references/          optional, mode-specific guidance
├── scripts/             optional, repeatable automation
└── assets/              optional, files copied into outputs
```

Keep the entrypoint focused. Put substantial conditional detail in references, link each reference from `SKILL.md), and explain when to read it. Do not add placeholder directories or duplicate the same instructions across files.

If you add `agents/openai.yaml`, its `default_prompt` must name the exact skill, including the `-skill` suffix.

## Before opening a pull request

Run every changed executable helper and the real build or output check the skill promises. Include:

- the user request or scenario you tested;
- the command(s) you ran;
- the observable result;
- any requirement or limitation the README should disclose.

Keep the pull request focused on one skill or one repository-level concern. Do not add CI workflows, deploy configuration, generated dependency folders, secrets, or unrelated formatting changes.

By contributing, you agree that your contribution is licensed under the repository's [MIT License](LICENSE).
