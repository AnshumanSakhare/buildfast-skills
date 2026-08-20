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

## At a glance

| Signal | Detail |
|:--|:--|
| **Bring** | One conversion goal, offer, audience, traffic source, proof, and brand constraints |
| **Get** | A self-contained HTML page, chosen copy framework/theme, audit results, and an asset/integration checklist |
| **Verifies** | Structure, CTA placement and consistency, likely Core Web Vitals risks, SEO metadata, and message clarity |
| **Needs** | Python 3 for the bundled audits; real proof and integration URLs before launch |

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

> [!TIP]
> **Start here:** “Use landing-page-generator-skill to make a webinar signup page for engineering managers. Traffic comes from LinkedIn ads.”

> “Audit this existing launch page and fix every issue below a B grade.”

> “Create a dark developer-tool page using PAS copy, with one free-trial CTA.”

## Audit loop

```bash
python scripts/conversion_checklist.py page.html
python scripts/cta_analyzer.py page.html
python scripts/page_speed_estimator.py page.html
```

The agent fixes every flagged issue and anything below grade B, then reruns the checks and performs the manual message-quality review in `references/optimization.md`.

### Verified starter baseline

| Check | Local result | What it proves |
|:--|:--|:--|
| Conversion structure | **93 · A** | The starter includes the expected hierarchy, proof, CTA placement, metadata, and mobile safeguards |
| Speed estimator | **100 · A** | The untouched starter stays lean and avoids the common LCP/CLS risks the script can detect |
| CTA analyzer | **65 · C** before copy is filled | Placeholder CTA labels are correctly flagged; a finished page must replace them and reach B or better |

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

[← Browse all BuildFast Skills](../README.md) · [MIT licensed](../LICENSE) · [View the repository](https://github.com/buildfastwithai/buildfast-skills)
