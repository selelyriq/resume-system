---
identity: security
branch: security-enterprise
active: true
---

# Security & Enterprise Identity

## Focus Areas

- IAM boundaries and role segmentation
- Least privilege enforcement
- Network isolation and micro-segmentation
- Secret and certificate lifecycle management
- State separation to minimize blast radius
- Identity chain architecture (AD/LDAP, IdP, OIDC)
- Compliance and governance controls
- Cloud misconfiguration prevention

## Core Narrative

**I design guardrails that reduce cloud misconfiguration and limit incident impact.**

Security isn't a feature bolted on at the end—it's a foundational design principle. That means thinking about IAM boundaries, network isolation, and blast radius from the start, and building systems that prevent entire classes of mistakes.

## Key Stories

- **IAM Role Migration & Centralized Identity**: Migrated application roles to centralized identity (IDC), improving access visibility and enabling fine-grained least-privilege enforcement
- **Identity Chain Diagnostics**: Triaged and resolved enterprise identity failures across AD/LDAP, Saviynt, CyberArk, OIDC, and ALB auth flows
- **Terraform State Isolation**: Segmented Terraform state and IAM scopes to prevent cross-environment privilege escalation
- **TLS Lifecycle & Secrets Management**: Owned certificate lifecycle (ACM, Secrets Manager) securing sensitive material across application teams and ALBs

## Technical Refresh

Services: IAM roles and policies, STS federation, OIDC provider integration, Secrets Manager, ACM, Network ACLs vs. security groups, VPC segmentation

Failure modes: Over-privileged roles, credential leakage, overly permissive security groups, public S3 buckets, cross-account trust misconfiguration

Tradeoffs: Centralized vs. distributed identity, OIDC federation vs. temporary credentials, static vs. dynamic secrets, network micro-segmentation vs. operational complexity

Common interview traps: How do you audit IAM usage? What's the blast radius of a credential leak? How do you secure multi-account deployments?
