# ai-ml-infra — Index & Navigation

Quick reference for everything on this branch.

---

## Files on This Branch

### Positioning
- `positioning/ai-infra-identity.md` — How to frame your experience for AI/ML infrastructure roles

### Prep
- `prep/ai-infra.md` — LLM deployment, Bedrock, SageMaker, serverless AI, cost optimization, ML observability
- `prep/common-interview-questions.md` — Universal behavioral + situational interview prep

### Resume
- `resume/main/resume.md` — AI/ML-infra tailored resume
- `resume/main/highlights.md` — Impact bullets ordered for AI/ML emphasis

### Stories (all available — use AI/ML infra lens)
| Story | AI/ML Infra Angle | Priority |
|-------|------------------|----------|
| `serverless-ai-pipeline.md` | Lambda orchestration, Bedrock + Transcribe, zero-ops pipeline | High |
| `cost-aware-llm.md` | Token cost tracking, model routing, responsible AI cost controls | High |
| `internal-developer-platform.md` | ML dev environments, self-service AI tooling | Medium |
| `kubernetes-deployment.md` | ML model serving, deployment reliability, container orchestration | Medium |
| `cloud-cutover.md` | AI system migrations, high-stakes infra changes | Medium |
| `failure-lessons.md` | AI system failures, observability, learning and recovery | Medium |
| `terraform-state-isolation.md` | IaC foundations for AI workload environments | Low |
| `github-enterprise-migration.md` | Large-scale tooling migrations (dev toolchain changes) | Low |

---

## Interview Prep Checklist

### Before the Interview
- [ ] Read `positioning/ai-infra-identity.md` — know your core narrative cold
- [ ] Study `prep/ai-infra.md` — be ready to go deep on LLM infra, Bedrock, cost tradeoffs
- [ ] Review `prep/common-interview-questions.md` — prep STAR answers with AI-infra framing

### Story Selection (pick 3-4 for an interview)
- [ ] Serverless AI Pipeline — Lambda orchestration, Bedrock + Transcribe (the most direct AI story)
- [ ] Cost-Aware LLM Orchestration — token budgets, model routing, responsible cost controls
- [ ] Internal Developer Platform — ML dev environments, self-service tooling
- [ ] Kubernetes Deployment — model serving patterns, deployment reliability

### Technical Topics to Be Ready For
From `prep/ai-infra.md`:
- AWS Bedrock: model APIs, prompt engineering, embedding patterns, cost per token
- AWS Transcribe: speech-to-text pipeline design, async job patterns
- AWS SageMaker: model training/hosting, endpoint management
- Lambda orchestration: async patterns, Step Functions vs. direct invocation
- Cost optimization: token budgeting, model selection tradeoffs, caching strategies
- ML observability: logging inference calls, latency tracking, error rates
- Serverless architecture: cold starts, concurrency limits, async fan-out patterns

---

## Core Narrative

**For all conversations about this identity**:

> "I build infrastructure that makes AI systems reliable, cost-aware, and production-ready. Whether that's orchestrating multi-model pipelines on Lambda, designing cost guardrails for LLM usage, or building developer environments where ML teams can move fast — I think about AI workloads the same way I think about any production system: observability, cost, and reliability."

Variations:
- **AI/ML platform roles**: Emphasize developer tooling, self-service, ML environment provisioning
- **MLOps/LLMOps**: Emphasize pipeline orchestration, model lifecycle, monitoring
- **Cloud AI engineer**: Emphasize Bedrock, SageMaker, serverless orchestration patterns

---

## System Map

| Branch | Identity | PDF |
|--------|----------|-----|
| `master` | Generic source of truth | — |
| `platform-engineering` | Platform Engineering | `Lyriq-Davis-Platform-Engineering.pdf` |
| `infra-automation` | Infrastructure Automation | `Lyriq-Davis-Infra-Automation.pdf` |
| `ai-ml-infra` | AI/ML Infrastructure | `Lyriq-Davis-AI-ML-Infra.pdf` |

Stories live on `master`. All stories are checked into this branch as reference, but stories tagged `ai-ml-infra` are primary for interviews.

---

## See Also
- `POSITIONING-RULES.md` — Ethics guardrails before any interview
- `CHANGELOG.md` — Branch history
