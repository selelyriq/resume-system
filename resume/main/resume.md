---
name: Lyriq Davis
contact: (419) 984-4884 | lyriqsele@gmail.com
---

## Summary
Cloud Engineer with 5+ years of experience building infrastructure for production AI and cloud-native systems. Deep hands-on expertise in serverless ML orchestration (AWS Lambda, Bedrock, Transcribe), cost-aware LLM pipeline design, and explainable AI ranking systems. Proven ability to integrate AI services into production workflows and deliver infrastructure that supports scalable, cost-controlled AI workloads.

---

## Education

**AWS Solutions Architect Associate** — March 2025
**AWS SysOps Associate** — February 2025
**Terraform Certified Associate** — September 2024

---

## Core Competencies & Skills

**Technical:**
AI Systems Engineering, LLM Orchestration, Cost-Aware AI Design, Explainable AI (XAI), Infrastructure as Code, Cloud Architecture, Kubernetes, CI/CD, Observability, Automation, Platform Engineering, Security & Compliance

**Technology Tools & Platforms:**
AWS (Bedrock, SageMaker, Lambda, Transcribe, S3, EC2, IAM, SSM, CloudWatch, ECS, EKS), Terraform, Python, OpenAI SDK, MCP, Streamlit, Databricks, Docker, Kubernetes, Helm, ArgoCD, GitHub Actions, Packer, Prometheus, Grafana, Azure (VNet, AKS, Private DNS, Private Link), SQL

---

## Experience

### General Electric Aerospace — via Capgemini
**Cloud Engineer** | August 2025 - Present | Cincinnati, OH

- Productized a standardized internal developer platform using VS Code Dev Containers and Makefile-driven workflows, eliminating environment drift and reducing onboarding time from 1–2 days to under 30 minutes across 6+ application teams.
- Executed a high-stakes cloud-to-cloud application migration supporting a mission-critical system processing ~$80M/day, orchestrating a three-hour maintenance window involving authentication-path cutover, AD/LDAP join/unjoin, DNS reconfiguration, and ALB certificate updates with zero downtime.
- Owned parallel identity and security initiatives by executing application role migration to centralized identity (IDC) and independently managing TLS certificate lifecycle using ACM and Secrets Manager, including new certificate issuance, secure storage of certificate material, and coordinated implementation across application teams and ALBs.

### University of Cincinnati
**Cloud Engineer** | January 2025 - August 2025 | Cincinnati, OH

- Designed and implemented Python-based automation (boto3, REST APIs) to orchestrate serverless workflows across AWS (Lambda, S3, SQS, Transcribe, Bedrock, API Gateway), enabling automated Teams transcript ingestion and AI-driven summarization.
- Built reusable, idempotent Terraform modules to standardize AWS and Azure infrastructure (networking, compute, IAM, observability), integrating plan/apply validation gates within GitHub-based CI/CD workflows.
- Deployed observability tooling (Prometheus, Grafana, Alloy, CloudWatch dashboards) to implement structured logging, metrics, and alerting for infrastructure and automation workflows.
- Implemented GitHub Actions and ArgoCD GitOps pipelines with branching strategies, pull-request reviews, automated chart validation, and container scanning to ensure safe, versioned infrastructure and application changes.
- Architected Terraform state isolation strategy by separating infrastructure into logically scoped state files and repositories (networking, shared services, application stacks) segmented by account and environment, minimizing blast radius and enabling safer, auditable change workflows.
- Partnered with security leadership to assess and remediate Security Hub findings, removing public S3 exposure, enforcing least-privilege IAM, and restricting open security groups, improving cloud security posture.

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

- Designed and delivered a local-first AI application that normalizes resume and LinkedIn data into structured candidate profiles and matches them against live job postings via MCP-based integrations.
- Implemented explainable, spec-driven ranking pipelines that deterministically score roles across skill overlap, seniority alignment, constraints, and posting freshness, with user-adjustable weighting.
- Built an AI-assisted search evaluation framework that measures keyword effectiveness across job results, surfaces work arrangement distributions, and enables side-by-side comparison of multiple resume profiles.
- Designed cost-aware LLM orchestration by dynamically limiting ranking operations based on user-selected scope, preventing excessive API usage while preserving functionality; defaulted to conservative thresholds to protect users from runaway costs.

---

## Mentoring & Leadership

### SCRIPT CLUB
**Career Coach / Mentor** | January 2021 - Present | Remote

- Lead weekly mentorship office hours and developed curriculum covering cloud fundamentals, IaC, and career strategy, supporting engineers transitioning into DevOps, cloud, and software roles.
- Provided resume reviews, mock interviews, and career coaching, helping 20+ professionals secure roles across DevOps, software, and cloud engineering.
- Co-managed a mentorship community serving up to 150 participants, including curriculum guidance and resource coordination.
