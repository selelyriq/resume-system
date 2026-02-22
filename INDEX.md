# Resume System Index & Cross-Reference Guide

This document maps the resume system's structure and helps you navigate between branches, identities, and supporting materials.

## Quick Navigation

### By Branch

| Branch | Positioning | Primary Focus | Ideal For |
|--------|-------------|---------------|-----------|
| **main** | Platform Engineering | System design, architecture, scalability | Infrastructure systems roles, platform engineer positions |
| **automation-devops** | Automation & DevOps | CI/CD, GitOps, eliminating toil | DevOps engineer, cloud infrastructure positions |
| **security-enterprise** | Security & Enterprise | IAM, blast radius, compliance | Security engineer, enterprise architecture roles |
| **ai-infra** | AI Infrastructure | ML systems, data pipelines, cost optimization | ML infrastructure engineer, AI systems engineer roles |

### By Identity

#### Platform Engineering (`positioning/platform-identity.md`)
- **Stories**: Terraform State Isolation, GitHub Enterprise Migration, Internal Developer Platform, $80M Cutover
- **Prep**: `prep/platform-deep-dive.md`
- **Key themes**: Modularity, blast radius, reusability, team ownership

#### Automation & DevOps (`positioning/automation-identity.md`)
- **Stories**: Terraform State Isolation (automation lens), GitHub Enterprise Migration, Internal Developer Platform, CI/CD Performance
- **Prep**: `prep/automation-devops.md`
- **Key themes**: CI/CD pipelines, GitOps, eliminating manual work, event-driven systems

#### Security & Enterprise (`positioning/security-identity.md`)
- **Stories**: Terraform State Isolation (security lens), $80M Cutover, Identity Chain Diagnostics
- **Prep**: `prep/security-enterprise.md`
- **Key themes**: IAM boundaries, least privilege, blast radius, compliance

#### AI Infrastructure (`positioning/ai-infra-identity.md`)
- **Stories**: Cost-Aware LLM Orchestration
- **Prep**: `prep/ai-infra.md`
- **Key themes**: ML systems design, data pipelines, cost awareness, model lifecycle

### By Story

Each story in `stories/` has YAML frontmatter tagging which identities it aligns to:

| Story | Identities | Use Cases |
|-------|-----------|-----------|
| `terraform-state-isolation.md` | platform, automation, security | Blast radius design, team ownership, automation patterns |
| `github-enterprise-migration.md` | platform, automation | Large-scale change management, coordination |
| `internal-developer-platform.md` | platform, automation | Developer experience, standardization |
| `cloud-cutover.md` | platform, security | High-stakes infrastructure, risk management |
| `kubernetes-deployment.md` | platform, automation | Performance, reliability, deployment scale |
| `cost-aware-llm.md` | ai-infra | Cost optimization, responsible AI |
| `failure-lessons.md` | platform, automation, security, ai-infra | Learning from mistakes, evolution |

### By Prep Materials

| File | Branch | Best For |
|------|--------|----------|
| `prep/platform-deep-dive.md` | main | Understanding system design, state isolation, multi-account architecture |
| `prep/automation-devops.md` | automation-devops | GitHub Actions, GitOps, CI/CD patterns, drift detection |
| `prep/security-enterprise.md` | security-enterprise | IAM design, compliance, network isolation, incident response |
| `prep/ai-infra.md` | ai-infra | LLM deployment, feature stores, model lifecycle, ML observability |
| `prep/common-interview-questions.md` | all | Universal interview prep with positioning-specific answers |

## Interview Preparation Workflow

### Preparing for a Platform Engineering Role
1. **Review**: `positioning/platform-identity.md` (understand the framing)
2. **Study**: `prep/platform-deep-dive.md` (technical depth)
3. **Prepare stories**:
   - Terraform State Isolation
   - Internal Developer Platform
   - $80M Cutover
4. **Practice**: Use `prep/common-interview-questions.md` with platform lens
5. **Use branch**: Checkout `main` branch for resume

### Preparing for an Automation/DevOps Role
1. **Review**: `positioning/automation-identity.md`
2. **Study**: `prep/automation-devops.md`
3. **Prepare stories**:
   - Terraform State Isolation (automation lens)
   - GitHub Enterprise Migration
   - Kubernetes Deployment & CI/CD
4. **Practice**: Common interview questions emphasizing automation
5. **Use branch**: Checkout `automation-devops` branch for resume

### Preparing for a Security Role
1. **Review**: `positioning/security-identity.md`
2. **Study**: `prep/security-enterprise.md`
3. **Prepare stories**:
   - Terraform State Isolation (security lens)
   - $80M Cutover (identity chain, risk management)
   - IAM and compliance focus
4. **Practice**: Common interview questions with security lens
5. **Use branch**: Checkout `security-enterprise` branch for resume

### Preparing for an AI Infrastructure Role
1. **Review**: `positioning/ai-infra-identity.md`
2. **Study**: `prep/ai-infra.md`
3. **Prepare stories**:
   - Cost-Aware LLM Orchestration
   - ML systems and data pipeline design
4. **Practice**: Common interview questions with AI-infra lens
5. **Use branch**: Checkout `ai-infra` branch for resume

## Using YAML Frontmatter Tags

Stories and prep files use YAML frontmatter to tag which identities they serve:

```yaml
---
title: "Example Story"
identities: [platform, automation, security]
characters: [GE Aerospace]
tags: [infrastructure-design, risk-management]
---
```

Use frontmatter to:
- Filter stories by identity
- Build positioning-specific prep checklists
- Ensure consistency across branches

## Resume File Structure

### Main Branch
```
resume/main/
├── resume.md       # Full resume (canonical source)
├── summary.md      # 2-3 line pitch (positioning customizable)
└── highlights.md   # Reorderable impact bullets (customizable per branch)
```

### Other Branches
Same structure as main; only `summary.md` and `highlights.md` change per branch positioning. Core `resume.md` content is consistent across all branches (no duplication).

## Version Tags

Releases are tagged in Git:
```
v1.0-platform    # Platform engineering primary positioning
v1.1-automation  # Automation DevOps focus
v2.0-ai-infra    # AI Infrastructure positioning
```

Use Git tags to track your resume evolution over time.

## Maintaining This System

### When to Update

**Add new stories**:
- Major project completion
- Significant career evolution
- New positioning added

**Update positioning**:
- Career pivot or emphasis shift
- New technical areas of focus
- Feedback from interviews

**Refresh prep materials**:
- New technologies or patterns learned
- Interview feedback revealing gaps
- Market changes requiring new emphasis

### Keeping Branches in Sync

The core `resume/main/resume.md` file should stay consistent across branches. Only branch-specific files (`summary.md`, `highlights.md`, `positioning/*.md`) differ.

To update across branches:
```bash
git checkout main
# make core changes
git commit -m "Update resume core content"
git checkout automation-devops
git merge main --strategy-option theirs resume/main/resume.md
```

## Ethics & Positioning

See `POSITIONING-RULES.md` for complete guidelines on:
- What is honest positioning
- What is not acceptable
- How to adapt stories ethically
- Impact framing principles
