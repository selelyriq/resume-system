---
identity: ai-infra
branch: ai-infra
active: true
---

# AI Infrastructure Identity

## Focus Areas

- ML workload deployment and orchestration
- Model lifecycle and versioning infrastructure
- Data pipeline and feature store architecture
- Data parallel and model parallel training infrastructure
- Scalable development environments for ML teams
- Cross-cloud AI architecture (AWS Bedrock, SageMaker, Azure ML)
- Cost optimization for ML workloads
- Observability for ML systems

## Core Narrative

**I build infrastructure systems that support production AI workloads.**

As AI becomes central to product, the systems that support it—from training environments to model serving, from feature stores to cost control—become critical infrastructure challenges.

## Key Stories

- **Cost-Aware LLM Orchestration**: Designed and implemented intelligent cost-limiting in Job Scout LLM ranking to prevent runaway API costs while preserving functionality
- **Explainable AI Pipeline Infrastructure**: Built deterministic ranking pipelines with configurable weighting, enabling transparent, debuggable ML decisions
- **Serverless ML Orchestration**: Designed AWS Lambda + Textract + Bedrock workflows for automated document processing and ML-driven summarization
- **Local-First ML Application**: Architected Job Scout to make intelligent use of local vs. cloud inference based on scope and cost constraints

## Technical Refresh

Services: AWS SageMaker, Bedrock, Textract, Azure ML, model serving (TensorFlow Serving, Triton), vector databases (Pinecone, Weaviate), feature stores (Tecton)

Failure modes: Model staleness, training/serving skew, data pipeline failures, cost explosion during inference, unmonitored ML degradation

Tradeoffs: Local vs. cloud inference, batch vs. real-time serving, monolithic vs. microservice model architecture, fine-tuning vs. prompting

Common interview traps: How do you version models? How do you detect ML model degradation? How do you handle data distribution shift?
