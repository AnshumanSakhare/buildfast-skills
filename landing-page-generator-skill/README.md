<div align="center">

# 🛬 Landing Page Generator

**Builds one production-ready HTML landing page, then audits the conversion path, CTA system, and likely performance risks.**

[Install](#install) · [What ships](#what-ships) · [Try it](#try-it) · [Browse BuildFast Skills](../README.md)

</div>

## Install

```bash
npx skills add buildfastwithai/buildfast-skills --skill landing-page-generator-skill
```

Add `--global` to make it available across projects.

## What ships

- A self-contained HTML starter with nine conversion sections, four themes, SEO metadata, FAQ schema, and core performance safeguards.
- Copy guidance for PAS, AIDA, and Before–After–Bridge.
- Section, visual-style, and optimization references.
- Three Python audits for page structure, CTA placement and consistency, and estimated speed risks.

The skill treats one page as one conversion goal. It removes sections that do not support that goal and never invents testimonials, logos, customer names, metrics, or guarantees.

## Requirements

- Python 3 to run the bundled audits.
- Real URLs for forms, checkout, booking, or analytics before those integrations can be called complete.
- Real proof from the user; missing testimonials and metrics remain clearly marked placeholders.

## Try it

> “Use landing-page-generator-skill to make a webinar signup page for engineering managers. Traffic comes from LinkedIn ads.”

> “Audit this existing launch page and fix every issue below a B grade.”

> “Create a dark developer-tool page using PAS copy, with one free-trial CTA.”

## Audit loop

```bash
python scripts/conversion_checklist.py page.html
python scripts/cta_analyzer.py page.html
python scripts/page_speed_estimator.py page.html
```

The agent fixes every flagged issue and anything below grade B, then reruns the checks and performs the manual message-quality review in `references/optimization.md`.

## Inside the skill

```text
landing-page-generator-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── template.html
├── references/
│   ├── copy-frameworks.md
│   ├── design-styles.md
│   ├── optimization.md
│   └── section-library.md
└── scripts/
    ├── conversion_checklist.py
    ├── cta_analyzer.py
    └── page_speed_estimator.py
```

## Output

You receive the finished HTML, chosen framework and theme, audit results, assumptions, and a precise list of real assets or integrations still needed.

---

[← Browse all BuildFast Skills](../README.md) · [View the repository](https://github.com/buildfastwithai/buildfast-skills)
