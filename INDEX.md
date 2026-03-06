# Platform Engineering — Branch Index

## Identity

**Narrative**: "I build the foundation other engineers build on."
**Focus**: Developer experience, internal tooling, platform standardization, IaC modularity, blast radius isolation
**Best for**: Platform engineer, infrastructure systems engineer roles

## Files on this branch

| File | Purpose |
|---|---|
| `resume/main/resume.md` | Platform Engineering tailored resume |
| `resume/main/highlights.md` | Platform Engineering key highlights |
| `positioning/platform-identity.md` | Full identity definition, narrative, interview traps |
| `prep/platform-deep-dive.md` | Technical prep for platform engineering interviews |
| `prep/common-interview-questions.md` | STAR-format interview question prep |

## Priority Stories

Stories live on `master`. Read these with the **Platform Engineering** lens:

| Story | Why it matters for this identity |
|---|---|
| `internal-developer-platform.md` | Your strongest platform story — product thinking, developer experience |
| `terraform-state-isolation.md` | Platform architecture — blast radius, team ownership, scalability |
| `cloud-cutover.md` | Risk-aware execution — planning discipline, failure mode mapping |
| `github-enterprise-migration.md` | Platform consolidation — coordination, phased rollout at scale |
| `kubernetes-deployment.md` | Deployment platform — reliability, enabling application teams |

## Interview Prep Checklist

1. `cat positioning/platform-identity.md` — understand the framing and key talking points
2. `cat prep/platform-deep-dive.md` — technical depth
3. Read Platform Engineering lens in each priority story above
4. `cat prep/common-interview-questions.md` — STAR framework practice

## Key Technical Themes

- Terraform module design and state isolation
- Internal developer platforms (Dev Containers, Makefile workflows)
- GitOps pipelines (GitHub Actions, ArgoCD)
- Multi-account AWS/Azure architecture
- Observability standards (Prometheus, Grafana, CloudWatch)
- Blast radius minimization
