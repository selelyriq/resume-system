# Lyriq Davis
**Cloud Infrastructure & AI Systems Engineer**

---
## Summary
Cloud Engineer with 5+ years of experience specializing in DevOps, Infrastructure as Code (Terraform), and
multicloud environments (AWS, Azure). Proven expertise in leading large-scale migrations, implementing robust
CI/CD and GitOps workflows (GitHub Actions, ArgoCD), managing Kubernetes/containerized services, and restoring
mission-critical application access through comprehensive identity-chain diagnosis. Highly proficient in automating
infrastructure, reducing deployment times, and standardizing developer platforms for increased efficiency.
---

## Education

**University of Cincinnati** — *Bachelors of Arts - Media Production* — Expected May 2026
**AWS Solutions Architect Associate** — March 2025
**AWS SysOps Associate** — February 2025
**Terraform Certified Associate** — September 2024

---

## Core Competencies & Skills

**Technical:**
Automation, Infrastructure as Code, Kubernetes, Cloud Architecture, CI/CD, Observability, Platform Engineering, AI Systems Engineering, Security & Compliance, Explainable AI (XAI), LLM Orchestration, Cost-Aware AI Design

**Technology Tools & Platforms:**
Terraform, AWS (EC2, S3, IAM, SSM, CloudWatch, ECS, EKS, Bedrock), Azure (VNet, AKS, Private DNS, Private Link), Docker, Kubernetes, Helm, ArgoCD, GitHub Actions, Packer, Prometheus, Grafana, Python, SQL, PySpark, Databricks, OpenAI SDK, LangGraph, CrewAI, MCP, Streamlit

---

## Experience

### General Electric Aerospace — via Capgemini
**Cloud Engineer** | August 2025 - Present | Cincinnati, OH

- Led large-scale GitHub Enterprise → GitHub SaaS migration of 400+ repositories, coordinating with application owners and repo stakeholders for planning and executing repository moves, deprecations, and archival workflows.
- Executed high-risk cloud-to-cloud application migration (cutover + AD/LDAP join/unjoin) for mission-critical system processing ~$80M/day. Implemented authentication-path and DNS changes, coordinated ALB cert updates during three-hour maintenance window to ensure seamless continuity.
- Owned parallel identity and security initiatives by executing application role migration to centralized identity (IDC), independently managing TLS certificate lifecycle (ACM, Secrets Manager), including issuance, secure storage, and coordinated implementation across application teams and ALBs.
- Diagnosed and resolved enterprise identity-chain failures across AD/LDAP, Saviynt, CyberArk, OIDC, and ALB auth flows, restoring access for mission-critical GE Aerospace applications.
- Productized standardized internal developer platform using VS Code Dev Containers and Makefile-driven workflows, eliminating environment drift and reducing onboarding time from 1-2 days to under 30 minutes across 6+ application teams.

### University of Cincinnati
**Cloud Engineer** | January 2025 - August 2025 | Cincinnati, OH

- Built and maintained Kubernetes environments across Azure and AWS, developing Helm charts to deploy
microservices and internal AI/ML workloads with consistency and reproducibility.
- Implemented GitOps workflows using ArgoCD and GitHub Actions, enabling declarative deployments,
automated chart validation, container scanning, and reliable promotion pipelines.
- Deployed observability tooling (Prometheus, Grafana, Alloy) and Terraform-driven CloudWatch dashboards
to unify metrics, logs, and alerting across EC2, AKS, and containerized services.
- Supported data engineering initiatives by integrating Snowflake and Informatica pipelines with AWS
workloads, improving pipeline reliability and enabling secure cloud-native analytics.
- Automated multicloud image builds using Packer + GitHub Actions and provisioned enterprise-grade RHEL
systems through Red Hat Hybrid Cloud Console to streamline environment setup.

### Tartan Builders
**Cloud Engineer** | October 2022 - December 2024 | Dublin, OH

- Built Ansible playbooks and templated configurations to manage CloudWatch Agent settings on golden AMI EC2 instances, enforcing standardized logging/metrics baselines and enabling repeatable, idempotent configuration updates.
- Developed Dockerfiles for container image creation, orchestrating containers with Kubernetes to support production operations, improving deployment speed by 3x and reducing deployment failure rate by 60%.
- Utilized Python scripts to automate EC2 uptime management aligned with work hours to reduce deployment costs.
- Utilized GitHub Actions, Docker, and ECR to establish CI/CD pipelines, automating build and deployment for web applications running in AWS, resulting in 50% increase in deployment speed and 75% improvement in code quality through automated testing.

### Obsidian Productions
**Digital Solutions Specialist** | June 2020 - June 2022 | Mansfield, OH

- Initialized GitHub repositories for secure source code management.
- Deployed and configured S3 buckets for static web hosting.
- Leveraged CodePipeline to automate deployment of applications from GitHub to S3 buckets.
- Maintained comprehensive documentation of work processes, customizations, and modifications.

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

- Lead weekly mentorship office hours with engineering team, supporting individuals transitioning into IT and cloud roles.
- Provided resume reviews, mock interviews, and career coaching, helping 20+ professionals secure roles across DevOps, software, and cloud engineering.
- Co-managed mentorship community serving up to 150 participants, including curriculum guidance and resource coordination.
