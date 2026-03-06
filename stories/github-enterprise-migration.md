---
title: "GitHub Enterprise to SaaS Migration"
identities: [platform-engineering, infra-automation]
characters: [GE Aerospace]
tags: [migration, change-management, risk-reduction, coordination]
---

# GitHub Enterprise to SaaS Migration

## Context

GE Aerospace operated GitHub Enterprise with 400+ repositories, self-hosted with significant operational overhead. The decision was made to migrate to GitHub.com SaaS to reduce that burden and gain access to newer features. At 400+ repos across dozens of application teams, there was no room for a chaotic, ad-hoc migration.

## Challenge

- **Scale**: Moving 400+ repositories without losing history, disrupting CI/CD, or orphaning anything
- **Coordination**: Multiple application teams with different schedules, risk tolerances, and levels of engagement
- **Data safety**: No repositories accidentally archived, deprecated, or lost in transit
- **Timeline**: Migration needed to complete within a defined window — no indefinite runway

## Action

**Designed a staged, risk-ordered migration**:
- Categorized repositories by criticality and team ownership
- Built a planning and tracking system to monitor progress and surface blockers
- Created runbooks for repository moves, deprecations, and archival workflows
- Coordinated directly with application owners and stakeholders for every move
- Implemented post-migration validation checks (branch protection rules, secrets cleanup, workflow re-enablement)

**Executed in phases**:
- Low-risk, non-critical repositories first — used to validate the migration process itself
- Medium-risk repositories with team sign-off at each step
- High-risk, mission-critical repositories last, with rollback plans ready

## Result

400+ repositories migrated successfully. No history lost, no workflows broken, no teams blocked. The process itself became a reusable template for future large-scale repository operations.

## Result by Identity

### Platform Engineering
**Platform consolidation at scale requires process as much as technical execution.** The tooling mattered less than the coordination model — categorizing by risk, phasing the rollout, and getting team buy-in before moving anything critical. The migration process became a reusable playbook for future platform-level changes affecting multiple teams simultaneously.

### Infra Automation
**Automated validation and change tracking eliminated manual coordination overhead.** Built tooling to track migration status, validate post-migration state automatically, and surface blockers before they became blockers. The goal was to reduce the per-repo manual effort to near zero for low-risk cases, reserving human attention for the high-risk migrations that actually needed it.

## Key Takeaway

Large-scale infrastructure changes are 20% technical and 80% coordination. The technical work is secondary to stakeholder management, risk ordering, and having clear rollback plans before you start.
