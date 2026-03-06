---
identity: automation
branch: automation-devops
active: true
---

# Automation & DevOps Identity

## Focus Areas

- CI/CD pipelines and workflow optimization
- GitHub Actions and OIDC federation
- EventBridge and serverless event-driven patterns
- GitOps workflows and ArgoCD
- Eliminating manual toil through automation
- Deterministic, repeatable deployments
- Infrastructure drift detection and remediation

## Core Narrative

**I eliminate operational friction through automation and event-driven systems.**

Every manual process is a bottleneck and a source of human error. The goal is building systems that run deterministically, with humans reserved for decisions and emergencies.

## Key Stories

- **Terraform State Isolation + GitOps**: Modularized Terraform repos to enable independent CI/CD pipelines per environment, reducing deployment friction
- **Automated Image Builds**: Built Packer + GitHub Actions pipeline to reliably produce hardened golden AMIs and Azure images, eliminating manual image creation
- **GitHub Actions CI/CD**: Established end-to-end deployment automation using GitHub Actions, ECR, and Kubernetes, improving speed by 3x and reducing failures by 60%
- **Serverless Automation**: Orchestrated AWS Lambda, SQS, Textract, and Bedrock workflows to automate Teams transcript ingestion and summarization

## Technical Refresh

Services: GitHub Actions OIDC, Terraform remote backend locking, ArgoCD reconciliation, EventBridge scheduling, GitHub Actions Environments and OIDC federation

Failure modes: Drift, state corruption, race conditions in pipelines, rollback failures, unsecured webhooks

Tradeoffs: Declarative vs. imperative automation, pipeline fan-out vs. monorepo, state file granularity, when to use event-driven vs. scheduled

Common interview traps: How to test CI/CD? How do you handle rollbacks? What's your drift strategy?
