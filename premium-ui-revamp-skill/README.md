<div align="center">

# ✨ Premium UI Revamp

**Turns a generic or visibly AI-generated interface into a deliberate product while preserving its behavior and stack.**

[Install](#install) · [What it changes](#what-it-changes) · [Try it](#try-it) · [Browse BuildFast Skills](../README.md)

</div>

## Install

```bash
npx skills add buildfastwithai/buildfast-skills --skill premium-ui-revamp-skill
```

Add `--global` to make it available across projects.

## At a glance

| Signal | Detail |
|:--|:--|
| **Bring** | An existing frontend, the target route or screen, and any product or brand constraints |
| **Get** | Implemented redesign, compact design brief, rationale, responsive states, and verification results |
| **Preserves** | Framework, routes, content, data flow, controls, and working behavior |
| **Verifies** | Production build, keyboard/focus behavior, responsiveness, reduced motion, and the included quality rubric |

## What it changes

The skill audits the actual rendered surface, writes a compact design brief, and fixes problems in the order that matters:

1. **Structural** — hierarchy, content order, information architecture, density, and responsive composition.
2. **Systemic** — typography, spacing, color, radii, elevation, components, and interaction states.
3. **Polish** — optical alignment, icons, borders, microcopy, transitions, and finishing detail.

It works inside HTML/CSS/JavaScript, React, Vue, Svelte, Next.js, and similar frontend projects. It does not replace the framework, rewrite unrelated components, or invent a new brand just to make redesign easier.

## Try it

> [!TIP]
> **Start here:** “Use premium-ui-revamp-skill to make this dashboard feel precise and trustworthy. Preserve every workflow.”

> “Audit this marketing page at desktop and mobile sizes, then implement the highest-impact fixes.”

> “Remove the generic AI design tells from this React app without turning it into another bland minimal site.”

## What it verifies

| Surface | Done means |
|:--|:--|
| **Behavior** | Existing routes, data flow, controls, and content still work |
| **Access** | Keyboard, focus-visible, reduced-motion, and responsive states remain usable |
| **System** | Shared tokens and repeated components stay coherent |
| **Build** | The production build succeeds |
| **Finish** | The rendered result passes the included quality rubric |

## Inside the skill

```text
premium-ui-revamp-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── premium-patterns.md
    └── quality-rubric.md
```

## Output

You receive implemented changes in the existing stack, the design rationale behind them, validation results, and any remaining limitation that needs product or brand input.

---

[← Browse all BuildFast Skills](../README.md) · [MIT licensed](../LICENSE) · [View the repository](https://github.com/buildfastwithai/buildfast-skills)
