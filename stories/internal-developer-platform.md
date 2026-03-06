---
title: "Internal Developer Platform & Onboarding Optimization"
identities: [platform-engineering, infra-automation, ai-ml-infra]
characters: [GE Aerospace]
tags: [developer-experience, standardization, operational-efficiency]
---

# Internal Developer Platform & Onboarding Optimization

## Context

At GE Aerospace, 6+ application teams had varying development environments, build processes, and deployment practices. Inconsistency created real friction: new developers spent 1–2 days just getting set up, teams had siloed CI/CD patterns, and "works on my machine" was a recurring problem.

## Challenge

- **Environment drift**: Every developer's local setup was subtly different, causing hard-to-reproduce issues
- **Onboarding friction**: Inconsistent documentation meant every new team member had a different experience
- **Knowledge silos**: Teams operated with different mental models of how to build, test, and deploy
- **Reproducibility**: No guarantee that what worked locally would work in CI or production

## Action

**Productized a standardized developer platform**:
- Built VS Code Dev Containers that bundled all dependencies, tools, and runtime environments into a single, reproducible container
- Created Makefile-driven workflows for common operations: `make build`, `make test`, `make deploy` — familiar interface, no new tooling required
- Centralized documentation and runbooks in a shared template repository
- Rolled out to teams iteratively, gathered feedback, refined based on real usage

**Outcomes**:
- Onboarding reduced from 1–2 days to under 30 minutes
- Environment drift eliminated — every developer runs an identical container
- Consistent CI/CD expectations across all 6+ teams
- New team members contributing on day one

## Key Success Factors

- **Simplicity over sophistication**: Makefile requires no new tooling, works everywhere
- **User feedback loop**: Gathered input from the teams actually using it, not just designing in a vacuum
- **Iteration**: Version 1 wasn't perfect — refined based on real usage patterns

## Result by Identity

### Platform Engineering
**A platform is a product, not just infrastructure.** The technical implementation (Dev Containers, Makefile) was straightforward. The hard part was understanding what friction actually looked like for each team, designing something simple enough that adoption wasn't a project in itself, and iterating based on feedback. Onboarding going from 1–2 days to 30 minutes is a platform metric, not just an ops metric.

### Infra Automation
**Automated environment provisioning eliminated the entire class of "setup" problems.** Instead of documentation that gets stale, or setup scripts that break on new machines, the container is the environment — it's always current, always reproducible, and always identical across developers and CI. The Makefile automation layer made the common operations one command instead of a multi-step manual process.

### AI/ML Infra
**Standardized ML development environments are an undervalued AI infrastructure problem.** The same environment drift that slows application developers is worse for ML teams — where Python version mismatches, CUDA dependencies, and library conflicts create hard-to-debug failures. The Dev Container pattern scales directly to ML contexts: pin the environment, make it reproducible, eliminate the "it works on my GPU" problem.

## Key Takeaway

A platform isn't just infrastructure — it's the experience of using it. The onboarding metric (1–2 days → 30 minutes) matters because it compounds: every new team member, every new project, every context switch. Optimizing for consistency and developer experience has outsized impact on team velocity.
