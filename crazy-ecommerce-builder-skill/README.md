<div align="center">

# 🛒 Crazy Ecommerce Builder

**Turns a short product brief into an unconventional storefront with a coherent creative thesis—not random effects.**

[Install](#install) · [The method](#the-method) · [Try it](#try-it) · [Browse BuildFast Skills](../README.md)

</div>

## Install

```bash
npx skills add buildfastwithai/buildfast-skills --skill crazy-ecommerce-builder-skill
```

Add `--global` to make it available across projects.

## At a glance

| Signal | Detail |
|:--|:--|
| **Bring** | A product or company brief, catalog details, brand constraints, and any existing web project |
| **Get** | A creative thesis, coherent image world, responsive storefront, cart interactions, and build results |
| **Verifies** | Product clarity, cart usability, mobile composition, accessible controls, asset consistency, and production build |
| **Best with** | Image generation plus the project's existing framework and commerce integrations |

## The method

The skill connects art direction to the truth of the product, creates a consistent image world, then builds the shortest credible path from intrigue to purchase.

| Stage | What happens |
|:--|:--|
| **1 · Find the product tension** | Distill the brief into a customer feeling, visual world, commerce spine, and signature device |
| **2 · Build one image system** | Plan a small family of consistent product images instead of unrelated generated art |
| **3 · Make it shoppable** | Build the hero, browse surface, cart state, brand proof, and honest demo states |
| **4 · Prove it works** | Run the production build and check the storefront at mobile and desktop sizes |

## Requirements

- An existing web project or permission to create one.
- Image generation is strongly recommended for original product photography.
- Checkout, inventory, email, and fulfillment require the user's real providers and credentials. The skill never pretends an unconnected service is live.

## Try it

> [!TIP]
> **Start here:** “Use crazy-ecommerce-builder-skill to turn this ceramic coffee brand into a bold storefront. Keep the checkout as a clearly labeled demo.”

> “Rework my existing shop so it feels experimental and memorable without making it harder to buy.”

> “Create three art directions for this running-shoe launch, then build the strongest one.”

## Output

- A written creative thesis tied to the product.
- A coherent product-image plan and the generated assets used by the project.
- A responsive, accessible commerce experience with working local interactions.
- A successful production build and a short handoff that identifies any unconnected services.

## Inside the skill

```text
crazy-ecommerce-builder-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── commerce-checklist.md
    ├── creative-system.md
    └── image-system.md
```

The references separate creative direction, image continuity, and commerce usability so the agent loads only the detail needed for the current decision.

## Quality bar

The design should lose meaning if swapped onto an unrelated company. The product must remain understandable in the first viewport, the cart must be usable, generated imagery must stay consistent, and incomplete production integrations must be disclosed.

---

[← Browse all BuildFast Skills](../README.md) · [MIT licensed](../LICENSE) · [View the repository](https://github.com/buildfastwithai/buildfast-skills)
