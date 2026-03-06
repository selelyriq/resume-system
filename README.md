# ai-ml-infra — Resume Branch

This is the **AI/ML Infrastructure** identity branch. Use this branch when applying for roles focused on building infrastructure for production AI workloads — model serving, ML pipelines, serverless AI orchestration, cost-aware LLM systems, and cloud-native AI tooling.

**Core narrative**: "I build infrastructure systems that support production AI and ML workloads at scale."

---

## What's on This Branch

```
ai-ml-infra/
├── resume/main/
│   ├── resume.md              # AI/ML-tailored resume (AI services, serverless pipelines front and center)
│   └── highlights.md          # Reordered for AI/ML infrastructure impact
│
├── positioning/
│   └── ai-infra-identity.md   # How to frame your identity for AI/ML infra roles
│
├── prep/
│   ├── ai-infra.md            # Deep-dive: LLM infra, serverless AI, Bedrock, SageMaker, cost optimization
│   └── common-interview-questions.md  # Universal interview prep with AI-infra lens
│
└── stories/                   # Anchor stories — use ai-ml-infra-tagged ones in interviews
```

---

## Interview Prep Workflow

**Days before**: Read `positioning/ai-infra-identity.md` + `prep/ai-infra.md`

**Day before**: Review your priority stories (see below)

**Day of**: Skim `prep/common-interview-questions.md` with AI-infra framing

**During**: Use STAR method. Lead with system design and cost tradeoffs, not just tool names.

---

## Priority Stories for This Identity

| Story | Why it fits |
|-------|-------------|
| `stories/serverless-ai-pipeline.md` | Lambda orchestration, Bedrock + Transcribe pipeline, zero-ops AI infra |
| `stories/cost-aware-llm.md` | Token cost tracking, model routing, responsible AI cost controls |
| `stories/internal-developer-platform.md` | ML dev environments, self-service AI tooling |
| `stories/kubernetes-deployment.md` | ML model serving patterns, deployment reliability |
| `stories/cloud-cutover.md` | High-stakes infra change management (AI system migrations) |
| `stories/failure-lessons.md` | Learning from AI system failures, observability |
| `stories/terraform-state-isolation.md` | IaC foundations for AI workload environments |

Use the **AI/ML Infrastructure Lens** section in each story. That's the framing that fits this identity.

---

## PDF Output

Pushing to this branch triggers the CI pipeline:

```
resume/main/resume.md → Claude API (LaTeX) → pdflatex → Lyriq-Davis-AI-ML-Infra.pdf
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
git checkout ai-ml-infra
git merge master
git push
```

Only touch `resume/main/resume.md` and `resume/main/highlights.md` for content changes. The positioning framing in `positioning/ai-infra-identity.md` rarely needs updating unless your focus shifts.

---

## Key Files

| File | Purpose |
|------|---------|
| `positioning/ai-infra-identity.md` | Who you are for this identity |
| `prep/ai-infra.md` | Technical depth — LLM infra, Bedrock, SageMaker, serverless AI, cost optimization |
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

**Branch**: ai-ml-infra
**Last updated**: 2026-03-06
**Pipeline**: Claude API → LaTeX → pdflatex → `Lyriq-Davis-AI-ML-Infra.pdf`
