---
name: Lyriq Davis
contact: (419) 984-4884 | lyriqsele@gmail.com
---

## Summary

Infrastructure Automation Engineer with 5+ years designing CI/CD pipelines, GitOps workflows, and modular IaC foundations across AWS and Azure. Deep expertise in Terraform module architecture, GitHub Actions-driven delivery, ArgoCD-based GitOps, and event-driven serverless automation at enterprise scale. Focused on eliminating manual operations through deterministic, repeatable infrastructure delivery that enforces consistency and reduces deployment friction.

---

## Education

**AWS Solutions Architect Associate** — March 2025
**AWS SysOps Associate** — February 2025
**Terraform Certified Associate** — September 2024
**University of Cincinnati** — *Bachelors of Arts - Media Production* — Expected May 2026

---

## Core Competencies & Skills

**Technical:**
Infrastructure as Code, CI/CD Pipeline Engineering, GitOps, Configuration Management, Automation, Kubernetes, Cloud Architecture, Observability, Event-Driven Automation, Infrastructure Drift Remediation, Serverless Orchestration

**Technology Tools & Platforms:**
Terraform, GitHub Actions, ArgoCD, Packer, Ansible, AWS (EC2, S3, IAM, SSM, CloudWatch, ECS, EKS, Lambda, SQS, Textract, Bedrock, API Gateway), Azure (VNet, AKS, Private DNS, Private Link), Docker, Kubernetes, Helm, Prometheus, Grafana, Python, AWS CodePipeline

---

## Experience

### General Electric Aerospace — via Capgemini
**Cloud Engineer** | August 2025 - Present | Cincinnati, OH

- Productized a standardized internal developer platform using VS Code Dev Containers and Makefile-driven workflows, eliminating environment drift and reducing onboarding time from 1–2 days to under 30 minutes across 6+ application teams.
- Drove large-scale GitHub Enterprise to GitHub SaaS migration of 400+ repositories, coordinating across application owners and stakeholders to plan and execute phased repo moves, deprecations, and archival workflows at enterprise scale.
- Executed a high-stakes cloud-to-cloud application migration supporting a mission-critical system processing ~$80M/day, orchestrating a three-hour maintenance window involving authentication-path cutover, AD/LDAP join/unjoin, DNS reconfiguration, and ALB certificate updates with zero downtime.

### University of Cincinnati
**Cloud Engineer** | January 2025 - August 2025 | Cincinnati, OH

- Built reusable, idempotent Terraform modules to standardize AWS and Azure infrastructure (networking, compute, IAM, observability), integrating plan/apply validation gates within GitHub-based CI/CD workflows.
- Architected Terraform state isolation strategy by separating infrastructure into logically scoped state files and repositories (networking, shared services, application stacks) segmented by account and environment, minimizing blast radius and enabling safer, auditable change workflows.
- Implemented GitHub Actions and ArgoCD GitOps pipelines with branching strategies, pull-request reviews, automated chart validation, and container scanning to ensure safe, versioned infrastructure and application changes.
- Automated multicloud image builds using Packer + GitHub Actions, producing hardened golden AMIs and Azure images aligned to enterprise security standards.
- Designed and implemented Python-based automation (boto3, REST APIs) to orchestrate serverless workflows across AWS (Lambda, S3, SQS, Textract, Bedrock, API Gateway) for automated Teams transcript ingestion and AI-driven summarization.
- Deployed observability tooling (Prometheus, Grafana, Alloy, CloudWatch dashboards) implementing structured logging, metrics, and alerting for infrastructure and automation workflows.

### Tartan Builders
**Cloud Engineer** | October 2022 - December 2024 | Dublin, OH

- Designed and maintained configuration management pipelines using Ansible to enforce standardized CloudWatch Agent settings across golden AMI EC2 fleets, ensuring consistent logging and metrics baselines with repeatable, idempotent deployment.
- Architected containerized application infrastructure using Docker and Kubernetes, defining deployment manifests, resource limits, and rollout strategies to support production workloads and improve release reliability.
- Developed Python automation to manage EC2 instance lifecycle scheduling, aligning runtime with business hours to reduce cloud spend on non-production environments.
- Built end-to-end CI/CD pipelines using GitHub Actions, Docker, and ECR to automate container image builds, testing, and deployment for AWS-hosted web applications, reducing manual release overhead and enforcing quality gates through automated test execution.

### Obsidian Productions
**Digital Solutions Specialist** | June 2020 - June 2022 | Mansfield, OH

- Provisioned AWS infrastructure using CloudFormation, authoring repeatable stack templates to define and manage hosting environments, establishing an infrastructure-as-code foundation for cloud deployments.
- Configured S3-hosted static web environments and implemented automated deployment pipelines via AWS CodePipeline, enabling version-controlled, repeatable releases from GitHub to production.
- Introduced source control practices and maintained documentation of deployment processes, configuration changes, and infrastructure runbooks to support repeatable, auditable operations.

---

## Selected Projects

### Job Scout — Local-First AI Job Matching & Resume Optimization Tool

- Designed and delivered local-first AI application normalizing resume and LinkedIn data into structured candidate profiles, matching against live job postings via MCP-based integrations.
- Implemented explainable, spec-driven ranking pipelines deterministically scoring roles across skill overlap, seniority alignment, constraints, and posting freshness with user-adjustable weighting.
- Built AI-assisted search evaluation framework measuring keyword effectiveness, surfacing work arrangement distributions, and enabling side-by-side comparison of multiple resume profiles.
- Designed cost-aware LLM orchestration by dynamically limiting ranking operations based on user-selected scope, preventing excessive API usage while preserving functionality.

---

## Mentoring & Leadership

### SCRIPT CLUB
**Career Coach / Mentor** | January 2021 - Present | Remote

- Lead weekly mentorship office hours and developed curriculum covering cloud fundamentals, IaC, and career strategy, supporting engineers transitioning into DevOps, cloud, and software roles.
- Provided resume reviews, mock interviews, and career coaching, helping 20+ professionals secure roles across DevOps, software, and cloud engineering.
- Co-managed mentorship community serving up to 150 participants, including curriculum guidance and resource coordination.
