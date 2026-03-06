# infra-automation — Resume Branch

This is the **Infrastructure Automation** identity branch. Use this branch when applying for roles focused on CI/CD engineering, GitOps, IaC automation, event-driven pipelines, and eliminating operational toil.

**Core narrative**: "I eliminate operational friction through automation and event-driven infrastructure systems."

---

## What's on This Branch

```
infra-automation/
├── resume/main/
│   ├── resume.md              # Automation-tailored resume (CI/CD, GitOps, IaC front and center)
│   └── highlights.md          # Reordered for automation impact stories
│
├── positioning/
│   └── automation-identity.md # How to frame your identity for automation roles
│
├── prep/
│   ├── automation-devops.md   # Deep-dive: CI/CD, GitOps, drift detection, event-driven systems
│   └── common-interview-questions.md  # Universal interview prep with automation lens
│
└── stories/                   # Anchor stories — use automation-tagged ones in interviews
```

---

## Interview Prep Workflow

**Days before**: Read `positioning/automation-identity.md` + `prep/automation-devops.md`

**Day before**: Review your priority stories (see below)

**Day of**: Skim `prep/common-interview-questions.md` with automation framing

**During**: Use STAR method. Lead with friction eliminated, not tools used.

---

## Priority Stories for This Identity

| Story | Why it fits |
|-------|-------------|
| `stories/terraform-state-isolation.md` | Independent CI/CD pipelines per environment, approval gates |
| `stories/github-enterprise-migration.md` | Large-scale automation, migration scripting, rollback planning |
| `stories/kubernetes-deployment.md` | GitOps deployment patterns, pipeline performance |
| `stories/internal-developer-platform.md` | Self-service automation, eliminating manual onboarding |
| `stories/cloud-cutover.md` | Automated cutover execution, runbook-driven operations |
| `stories/serverless-ai-pipeline.md` | Event-driven Lambda orchestration, zero-ops AI pipeline |
| `stories/failure-lessons.md` | Learning through automation failure, drift and recovery |

Use the **Infra-Automation Lens** section in each story. That's the framing that fits this identity.

---

## PDF Output

Pushing to this branch triggers the CI pipeline:

```
resume/main/resume.md → Claude API (LaTeX) → pdflatex → Lyriq-Davis-Infra-Automation.pdf
```

The PDF is committed back to this branch automatically.

---

## Resume Update Workflow

Resume content lives in `resume/main/resume.md`. To update:

```bash
# Make changes on master (source of truth), then pull into this branch
git checkout master
# edit resume/main/resume.md
git commit -m "feat: update resume with new achievement"
git checkout infra-automation
git merge master
git push
```

Only touch `resume/main/resume.md` and `resume/main/highlights.md` for content changes. The positioning framing in `positioning/automation-identity.md` rarely needs updating unless your focus shifts.

---

## Key Files

| File | Purpose |
|------|---------|
| `positioning/automation-identity.md` | Who you are for this identity |
| `prep/automation-devops.md` | Technical depth — CI/CD, GitOps, IaC |
| `prep/common-interview-questions.md` | Behavioral + situational interview prep |
| `resume/main/resume.md` | The resume itself |
| `POSITIONING-RULES.md` | Ethics guardrails — read before any interview |

---

## Branch Overview

| Branch | Identity | PDF Output |
|--------|----------|------------|
| `master` | Source of truth (generic) | — |
| `platform-engineering` | Platform Engineering | `Lyriq-Davis-Platform-Engineering.pdf` |
| `infra-automation` | Infrastructure Automation | `Lyriq-Davis-Infra-Automation.pdf` |
| `ai-ml-infra` | AI/ML Infrastructure | `Lyriq-Davis-AI-ML-Infra.pdf` |

---

**Branch**: infra-automation
**Last updated**: 2026-03-06
**Pipeline**: Claude API → LaTeX → pdflatex → `Lyriq-Davis-Infra-Automation.pdf`
