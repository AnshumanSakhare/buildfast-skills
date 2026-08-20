<div align="center">

# ⚡ BuildFast Skills

**Five production-grade Agent Skills that turn plain-language briefs into finished web experiences.**

Brief in. Working landing page, storefront, interface revamp, talking avatar, or Three.js game out.

[Quickstart](#quickstart) · [Browse the skills](#the-five-skills) · [How it works](#how-a-buildfast-skill-works) · [Contribute](#contributing)

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-5-111111?style=flat-square)](#the-five-skills)
[![Install with npx](https://img.shields.io/badge/install-npx%20skills-CB3837?style=flat-square&logo=npm)](#quickstart)
[![MIT License](https://img.shields.io/badge/license-MIT-0f766e?style=flat-square)](LICENSE)

</div>

---

Most skill repositories are collections of prompts. BuildFast Skills is deliberately smaller and more complete: each package carries the workflow, constraints, references, scripts, or starter files needed to finish a specific job.

There is no framework to adopt and no hosted service to depend on. Install one skill, describe the outcome you want, and let your coding agent work inside the project you already have.

## Quickstart

Browse all five skills and choose interactively:

```bash
npx skills add buildfastwithai/buildfast-skills
```

Install one skill directly:

```bash
npx skills add buildfastwithai/buildfast-skills --skill premium-ui-revamp-skill
```

Add `--global` if you want the skill available across projects. Then restart your agent and ask for the outcome in normal language:

> “Use premium-ui-revamp-skill to make this dashboard feel like a deliberate, credible product without changing its behavior.”

### Start here on Monday

If you already have a working frontend that looks unfinished, start with **[Premium UI Revamp](premium-ui-revamp-skill/)**. It audits structure before decoration, works within the existing stack, implements the changes, and verifies the rendered result.

## The five skills

| Skill | Best for | What it delivers | Requirements |
|:--|:--|:--|:--|
| **[🛒 Crazy Ecommerce Builder](crazy-ecommerce-builder-skill/)** | A memorable, brand-specific storefront | Creative thesis, original image system, working commerce UI, and build verification | A web project; image generation strongly recommended |
| **[🛬 Landing Page Generator](landing-page-generator-skill/)** | Campaign, launch, signup, and lead-capture pages | One production-ready HTML file plus conversion, CTA, and speed audits | Python 3 for bundled audits |
| **[✨ Premium UI Revamp](premium-ui-revamp-skill/)** | A generic, dated, inconsistent, or visibly AI-generated interface | Implemented redesign, design rationale, responsive and accessibility polish | An existing frontend and its normal build tools |
| **[🗣️ Talking Avatar](talking-avatar-skill/)** | Realtime voice chat with a lip-synced character | Next.js/vinext starter, existing-app integration, portrait pipeline, audio-driven mouth poses, and tests | Node.js, Python 3, an OpenAI API key, and image generation |
| **[🎮 Three.js Game Generator](threejs-game-generator-skill/)** | Original 3D browser games and interactive prototypes | A playable Three.js project with game loop, controls, UI states, audio, persistence, and build verification | Node.js, npm, and a WebGL-capable browser |

### Proof, not prompt snippets

The useful detail lives inside each package:

| Package | Included working material |
|:--|:--|
| Crazy Ecommerce Builder | Three art-direction and commerce references |
| Landing Page Generator | A nine-section HTML starter, four focused references, and three executable audit scripts |
| Premium UI Revamp | A premium-pattern library and a scored quality rubric |
| Talking Avatar | Six app/test templates, three implementation references, and two Python utilities |
| Three.js Game Generator | Engine, visual, audio, and genre playbooks built specifically for 3D browser games |

Open any `SKILL.md` and you will see an output contract, decision criteria, verification steps, and explicit boundaries. Supporting files are loaded only when the task needs them.

## Install it your way

### Any agent supported by the `skills` CLI

```bash
# Interactive picker
npx skills add buildfastwithai/buildfast-skills

# One named skill
npx skills add buildfastwithai/buildfast-skills --skill threejs-game-generator-skill

# Every skill, globally
npx skills add buildfastwithai/buildfast-skills --all --global
```

### Claude Code, manual install

Keep the whole selected folder so its references, scripts, and assets remain available:

```bash
git clone --depth 1 https://github.com/buildfastwithai/buildfast-skills.git
mkdir -p ~/.claude/skills
cp -R buildfast-skills/premium-ui-revamp-skill ~/.claude/skills/
```

### Claude.ai

Download or clone the repository, compress the skill folder you want, then upload that folder under **Settings → Capabilities → Skills**.

### Other assistants

Copy the selected `*-skill` folder into your assistant's skills directory. If the assistant has no skill system, attach `SKILL.md` and the references it links to, then use this fallback prompt:

> Read the attached SKILL.md as operating instructions. Preserve my stated scope and permissions, load only the linked references needed for this request, implement the requested outcome, and run the skill's verification steps before handing it back.

## How a BuildFast skill works

1. **Discovery** — the frontmatter description tells the agent exactly when the skill applies.
2. **Decision-making** — `SKILL.md` supplies the workflow, constraints, and quality bar that change how the agent works.
3. **Progressive detail** — references are opened only for the relevant mode, keeping routine tasks lean.
4. **Execution** — templates and scripts make repeatable work deterministic where that matters.
5. **Verification** — every builder skill ends by running the real build, audits, or behavioral checks it claims.

This repository does not add a redundant “registry skill.” The transferable methods are the five installable products themselves.

## Repository structure

```text
buildfast-skills/
├── crazy-ecommerce-builder-skill/
├── landing-page-generator-skill/
├── premium-ui-revamp-skill/
├── talking-avatar-skill/
├── threejs-game-generator-skill/
├── scripts/
│   └── validate_repo.py
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

Each skill folder is self-describing:

```text
skill-name/
├── SKILL.md            # trigger metadata and operating instructions
├── README.md           # human-facing overview and examples
├── agents/             # optional agent UI metadata
├── references/         # detail loaded only when relevant
├── scripts/            # repeatable checks or generators
└── assets/             # starter files copied into the result
```

## Validate locally

The repository has no CI workflow and no deploy configuration. Run the same local checks contributors use:

```bash
python scripts/validate_repo.py
```

For packages with executable helpers, also run their focused checks:

```bash
python -m py_compile landing-page-generator-skill/scripts/*.py
python -m py_compile talking-avatar-skill/scripts/*.py
```

The validator checks skill names, frontmatter, install commands, agent metadata, relative Markdown links, and stale paths from the old repository identity.

## Contributing

Improvements are welcome—especially clearer trigger descriptions, stronger verification, practical references, and scripts that replace repeated guesswork.

Read [CONTRIBUTING.md](CONTRIBUTING.md), keep each pull request focused on one skill or repository concern, and include the local validation output.

## FAQ

<details>
<summary><strong>Do all five skills work in every coding agent?</strong></summary>

The folders use the portable Agent Skills shape: a `SKILL.md` plus optional resources. Installation support and tool availability vary by agent. A skill will fall back to the closest local workflow when a preferred integration is unavailable, but requirements such as Node.js, Python, image generation, or an API key still apply where listed.

</details>

<details>
<summary><strong>Can I install more than one?</strong></summary>

Yes. Run the interactive quickstart, pass several names after `--skill`, or use `--all`.

</details>

<details>
<summary><strong>How do updates work?</strong></summary>

Run the same `npx skills add` command again, or use `npx skills update` for installed skills.

</details>

<details>
<summary><strong>Why only five skills?</strong></summary>

The catalog is intentionally focused on build workflows with enough supporting material to produce and verify a concrete result. Depth beats a long list of interchangeable prompt files.

</details>

## License

[MIT](LICENSE) © 2026 Build Fast with AI.

---

<p align="center">
  Built by <a href="https://www.buildfastwithai.com/"><strong>Build Fast with AI</strong>
  · <a href="https://github.com/buildfastwithai/buildfast-skills/issues/new">Request a skill</a>
  · <a href="https://github.com/buildfastwithai/buildfast-skills/stargazers">Star BuildFast Skills</a>
</p>
