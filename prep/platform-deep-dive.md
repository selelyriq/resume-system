---
positioning: platform
branch: main
---

# Platform Engineering Deep Dive

## Core Services & Patterns

### Terraform & State Management
- **State isolation strategy**: Remote backends (S3 + DynamoDB), separate state files per concern
- **Module composition**: Reusable, DRY modules for networking, compute, storage, IAM
- **Multi-account design**: Role assumption, cross-account references, centralized vs. decentralized IAM
- **Drift detection**: Terraform refresh cycles, automated drift alerting

**Questions to drill**:
- How do you prevent state file conflicts in multi-team environments?
- What's the difference between state isolation strategies (per env vs. per concern vs. per team)?
- How do you safely handle state file migration or recovery?

### Infrastructure Modularity
- **Blast radius minimization**: How segmentation reduces scope of failures
- **Team ownership**: Clear ownership boundaries via state/repo segmentation
- **Versioning**: How to version infrastructure changes (tagging, releases)
- **Documentation**: Runbooks, architecture diagrams, decision records

### Multi-Account Architecture
- **Account strategy**: Dev/staging/prod, per-product, per-team, security boundaries
- **Role assumption**: Cross-account assume role patterns, trust relationships
- **Networking**: Private/public subnets, inter-account routing, shared services
- **Security**: Account-level isolation, CloudTrail centralization, Security Hub aggregation

### Observability Standards
- **Structured logging**: Log aggregation, filtering, alerting
- **Metrics**: System metrics, custom metrics, dashboarding
- **Tracing**: Distributed tracing, request correlation
- **Alerts**: Meaningful alerting (avoid alert fatigue), runbook links, escalation paths

## Common Failure Modes

- **State file corruption**: Can happen from concurrent writes, incomplete deletions, or version mismatches
- **Blast radius underestimation**: Changes intended for one resource accidentally apply to many
- **Dependency issues**: Removing infrastructure that other systems depend on
- **Secrets in state files**: Accidentally committing sensitive data to version control
- **IAM over-permissioning**: Roles granted more permissions than necessary
- **Multi-account gotchas**: Cross-account role assumption failures, missing trust relationships
- **Rollback failures**: State divergence making rollback impossible

## Key Tradeoffs

| Tradeoff | Option A | Option B | Best For |
|----------|----------|----------|----------|
| State granularity | Many small files | Few large files | Small: many files; Large: few + smaller blast radius |
| Centralized vs. distributed IAM | Central admin service | Per-team IAM | Central: easier governance; Distributed: team velocity |
| Multi-repo vs. monorepo Terraform | Multiple repos | Single repo | Multi: clear ownership; Mono: shared services |
| Manual vs. automated infrastructure changes | Terraform apply after review | Full CI/CD automation | Manual: safety; Automated: velocity |
| Account per team vs. shared accounts | More accounts (higher complexity) | Fewer accounts (less isolation) | Teams: isolation; Startups: simplicity |

## Interview Traps

1. **"How many AWS accounts should we have?"** — Answer: Depends on team structure, blast radius tolerance, and governance. There's no universal number.
2. **"Should we version our infrastructure?"** — Yes, always. Git tags, release notes, documented changes.
3. **"How do we handle infrastructure secrets?"** — Separate from code, use Secrets Manager/Vault, rotate regularly, audit access.
4. **"Can Terraform do everything?"** — No. Terraform is strong on infrastructure, weak on application-level configuration. Know the boundaries.
5. **"How do we prevent state file loss?"** — Remote backends, versioning, backups, disaster recovery procedures.

## Deep Dive Topics

### Designing for Operational Safety
- Understand your blast radius before you build
- Design infrastructure so that failures are isolated, not cascading
- Implement observability so problems are visible immediately

### Scaling Beyond One Team
- What breaks when you add 5 more teams?
- State management, ownership boundaries, change coordination
- How does your platform support team autonomy without chaos?

### Transitioning to Infrastructure as a Product
- Infrastructure should be easy and intuitive for consumers
- Strong documentation and runbooks are not optional
- Versioning and breaking change management matter
