# Resume System

A Git-based resume system with a generic source of truth on `master` and three identity-tailored public-facing branches. Resume content is compiled into PDFs via a Claude API → LaTeX → pdflatex pipeline running in GitHub Actions.

## Branch Structure

| Branch | Identity | Public | PDF Output |
|---|---|---|---|
| `master` | Generic (internal only) | No | — |
| `platform-engineering` | Platform Engineering | Yes | `Lyriq-Davis-Platform-Engineering.pdf` |
| `infra-automation` | Infrastructure Automation | Yes | `Lyriq-Davis-Infra-Automation.pdf` |
| `ai-ml-infra` | AI/ML Infrastructure | Yes | `Lyriq-Davis-AI-ML-Infra.pdf` |

## How It Works

1. **`master`** is the internal source of truth. Add new experience here first.
2. Each identity branch has a tailored `resume.md` and `highlights.md` with framing specific to that positioning.
3. On every push to an identity branch, GitHub Actions calls the Claude API to generate a `.tex` file from `resume.md`, compiles it with pdflatex, and commits the named PDF back to the branch.

## Repository Structure (master)

```
resume-system/
├── resume/main/
│   ├── resume.md              # Generic base resume (source of truth)
│   ├── highlights.md          # Generic key highlights
│   └── summary.md             # Positioning pitch (varies per branch)
│
├── positioning/
│   ├── platform-identity.md   # Platform Engineering identity & narrative
│   ├── automation-identity.md # Infrastructure Automation identity & narrative
│   └── ai-infra-identity.md   # AI/ML Infrastructure identity & narrative
│
├── stories/
│   ├── cloud-cutover.md                  # $80M/day migration
│   ├── cost-aware-llm.md                 # LLM cost orchestration (Job Scout)
│   ├── failure-lessons.md                # Career evolution & lessons
│   ├── github-enterprise-migration.md    # 400+ repo migration
│   ├── internal-developer-platform.md    # Dev containers platform
│   ├── kubernetes-deployment.md          # K8s & CI/CD performance
│   ├── serverless-ai-pipeline.md         # UC Bedrock/Transcribe pipeline
│   └── terraform-state-isolation.md      # State isolation strategy
│
├── .github/
│   ├── scripts/generate-latex.py  # Calls Claude API, returns .tex from resume.md
│   └── workflows/build-pdf.yml    # CI: .tex → pdflatex → named PDF → commit
│
├── README.md              # This file
├── INDEX.md               # Cross-reference & navigation guide
├── CHANGELOG.md           # Version history
└── POSITIONING-RULES.md   # Ethics guardrails
```

## Adding New Experience

1. Checkout `master`, update `resume/main/resume.md`
2. Reference `positioning/` to understand how to reframe per identity
3. Checkout each identity branch and apply the reframed version
4. Push identity branches to trigger PDF regeneration

## Interview Prep

Stories live in `stories/` on master. Each story has a **Result by Identity** section — read the lens that matches the role you're interviewing for.

Positioning docs in `positioning/` include the core narrative, key stories, technical refresh notes, and common interview traps for each identity.

## Quick Reference

```bash
# Switch to an identity branch
git checkout platform-engineering
git checkout infra-automation
git checkout ai-ml-infra
git checkout master

# Read your resume for the current branch
cat resume/main/resume.md

# Read the positioning guide for the current branch
cat positioning/platform-identity.md      # on platform-engineering
cat positioning/automation-identity.md    # on infra-automation
cat positioning/ai-infra-identity.md      # on ai-ml-infra

# Read a story with all identity lenses
cat stories/cloud-cutover.md
```

## PDF Pipeline

Triggered automatically on push to any identity branch. To test locally:

```bash
# Requires ANTHROPIC_API_KEY in .env
python3 .github/scripts/generate-latex.py
# pdflatex compilation happens in CI only
```

## Ethics

Positioning is emphasis and framing, not fabrication. See `POSITIONING-RULES.md`.

---

**Last updated**: 2026-03-06
**Active branches**: master, platform-engineering, infra-automation, ai-ml-infra
