<div align="center">

# 🎮 Three.js Game Generator

**Turns a game brief into an original, playable 3D browser game with a real loop, controls, UI states, audio, and verification.**

[Install](#install) · [What it builds](#what-it-builds) · [Try it](#try-it) · [Browse BuildFast Skills](../README.md)

</div>

## Install

```bash
npx skills add buildfastwithai/buildfast-skills --skill threejs-game-generator-skill
```

Add `--global` to make it available across projects.

## What it builds

- A maintainable Three.js project in the user's existing stack, or a lean Vite project for a new game.
- One complete core loop before secondary systems are added.
- Responsive keyboard, pointer, and touch controls appropriate to the genre.
- DOM-based menus and HUD, pause/restart/game-over states, audio activation, and local persistence.
- Original visual and mechanical direction even when the brief references a familiar game.
- A successful production build plus browser and playability checks.

## Requirements

- Node.js and npm.
- A browser with WebGL support.
- Licensed or original assets when the game uses external models, textures, fonts, or audio.

## Try it

> “Use threejs-game-generator-skill to build a low-poly delivery game where the city folds upward as the timer runs out.”

> “Turn this Three.js scene into a complete three-minute arcade loop with mobile controls and a restart flow.”

> “Prototype an original third-person stealth game inspired by diorama theater sets—do not copy an existing title's characters or levels.”

## Inside the skill

```text
threejs-game-generator-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── audio-recipes.md
    ├── engine-patterns.md
    ├── genres.md
    └── visuals.md
```

The four references separate engine architecture, art direction, sound, and genre-specific decisions. The agent reads only the ones the current game needs.

## Output

You receive the runnable project, control map, asset and licensing notes, build/test results, and a concise list of intentionally deferred features. The first delivery must be a small finished game, not a large unfinished framework.

---

[← Browse all BuildFast Skills](../README.md) · [View the repository](https://github.com/buildfastwithai/buildfast-skills)
