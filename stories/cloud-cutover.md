---
title: "$80M/Day Cloud Cutover"
identities: [platform, security]
characters: [GE Aerospace]
tags: [high-stakes, risk-management, coordination, mission-critical]
---

# $80M/Day Cloud Cutover

## Context

GE Aerospace had a mission-critical application processing approximately $80 million per day in transactions. The application needed to migrate from one cloud infrastructure to another, requiring careful coordination of authentication, DNS, and certificate updates during a narrow maintenance window.

## Challenge

- **Zero margin for error**: Downtime would directly impact revenue
- **Tight coordination**: Multiple systems needed to change in sequence (AD/LDAP, DNS, authentication flows, ALB certificates)
- **Unknown unknowns**: Complex identity chain with AD/LDAP, Saviynt, CyberArk, OIDC, and ALB auth flows
- **Rollback complexity**: If the cutover failed, had to revert quickly without manual intervention

## Action

**Pre-cutover preparation**:
- Mapped entire identity chain to understand failure modes
- Built detailed runbooks for cutover steps and rollback procedures
- Coordinated with security, networking, and application teams
- Validated authentication flows in pre-production environment
- Prepared rollback scripts to restore service quickly if needed

**During cutover (3-hour maintenance window)**:
- Executed DNS changes to route traffic to new infrastructure
- Updated ALB certificates and authentication configuration
- Validated application functionality and user access
- Monitored for identity chain failures (AD/LDAP, OIDC, certificate validation)

**Post-cutover**:
- Verified no transactions were lost
- Decommissioned old infrastructure
- Documented lessons learned

## Result

**Seamless continuity with zero downtime**. Application remained available throughout the 3-hour maintenance window. Identity authentication never failed, and all transactions processed without issue.

## Result (by positioning)

### Platform Engineering Lens
**Risk-aware, intentional infrastructure design**. This wasn't luck—it was careful preparation, understanding failure modes, and building in safety mechanisms.

### Security Lens
**Designed and executed secure authentication cutover**. The identity chain was complex, but by understanding each component and its failure modes, we prevented security breaches while changing infrastructure.

## Key Takeaway

High-stakes infrastructure work requires meticulous planning, deep understanding of system dependencies, and strong coordination. The technical skill is secondary to the planning discipline.
