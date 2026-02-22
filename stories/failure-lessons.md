---
title: "Failure Lessons & Career Evolution"
identities: [platform, automation, security, ai-infra]
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

**Lesson**: Automate after you understand the problem. Premature automation amplifies mistakes.

### Underestimating Identity Complexity

Assumed OIDC federation was simple until I had to troubleshoot identity-chain failures across AD/LDAP, Saviynt, CyberArk, and ALB auth flows simultaneously.

**Lesson**: Complex systems have complex failure modes. Design for debuggability and visibility.

### LLM Cost Optimism

Early versions of Job Scout didn't account for LLM API costs carefully. Would have surprised users with bills.

**Lesson**: External cost exposure needs guardrails from day one.

## Evolution

- **2020-2021**: Infrastructure automation (Obsidian, early Tartan)
- **2022-2023**: Kubernetes and team-scale deployment (Tartan)
- **2024-2025**: Multi-account, multi-team infrastructure at enterprise scale (University of Cincinnati, GE Aerospace)
- **2025+**: AI systems infrastructure (Job Scout, AI Infra positioning)

Core insight: **Platform thinking evolves as scale increases**. What works for 1 team doesn't scale to 6+ teams, and what works for on-premises doesn't work for cloud.

## Key Takeaway

Failures teach more than successes. The infrastructure patterns that matter most are usually the ones that failed spectacularly when I ignored them.
