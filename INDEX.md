# Resume System Index

## Branches

| Branch | Identity | Narrative | Best For |
|---|---|---|---|
| `master` | Generic (internal) | Source of truth | Adding new experience, updating stories |
| `platform-engineering` | Platform Engineering | "I build the foundation other engineers build on" | Platform engineer, infra systems roles |
| `infra-automation` | Infrastructure Automation | "I eliminate operational friction through automation" | DevOps engineer, cloud automation roles |
| `ai-ml-infra` | AI/ML Infrastructure | "I build infrastructure that makes AI systems production-ready" | ML infra engineer, AI systems engineer roles |

## Stories (all on master)

Each story has a **Result by Identity** section for all three active identities.

| Story | Identities | Key Theme |
|---|---|---|
| `cloud-cutover.md` | all three | High-stakes migration, operational reliability |
| `cost-aware-llm.md` | all three | LLM cost governance, platform guardrails |
| `failure-lessons.md` | all three | Career evolution, lessons learned |
| `github-enterprise-migration.md` | platform-engineering, infra-automation | Large-scale change management |
| `internal-developer-platform.md` | all three | Developer experience, env standardization |
| `kubernetes-deployment.md` | all three | Container orchestration, CI/CD |
| `serverless-ai-pipeline.md` | ai-ml-infra, infra-automation | Bedrock/Transcribe AI pipeline |
| `terraform-state-isolation.md` | all three | Blast radius, team ownership, IaC design |

## Positioning Docs

| File | Branch | Purpose |
|---|---|---|
| `positioning/platform-identity.md` | platform-engineering | Focus areas, narrative, key stories, interview traps |
| `positioning/automation-identity.md` | infra-automation | Focus areas, narrative, key stories, interview traps |
| `positioning/ai-infra-identity.md` | ai-ml-infra | Focus areas, narrative, key stories, interview traps |

## Prep Files (per identity branch)

| File | Branch |
|---|---|
| `prep/platform-deep-dive.md` | platform-engineering |
| `prep/automation-devops.md` | infra-automation |
| `prep/ai-infra.md` | ai-ml-infra |
| `prep/common-interview-questions.md` | platform-engineering, infra-automation |

## Interview Prep Workflow

### Platform Engineering Role
1. `cat positioning/platform-identity.md`
2. `cat prep/platform-deep-dive.md`
3. Stories to prep: `internal-developer-platform.md`, `terraform-state-isolation.md`, `cloud-cutover.md`, `github-enterprise-migration.md`
4. Read **Platform Engineering** lens in each story

### Infra Automation Role
1. `cat positioning/automation-identity.md`
2. `cat prep/automation-devops.md`
3. Stories to prep: `terraform-state-isolation.md`, `kubernetes-deployment.md`, `serverless-ai-pipeline.md`, `github-enterprise-migration.md`
4. Read **Infra Automation** lens in each story

### AI/ML Infrastructure Role
1. `cat positioning/ai-infra-identity.md`
2. `cat prep/ai-infra.md`
3. Stories to prep: `serverless-ai-pipeline.md`, `cost-aware-llm.md`, `kubernetes-deployment.md`, `cloud-cutover.md`
4. Read **AI/ML Infra** lens in each story

## Keeping Branches in Sync

New experience goes on `master` first. To cascade to identity branches:

```bash
# 1. Update master
git checkout master
# edit resume/main/resume.md
git commit -m "feat: add [new experience]"

# 2. Apply tailored version to each identity branch
git checkout platform-engineering
# edit resume/main/resume.md with platform framing
git commit -m "feat: add [new experience] — platform lens"

git checkout infra-automation
# edit with automation framing
git commit -m "feat: add [new experience] — automation lens"

git checkout ai-ml-infra
# edit with AI/ML framing
git commit -m "feat: add [new experience] — ai-ml-infra lens"

# 3. Push identity branches to trigger PDF regeneration
git push origin platform-engineering infra-automation ai-ml-infra
```
