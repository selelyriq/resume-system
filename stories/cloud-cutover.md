---
title: "$80M/Day Cloud Cutover"
identities: [platform-engineering, infra-automation, ai-ml-infra]
characters: [GE Aerospace]
tags: [high-stakes, risk-management, coordination, mission-critical]
---

# $80M/Day Cloud Cutover

## Context

GE Aerospace had a mission-critical application processing approximately $80 million per day in transactions. The application needed to migrate from one cloud infrastructure to another, requiring careful coordination of authentication, DNS, and certificate updates during a narrow maintenance window.

## Challenge

- **Zero margin for error**: Downtime would directly impact revenue
- **Tight coordination**: Multiple systems needed to change in sequence (AD/LDAP, DNS, authentication flows, ALB certificates)
- **Complex identity chain**: AD/LDAP, Saviynt, CyberArk, OIDC, and ALB auth flows — each a potential failure point
- **Rollback complexity**: If the cutover failed, had to revert quickly without manual intervention

## Action

**Pre-cutover preparation**:
- Mapped entire identity chain to understand failure modes before touching anything
- Built detailed runbooks for every cutover step and rollback procedure
- Coordinated with security, networking, and application teams in advance
- Validated authentication flows end-to-end in pre-production environment
- Prepared rollback scripts to restore service quickly if needed

**During cutover (3-hour maintenance window)**:
- Executed DNS changes to route traffic to new infrastructure
- Updated ALB certificates and authentication configuration in sequence
- Validated application functionality and user access at each step
- Monitored for identity chain failures across every auth layer

**Post-cutover**:
- Verified no transactions were lost
- Decommissioned old infrastructure
- Documented lessons learned and updated runbooks

## Result

Seamless continuity with zero downtime. Application remained available throughout the 3-hour maintenance window. Identity authentication held across all layers, and all transactions processed without issue.

## Result by Identity

### Platform Engineering
**Risk-aware, intentional infrastructure design.** This wasn't luck — it was careful preparation, explicit failure mode mapping, and building in safety mechanisms at every layer. The planning discipline — runbooks, staged validation, rollback scripts — is exactly what separates a clean platform migration from a production incident.

### Infra Automation
**Orchestrated, scripted execution eliminated human error.** Every cutover step was documented, sequenced, and pre-validated before the window opened. Rollback scripts were ready before we started. The maintenance window became a deterministic execution of a pre-tested procedure — not an improvised, manual operation. That's the automation mindset applied to operational risk.

### AI/ML Infra
**Production reliability under SLA pressure is a core AI infrastructure competency.** The same discipline that made this cutover clean — mapping failure modes, sequencing changes, validating before committing — is exactly what production AI systems require when rotating model endpoints, migrating vector stores, or swapping inference backends without dropping in-flight requests.

## Key Takeaway

High-stakes infrastructure work requires meticulous planning, deep understanding of system dependencies, and strong coordination. The technical execution is secondary to the planning discipline.
