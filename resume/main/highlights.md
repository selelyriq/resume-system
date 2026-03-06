---
positioning: ai-ml-infra
branch: ai-ml-infra
---

# Key Highlights

## Impact & Outcomes

- **Built serverless AI orchestration pipeline** using AWS Lambda, Transcribe, Bedrock, and SQS to automate Teams transcript ingestion and AI-driven summarization, replacing manual processes with event-driven ML workflows.
- **Designed cost-aware LLM orchestration** in Job Scout, dynamically limiting ranking operations based on user-selected scope to prevent runaway API costs while preserving functionality; defaulted to conservative thresholds.
- **Implemented explainable, spec-driven AI ranking pipelines** that deterministically score job roles across skill overlap, seniority alignment, constraints, and posting freshness with user-adjustable weighting — fully auditable, no black-box decisions.
- **Architected local-first AI application** (Job Scout) making intelligent use of local vs. cloud inference based on scope and cost constraints, with MCP-based integrations for live job data.
- **Led $80M/day mission-critical cloud migration**: Coordinated high-risk cutover (authentication, DNS, ALB certs) during 3-hour maintenance window, achieving seamless continuity with zero downtime.
- **Productized internal developer platform** using VS Code Dev Containers and Makefile workflows, reducing team onboarding from 1–2 days to 30 minutes across 6+ application teams.
- **Deployed observability standards** (Prometheus, Grafana, CloudWatch) establishing structured logging, metrics, and alerting across infrastructure and automation workflows.
- **Improved deployment speed by 3x, reduced failure rate by 60%** through Kubernetes orchestration and GitHub Actions CI/CD automation.

## Technical Depth

- **AI & ML Infrastructure**: AWS Bedrock, SageMaker, Lambda, Transcribe — serverless ML orchestration, AI-driven document processing, cost-aware LLM pipeline design
- **AI Application Design**: LLM orchestration, explainable ranking pipelines, local vs. cloud inference tradeoffs, MCP integrations, OpenAI SDK, Streamlit
- **Infrastructure as Code**: Terraform (state management, modules, multi-account design)
- **Cloud Platforms**: AWS (Bedrock, SageMaker, Lambda, Transcribe, S3, EC2, IAM, ECS, EKS, CloudWatch), Azure (VNet, AKS, Private Link)
- **DevOps & Automation**: GitHub Actions, ArgoCD, CI/CD pipelines, Ansible, Docker, Kubernetes
- **Observability**: Prometheus, Grafana, CloudWatch, structured logging
- **Security & Compliance**: IAM design, least-privilege enforcement, TLS lifecycle management, Security Hub remediation
- **Languages**: Python (boto3, automation scripts), SQL, Bash
