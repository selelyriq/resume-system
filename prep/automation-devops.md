---
positioning: automation
branch: automation-devops
---

# Automation & DevOps Deep Dive

## Core Services & Patterns

### GitHub Actions & CI/CD
- **Workflow structure**: Jobs, steps, actions, secrets management
- **Self-hosted runners**: When to use, security implications, scaling
- **OIDC federation**: Keyless authentication to cloud providers (AWS, Azure)
- **Matrix builds**: Testing across versions, platforms, configurations
- **Conditional execution**: Triggering jobs based on file changes, labels, branches

**Questions to drill**:
- How do you securely manage secrets in CI/CD?
- What's the difference between OIDC federation and long-lived credentials?
- How do you prevent CI/CD pipeline attacks (compromised dependencies, rogue PRs)?

### Infrastructure Drift & Reconciliation
- **Drift detection**: Running Terraform refresh to find out-of-band changes
- **Reconciliation strategies**: Auto-reconcile vs. alert-and-review
- **Configuration drift vs. state drift**: What they are, how they differ
- **Prevention**: Good automation prevents drift (immutable infrastructure, declarative deployments)

### Deterministic Deployments
- **Idempotency**: Applications/infrastructure should be safe to redeploy many times
- **Rollback strategy**: How to quickly revert to previous version
- **Canary deployments**: Gradually roll out changes, monitor for issues
- **Blue-green deployments**: Run two versions, switch traffic to new

### GitOps & ArgoCD
- **Declarative infrastructure**: "State" lives in Git, system works to match declaration
- **Pull-based vs. push-based**: ArgoCD uses pull model (safer, more observable)
- **Application synchronization**: ArgoCD reconciliation loop, detecting drift
- **Multi-environment management**: Kustomize overlays, Helm values per env

### Serverless Event-Driven Patterns
- **EventBridge**: Rules, buses, targets; routing based on event patterns
- **Lambda invocation**: Synchronous vs. async, error handling, retries
- **Event source mapping**: SQS to Lambda, Kinesis to Lambda
- **Idempotent processing**: Handling duplicate events, exactly-once guarantees

## Common Failure Modes

- **State corruption in CI/CD**: Race conditions with concurrent jobs, lock timeouts
- **Webhook security**: Unvalidated webhooks triggering unauthorized deployments
- **Credential leakage**: Secrets logged to build output, exposed in container images
- **Dependency vulnerabilities**: Using outdated or compromised actions/tools
- **Pipeline cascade failures**: One failed job blocking dependent jobs
- **Inconsistent drift detection**: Some resources drifting undetected
- **Rollback failures**: State divergence making rollback impossible or risky
- **Event duplicate processing**: Processing same event twice causing idempotency issues

## Key Tradeoffs

| Tradeoff | Option A | Option B | Best For |
|----------|----------|----------|----------|
| Monorepo vs. multi-repo | All code in one repo | Separate repos per component | Monorepo: easier orchestration; Multi: clear ownership |
| Push vs. pull CD | Push changes from CI | Pull changes via GitOps | Push: faster; Pull: safer, better auditability |
| Fan-out vs. serial jobs | Parallel job execution | Sequential job execution | Fan-out: speed; Serial: dependency control |
| Terraform state locking | Strict locking (slower) | Optimistic locking (faster, riskier) | Locking: multi-team safety; Optimistic: single-team speed |
| Self-hosted vs. managed runners | Self-hosted (control, cost) | Managed (simplicity) | Self-hosted: secrets, performance; Managed: simplicity |

## Interview Traps

1. **"How do you prevent CI/CD pipeline attacks?"** — Validate PR sources, scan dependencies, limit runaway resource usage, audit logs.
2. **"Should we use GitOps?"** — GitOps is great for declarative systems (infrastructure, Kubernetes). Less applicable to imperative processes.
3. **"How do we handle state file locks in concurrent deployments?"** — Terraform locking prevents corruption, but can cause timeouts. Understand timeouts and failure recovery.
4. **"Can we make deployments infinitely fast?"** — Testing and safety checks take time. There are limits to how fast you can safely deploy.
5. **"How do we handle secrets in containerized deployments?"** — Never bake secrets into images. Use runtime injection (Secrets Manager, OIDC).

## Deep Dive Topics

### Designing for Operator Confidence
- Automation should make humans more confident, not replace human judgment
- Clear logs and observability are critical
- Rollback procedures must be fast and reliable

### Scaling Automation Across Teams
- One team's automation can become another team's bottleneck
- How do you allow teams to own their own pipelines?
- What guardrails prevent chaos?

### Event-Driven Systems
- Events enable loose coupling and scale
- But they also create complex failure modes (duplicate processing, event loss)
- Understand exactly-once vs. at-least-once semantics
