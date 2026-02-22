---
positioning: multi
tags: [interview-prep, cross-positioning]
---

# Common Interview Questions & Positioning-Aware Answers

## System Design & Architecture

### Q: Design a scalable infrastructure for a SaaS application

**Universal foundation**:
- Multi-region, multi-AZ for high availability
- Load balancing and auto-scaling
- Persistent storage (managed database)
- Caching layer (Redis)
- CDN for static content
- Monitoring and alerting

**Platform lens**: Emphasize modularity, reusability, blast radius isolation, state isolation strategy
**Automation lens**: Emphasize GitOps, CI/CD, infrastructure as code, drift detection
**Security lens**: Emphasize IAM boundaries, encryption, network isolation, least privilege
**AI-infra lens**: Add feature store, model versioning, data pipeline, cost tracking

### Q: How do you handle database scaling?

**Universal foundation**:
- Read replicas for read-heavy workloads
- Sharding for write-heavy workloads
- Backup and disaster recovery strategy

**Platform lens**: How does choice affect blast radius? Multi-account implications?
**Automation lens**: How do you automate failover? Drift detection for replicas?
**Security lens**: How do you isolate data? Encryption keys?
**AI-infra lens**: Feature store access patterns? Model serving query efficiency?

## Distributed Systems

### Q: Design a safe deployment system

**Platform lens**: Focus on state isolation, rollback safety, blast radius minimization
**Automation lens**: Focus on GitOps, drift reconciliation, deterministic deployments
**Security lens**: Focus on least privilege for deployment service, audit trails
**AI-infra lens**: Consider model serving aspects, gradual rollouts, A/B testing

### Q: How do you handle eventual consistency?

**Discuss**:
- Idempotency (same operation multiple times = same result)
- Conflict resolution strategies
- Data consistency levels (strong vs. eventual)
- Monitoring for divergence

## Disasters & Recovery

### Q: Your production database is corrupted. What do you do?

1. **Immediate**: Stop applications from writing corrupted data
2. **Assessment**: Determine scope (which data? how long ago?)
3. **Recovery**: Restore from backup, determine recovery point
4. **Validation**: Verify restored data integrity
5. **Lessons learned**: How to prevent next time

**Add by lens**:
- **Platform**: How does your blast radius strategy help isolate the issue?
- **Automation**: How do you automate failover and recovery?
- **Security**: Who has access to backups? How are they encrypted?
- **AI-infra**: Can you recover training data? Model artifacts?

### Q: How do you prevent cascading failures?

**Design patterns**:
- Circuit breakers (fail fast, don't retry forever)
- Bulkheads (isolate failures to specific components)
- Timeouts (don't wait for failed services)
- Graceful degradation (serve less than full functionality rather than fail entirely)

## Incident Response

### Q: Tell me about a production incident you handled

**Structure (STAR)**:
- **Situation**: What broke, when, impact
- **Task**: What was your responsibility
- **Action**: What did you do step-by-step
- **Result**: How did you fix it, what did you learn

**Add by lens**:
- **Platform**: What could you have designed differently to prevent this?
- **Automation**: How would automation have caught this earlier?
- **Security**: Was there a security component? Could it happen again?
- **AI-infra**: How does this apply to ML systems?

## Concurrency & Race Conditions

### Q: How do you prevent race conditions in infrastructure changes?

**Terraform**: State file locking (DynamoDB), remote backend coordination
**Databases**: Optimistic vs. pessimistic locking
**Distributed systems**: Consensus algorithms (Raft, Paxos)
**Events**: Idempotency tokens, deduplication

## Cost & Efficiency

### Q: How do you optimize cloud costs?

**Areas**:
- Right-sizing (instances, databases, storage)
- Reserved/spot instances
- Autoscaling down when not needed
- Data transfer costs (minimize cross-region, cross-AZ)
- Storage tiering (hot/warm/cold data)

**AI-infra addition**: API call budgeting, inference optimization, data pipeline efficiency

## Leadership & Communication

### Q: Tell me about a time you mentored someone

**Discuss**:
- Who: role, background, what were they learning
- Challenge: what did they struggle with
- How you helped: code reviews, pair programming, resources
- Result: what did they learn, where are they now

**For SCRIPT CLUB mentorship**: 20+ career placements, curriculum design, community management

## Technical Depth by Positioning

### Platform
- How do you scale to 100 teams? 1000 teams?
- What breaks when you grow?
- How do you keep infrastructure safe at massive scale?

### Automation
- How do you prevent CI/CD supply chain attacks?
- GitOps vs. traditional CD—when does each make sense?
- How do you test infrastructure changes safely?

### Security
- Walk me through your IAM model
- How do you audit access at scale?
- What's your blast radius strategy?

### AI-Infra
- How do you detect when an ML model is degrading?
- What's your strategy for cost control in ML systems?
- How do you ensure reproducibility in ML pipelines?

## Generic Preparation Tips

1. **Practice the STAR method**: Situation, Task, Action, Result. Spend 30-45 seconds on setup, most time on action and result.
2. **Prepare 3-5 strong stories**: Varied (success, failure, leadership, system design) so you can adapt to different questions.
3. **Know your positioning**: Be consistent about what you emphasize. Platform engineers emphasize different things than DevOps engineers.
4. **Prepare for follow-ups**: "How would you do this differently?" "What did you learn?" "What would you do next time?"
5. **Show your thinking**: Walk through your reasoning, not just the conclusion. Interviewers want to see how you think.
