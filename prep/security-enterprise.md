---
positioning: security
branch: security-enterprise
---

# Security & Enterprise Deep Dive

## Core Services & Patterns

### IAM Design & Enforcement
- **Principle of least privilege**: Users/services get minimum permissions needed
- **Role-based access control (RBAC)**: Organizing permissions into reusable roles
- **Permission boundaries**: Limits that prevent over-privileging
- **Service roles vs. user roles**: Different permission models for different identity types
- **Temporary credentials**: STS assume role, session tokens, time-limited access

**Questions to drill**:
- How do you audit IAM usage at scale?
- What's the difference between resource-based and identity-based policies?
- How do you prevent privilege escalation via IAM policy manipulation?

### Identity Chain Architecture
- **Federation**: Connecting external identity providers (Azure AD, Okta) to AWS/Azure
- **OIDC**: Keyless authentication, federated credentials
- **SAML**: Enterprise SSO
- **Multi-hop authentication**: AD → Identity Provider → Assume Role → Application
- **Failure diagnosis**: Understanding each link in the chain

### Network Isolation & Micro-segmentation
- **VPC design**: Private/public subnets, network ACLs, security groups
- **Blast radius**: Designing so network breaches don't expose entire infrastructure
- **Zero trust**: Verify every request, never trust implicit trust
- **Private DNS**: Preventing DNS-based attacks, internal service discovery

### Secret & Certificate Lifecycle
- **Rotation**: How to rotate without service interruption
- **Storage**: Where to store secrets (Secrets Manager, HashiCorp Vault, sealed Kubernetes secrets)
- **Audit trails**: Who accessed which secrets, when
- **Expiration handling**: Detecting and rotating expired certificates before they cause outages

### Compliance & Governance
- **Security Hub**: Compliance frameworks (CIS, PCI-DSS), automated findings
- **Audit logging**: CloudTrail, VPC Flow Logs, application logs
- **Data classification**: What's sensitive, where can it go
- **Access reviews**: Regular audits of who has access to what

## Common Failure Modes

- **Over-permissioned roles**: Roles grant too much access (principle of least privilege violated)
- **Credential leakage**: Secrets checked into Git, exposed in logs, hardcoded in applications
- **Cross-account trust misconfiguration**: Overly permissive trust relationships enabling unauthorized access
- **Unencrypted data**: Data at rest or in transit exposed due to missing encryption
- **Missing audit trails**: Actions not logged, making incident investigation impossible
- **Blast radius underestimation**: Assuming a compromise is isolated when it actually cascades
- **Certificate expiration**: Missing certificate rotations causing service outages
- **Weak identity chain**: One link in authentication failing brings down entire application

## Key Tradeoffs

| Tradeoff | Option A | Option B | Best For |
|----------|----------|----------|----------|
| Centralized vs. distributed IAM | Central admin service | Per-team IAM role creation | Central: governance; Distributed: team velocity |
| Temporary vs. long-lived credentials | Assume role + STS (ephemeral) | IAM user + access key (persistent) | Temporary: security; Long-lived: simplicity (if not exposed) |
| Encrypted at rest vs. unencrypted | All data encrypted | Encryption for sensitive only | Encrypted: uniformly safe; Selective: performance |
| Federation vs. local users | Federate to Azure AD/Okta | Create local IAM users | Federation: SSO, easier offboarding; Local: control |
| Micro-segmentation vs. broader networks | Many security groups (complex) | Few security groups (simple) | Micro: blast radius reduction; Broad: operational simplicity |

## Interview Traps

1. **"Should we use access keys or assume role?"** — Assume role (temporary credentials, STS) is more secure for applications. Access keys are for humans or exceptional cases.
2. **"How do we audit IAM usage at scale?"** — CloudTrail is foundational. Query for specific ARNs, APIs, principals. Use Security Hub for automated findings.
3. **"What's a safe blast radius?"** — Depends on your organization. At minimum: one environment (dev) shouldn't affect another (prod). Ideally: one team's resources don't affect another's.
4. **"Can we encrypt everything?"** — Yes, but it has performance cost. Understand your threat model and encrypt accordingly.
5. **"How do we rotate certificates without downtime?"** — Plan ahead: store new cert in Secrets Manager, update ALB, validate, remove old cert. Automation is critical.

## Deep Dive Topics

### Designing Security as Foundational
- Security shouldn't be an afterthought or compliance checkbox
- Good security design makes operations easier (fewer surprises)
- Bad security design creates operational burden

### Auditing for Compliance
- Compliance frameworks (CIS, PCI-DSS) are starting points, not endpoints
- Understand your threat model: what are you protecting against?
- Regular audits catch drift and misconfigurations

### Incident Response & Blast Radius
- How quickly can you detect a security incident?
- How quickly can you contain it?
- Can you isolate a compromised account/resource before it spreads?
