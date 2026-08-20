<div align="center">

# 🛒 Crazy Ecommerce Builder

**Turns a short product brief into an unconventional storefront with a coherent creative thesis—not random effects.**

[Install](#install) · [What it does](#what-it-does) · [Try it](#try-it) · [Browse BuildFast Skills](../README.md)

</div>

## Install

```bash
npx skills add buildfastwithai/buildfast-skills --skill crazy-ecommerce-builder-skill
```

Add `--global` to make it available across projects.

## What it does

The skill connects art direction to the truth of the product, creates a consistent image world, then builds the shortest credible path from intrigue to purchase.

- Distills the brief into a product tension, customer feeling, visual world, commerce spine, and signature device.
- Plans a small family of consistent product images instead of unrelated generated art.
- Builds a distinctive hero, browseable product surface, cart state, brand proof, and honest demo states for services that are not connected.
- Preserves the current framework, functional behavior, and hosting configuration.
- Runs the production build and checks the storefront at mobile and desktop sizes.

## Requirements

- An existing web project or permission to create one.
- Image generation is strongly recommended for original product photography.
- Checkout, inventory, email, and fulfillment require the user's real providers and credentials. The skill never pretends an unconnected service is live.

## Try it

> “Use crazy-ecommerce-builder-skill to turn this ceramic coffee brand into a bold storefront. Keep the checkout as a clearly labeled demo.”

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

[← Browse all BuildFast Skills](../README.md) · [View the repository](https://github.com/buildfastwithai/buildfast-skills)
