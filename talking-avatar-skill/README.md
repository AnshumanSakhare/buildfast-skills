<div align="center">

# 🗣️ Talking Avatar

**Builds a lightweight realtime voice app whose character mouth follows the actual remote audio stream.**

[Install](#install) · [What it builds](#what-it-builds) · [Try it](#try-it) · [Browse BuildFast Skills](../README.md)

</div>

## Install

```bash
npx skills add buildfastwithai/buildfast-skills --skill talking-avatar-skill
```

Add `--global` to make it available across projects.

## At a glance

| Signal | Detail |
|:--|:--|
| **Bring** | A portrait or character description, an initialized compatible app, and an OpenAI API key at runtime |
| **Get** | Character assets, realtime voice UI, audio-driven mouth poses, connection states, and regression tests |
| **Protects** | The pasted key remains ephemeral and session negotiation stays behind a same-origin server route |
| **Verifies** | Asset dimensions, unresolved template tokens, lip-sync source behavior, and worker responses when a build exists |

## What it builds

- A Next.js/vinext talking-avatar interface from a supplied photo or a written character description, or integration into an existing Vite app that already has a safe backend.
- One canonical portrait plus an identity-consistent mouth-pose sprite set.
- Lip sync driven by measured remote audio amplitude rather than a decorative timer.
- A bring-your-own-key OpenAI Realtime flow that keeps credentials out of committed client code.
- Connection, listening, speaking, muted, error, and retry states.
- Focused tests and local asset validation.

The skill can scaffold a new app or integrate the avatar layer into an existing realtime project without replacing working architecture.

## Requirements

- An initialized Next.js or vinext project for the bundled scaffold. Existing Vite apps need a safe backend route for session negotiation.
- Node.js plus `framer-motion` and `@phosphor-icons/react` for the generated web app.
- Python 3 for the included scaffold and asset-validation helpers.
- An OpenAI API key supplied at runtime.
- Image generation for a new character or mouth-pose set. A user-supplied asset set can be used instead.

## Try it

> [!TIP]
> **Start here:** “Use talking-avatar-skill to build a voice companion from this portrait.”

> “Create a warm museum-guide character from a description and add it to my existing Next.js Realtime app.”

> “Fix this avatar so its mouth responds to the assistant's actual audio instead of looping randomly.”

## Included utilities

```bash
python scripts/scaffold_app.py --help
python scripts/validate_avatar_assets.py --help
```

### Local scaffold proof

| Check | Result |
|:--|:--|
| Initialized-project guard | Correctly rejects an empty folder without `package.json` |
| Dry run and scaffold | Exit code **0** against an initialized local project |
| Template replacement | **0** unresolved template tokens |
| Pre-build regression test | **2 passed**, **2 worker-build checks skipped** until a vinext build exists |

## Inside the skill

```text
talking-avatar-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── starter/
├── references/
│   ├── app-contract.md
│   ├── image-pipeline.md
│   └── realtime-lipsync.md
└── scripts/
    ├── scaffold_app.py
    └── validate_avatar_assets.py
```

## Output

You receive a runnable app, the portrait and mouth assets it uses, tests, the commands that were executed, and a clear note about any credential, image, or deployment step still owned by the user.

---

[← Browse all BuildFast Skills](../README.md) · [MIT licensed](../LICENSE) · [View the repository](https://github.com/buildfastwithai/buildfast-skills)
