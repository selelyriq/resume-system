# infra-automation — Index & Navigation

Quick reference for everything on this branch.

---

## Files on This Branch

### Positioning
- `positioning/automation-identity.md` — How to frame your experience for automation/DevOps roles

### Prep
- `prep/automation-devops.md` — CI/CD patterns, GitOps, drift detection, event-driven systems, IaC best practices
- `prep/common-interview-questions.md` — Universal behavioral + situational interview prep

### Resume
- `resume/main/resume.md` — Infra-automation tailored resume
- `resume/main/highlights.md` — Impact bullets ordered for automation emphasis

### Stories (all available — use automation lens)
| Story | Automation Angle | Priority |
|-------|-----------------|----------|
| `terraform-state-isolation.md` | Per-env CI/CD pipelines, approval gates, isolated deploys | High |
| `github-enterprise-migration.md` | Migration automation, scripted validation, rollback workflows | High |
| `kubernetes-deployment.md` | GitOps patterns, deployment pipeline performance | High |
| `internal-developer-platform.md` | Self-service automation, eliminating manual provisioning | Medium |
| `cloud-cutover.md` | Runbook-driven cutover, automated execution | Medium |
| `serverless-ai-pipeline.md` | Lambda orchestration, event-driven zero-ops pipelines | Medium |
| `cost-aware-llm.md` | Automated token tracking, cost guardrails in pipeline | Low |
| `failure-lessons.md` | Drift detection, automation failure recovery | Medium |

---

## Interview Prep Checklist

### Before the Interview
- [ ] Read `positioning/automation-identity.md` — know your core narrative cold
- [ ] Study `prep/automation-devops.md` — be ready to go deep on CI/CD, GitOps, IaC
- [ ] Review `prep/common-interview-questions.md` — prep STAR answers with automation framing

### Story Selection (pick 3-4 for an interview)
- [ ] Terraform State Isolation — automation lens (independent pipelines, approval gates)
- [ ] GitHub Enterprise Migration — scripted migration, rollback planning
- [ ] Kubernetes Deployment — GitOps, pipeline performance
- [ ] Serverless AI Pipeline — event-driven Lambda orchestration
- [ ] Internal Developer Platform — self-service, eliminating toil

### Technical Topics to Be Ready For
From `prep/automation-devops.md`:
- GitHub Actions: workflow design, reusable workflows, secrets management
- Terraform: state management, remote backends, DynamoDB locking, drift detection
- GitOps: ArgoCD patterns, reconciliation loops, declarative infra
- Event-driven: Lambda triggers, SNS/SQS patterns, async orchestration
- CI/CD failure modes: flaky pipelines, rollback strategies, blue/green deployment

---

## Core Narrative

**For all conversations about this identity**:

> "I eliminate operational friction through automation and event-driven infrastructure systems. Whether that's building independent CI/CD pipelines per environment, automating large-scale migrations, or replacing manual runbooks with code — I look for the human bottleneck and build the system that removes it."

Variations:
- **Platform-adjacent roles**: Emphasize self-service + developer productivity
- **Pure DevOps/SRE**: Emphasize pipeline reliability + runbook elimination
- **IaC-heavy roles**: Emphasize Terraform state isolation + GitOps patterns

---

## System Map

| Branch | Identity | PDF |
|--------|----------|-----|
| `master` | Generic source of truth | — |
| `platform-engineering` | Platform Engineering | `Lyriq-Davis-Platform-Engineering.pdf` |
| `infra-automation` | Infrastructure Automation | `Lyriq-Davis-Infra-Automation.pdf` |
| `ai-ml-infra` | AI/ML Infrastructure | `Lyriq-Davis-AI-ML-Infra.pdf` |

Stories live on `master`. All 8 stories are checked into this branch as reference, but only stories tagged `infra-automation` are primary for interviews.

---

## See Also
- `POSITIONING-RULES.md` — Ethics guardrails before any interview
- `CHANGELOG.md` — Branch history
