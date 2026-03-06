---
title: "Failure Lessons & Career Evolution"
identities: [platform-engineering, infra-automation, ai-ml-infra]
characters: [various]
tags: [tradeoffs, learning, evolution]
---

# Failure Lessons & Career Evolution

## What I Got Wrong

### Early Career: Overcomplicating Infrastructure

Early on, I defaulted to "enterprise-grade" solutions (Terraform modules, GitOps, multi-environment pipelines) even for small projects. Result: unnecessary complexity that slowed iteration.

**Lesson**: Match tool sophistication to problem scale. A startup doesn't need the same infrastructure patterns as GE Aerospace.

### Monolithic Provisioning

Built large Terraform monoliths that applied infrastructure for entire environments at once. When something broke, the blast radius was huge.

**Lesson**: Smaller state files win. Separate by concern, not by "environment bundles."

### Over-automating Too Early

Built extensive automation for processes that happened once per year. Added maintenance burden for minimal benefit.

**Lesson**: Automate after you understand the problem. Premature automation amplifies mistakes — you're just making the wrong thing faster.

### Underestimating Identity Complexity

Assumed OIDC federation was simple until I had to troubleshoot identity-chain failures across AD/LDAP, Saviynt, CyberArk, and ALB auth flows simultaneously.

**Lesson**: Complex systems have complex failure modes. Design for debuggability and observability from the start.

### LLM Cost Optimism

Early versions of Job Scout didn't account for LLM API costs carefully. Would have surprised users with unexpected bills.

**Lesson**: External cost exposure needs guardrails from day one — bake it in, don't bolt it on.

## Evolution

- **2020–2021**: Infrastructure automation fundamentals (Obsidian, early Tartan)
- **2022–2023**: Kubernetes, container orchestration, and team-scale deployment (Tartan)
- **2024–2025**: Multi-account, multi-team infrastructure at enterprise scale (University of Cincinnati, GE Aerospace)
- **2025–present**: AI systems infrastructure, LLM orchestration, cost-aware design (Job Scout, GE AI tooling)

Core insight: **Platform thinking evolves as scale increases.** What works for one team doesn't scale to six, and what works on-premises doesn't translate to cloud without intentional design.

## Reflection by Identity

### Platform Engineering
The biggest failure was building platforms for myself rather than for the teams using them. Simplicity, discoverability, and low onboarding friction matter more than technical elegance. A platform nobody uses is just infrastructure with extra steps.

### Infra Automation
Over-automating too early is a real trap. Automation that runs before you fully understand the process just makes the wrong thing repeatable. The discipline is knowing when a process is stable enough to automate — and resisting the urge until then.

### AI/ML Infra
The LLM cost lesson hit hardest here. AI systems have a unique failure mode: everything works perfectly functionally, but the cost model is broken. You can build a system that does exactly what you designed it to do and still ship something that burns users' money. Cost is a first-class design constraint in AI infrastructure.

## Key Takeaway

Failures teach more than successes. The infrastructure patterns that matter most are usually the ones that failed spectacularly the first time I ignored them.
