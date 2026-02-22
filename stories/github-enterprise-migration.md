---
title: "GitHub Enterprise to SaaS Migration"
identities: [platform, automation]
characters: [GE Aerospace]
tags: [migration, change-management, risk-reduction, coordination]
---

# GitHub Enterprise to SaaS Migration

## Context

GE Aerospace operated GitHub Enterprise with 400+ repositories, locally maintained with significant operational overhead. The decision was made to migrate to GitHub.com SaaS to reduce operational burden and gain access to newer features.

## Challenge

- **Scale**: Moving 400+ repositories without losing history, losing access, or disrupting workflows
- **Coordination**: Multiple application teams with different deployment schedules and risk tolerances
- **Data safety**: Ensuring no repositories were orphaned or accidentally archived
- **Timeline pressure**: Migration needed to happen within a specific window

## Action

**Designed staged migration approach**:
- Categorized repositories by criticality and team ownership
- Built a planning and tracking system to monitor migration progress
- Created runbooks for repository moves, deprecations, and archival workflows
- Coordinated with application owners and repo stakeholders for each move
- Implemented validation checks post-migration (branch protection, secrets cleanup)

**Executed migration in phases**:
- Low-risk, non-critical repositories first (validation of process)
- Medium-risk repositories with team validation
- High-risk, mission-critical repositories last (with rollback plans)

## Result (by positioning)

### Platform Engineering Lens
**Reduced operational complexity at scale**. By implementing a systematic, coordinated approach, we demonstrated that operating 400+ repositories at SaaS scale is more manageable than on-premises. The process itself became reusable for future large-scale repository changes.

### DevOps/Automation Lens
**Automated validation and change tracking**. Built tooling to track migration status, validate post-migration state, and automatically update team documentation. Reduced manual coordination overhead.

## Key Takeaway

Large-scale infrastructure changes require careful planning, coordination with stakeholders, and staged rollout. The technical work is secondary to the coordination and risk management.
