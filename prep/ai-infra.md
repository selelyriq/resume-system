---
positioning: ai-infra
branch: ai-infra
---

# AI Infrastructure Deep Dive

## Core Services & Patterns

### LLM Deployment & Inference
- **Prompt engineering**: Designing prompts for consistent output
- **Model selection**: Base vs. fine-tuned vs. specialized models
- **API-based inference**: OpenAI, Anthropic, Bedrock (latency, cost, rate limits)
- **Self-hosted inference**: TensorFlow Serving, Triton, vLLM (control, cost, complexity)
- **Batch vs. real-time**: When to use each for different workload patterns

**Questions to drill**:
- How do you optimize cost for LLM API calls?
- What's the tradeoff between self-hosted vs. API-based inference?
- How do you handle rate limits and quota management?

### Model Lifecycle & Versioning
- **Model registry**: Storing model artifacts, versions, metadata
- **Training pipelines**: Data preparation, training, evaluation, artifacts
- **Model versioning**: How to track which model is deployed where
- **A/B testing**: Running multiple models in production, measuring performance
- **Rollback**: Reverting to previous model version

### Feature Stores & Data Pipelines
- **Feature engineering**: Creating meaningful features from raw data
- **Feature store**: Centralized feature repository (Tecton, Feast)
- **Data pipelines**: ETL/ELT, data quality checks, freshness guarantees
- **Training/serving consistency**: Ensuring features computed same way at train and serve time
- **Data versioning**: Tracking which data was used for training

### ML Observability
- **Model performance**: Accuracy, precision, recall, F1 score
- **Data drift**: Input data distribution changing over time
- **Model drift**: Model performance degrading due to data drift or concept drift
- **Feature importance**: Understanding which features drive predictions
- **Prediction traceability**: Understanding why a specific prediction was made

### Cost Optimization for ML
- **API call budgeting**: Limiting spending on external LLM APIs
- **Inference optimization**: Caching, batching, quantization to reduce cost
- **Data pipeline efficiency**: Avoiding redundant computation, storing intermediate results
- **GPU utilization**: Right-sizing instance types, spot instances for non-critical workloads

## Common Failure Modes

- **Model staleness**: Running models trained months ago on outdated data
- **Training/serving skew**: Features computed differently at train vs. serve time
- **Data leakage**: Training data leaking into test set, overestimating performance
- **Unmonitored drift**: Model performance degrading silently until users notice
- **Cost explosion**: Uncontrolled API calls or excessive inference incurring massive bills
- **Batch job failures**: Data pipelines failing silently, stale data in production
- **Low-quality training data**: Poor data quality leading to poor model quality
- **Lack of fallback**: No graceful degradation when model serving fails

## Key Tradeoffs

| Tradeoff | Option A | Option B | Best For |
|----------|----------|----------|----------|
| API-based vs. self-hosted | Bedrock/OpenAI (managed) | Self-hosted TensorFlow Serving (control) | API: simplicity, managed; Self-hosted: cost at scale, control |
| Batch vs. real-time inference | Compute once, serve results | Compute on-demand | Batch: cost-effective, latency acceptable; Real-time: low latency required |
| Fine-tuned vs. prompt engineering | Train custom model (cost, time) | Engineer prompts (faster, less cost) | Fine-tuned: specific domain, performance critical; Prompting: rapid iteration |
| Centralized feature store vs. ad-hoc features | Feature store (consistency, reuse) | Features computed at serve time (simpler) | Centralized: multiple models, consistency; Ad-hoc: simple features |
| Frequent retraining vs. periodic | Retrain when drift detected | Scheduled retraining (weekly/monthly) | Frequent: evolving/fast-changing data; Periodic: stable data |

## Interview Traps

1. **"How do you detect model drift?"** — Monitor model performance metrics. Compare current predictions to historical distribution. Track data drift as leading indicator.
2. **"Should we fine-tune or prompt engineer?"** — Start with prompting. Move to fine-tuning if prompting doesn't meet accuracy requirements.
3. **"How do we handle LLM hallucinations?"** — Retrieval-augmented generation (RAG) grounds LLM in real data. Use LLMs for reasoning, not as source of truth.
4. **"What's the difference between data drift and model drift?"** — Data drift: input distribution changes. Model drift: model performance degrades (can be caused by data drift).
5. **"How do we ensure reproducibility?"** — Version data, code, model, hyperparameters. Store all in artifacts/registry.

## Deep Dive Topics

### Designing for Cost Awareness
- Every LLM call is a cost decision
- Design systems to minimize unnecessary calls
- Educate users about cost implications

### ML Systems Reliability
- Models are more fragile than traditional software
- Require monitoring, retraining, versioning
- Need strong fallbacks and graceful degradation

### Data Quality in ML
- "Garbage in, garbage out"
- Invest in data validation and quality checks
- Understand your data distribution

### Model Interpretability
- Opaque models are dangerous in production
- Use SHAP, LIME, or attention visualizations
- Users need to understand why they got a prediction
