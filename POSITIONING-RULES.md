# Positioning Rules & Ethics Guardrails

## Core Principles

This resume system is built on a foundation of **complete honesty and integrity**. Positioning is about emphasis and framing, not fabrication.

### What is Positioning?

- Reordering bullets to lead with relevant work
- Emphasizing aspects of a project that align with the target role
- Framing the same work from different angles (AI-infra vs. automation vs. platform)
- Highlighting experiences that match the interview focus
- Being strategic about which stories to tell

### What is NOT Positioning

- Fabricating experiences or projects
- Exaggerating impact metrics ("production AI system" when it was a prototype)
- Claiming ownership of work done by colleagues
- Adding technical skills not actually used or learned
- Misleading about timeline or responsibility

---

## Specific Guardrails

### Metrics & Impact
- **Only cite metrics you directly influenced**. The serverless AI pipeline you built at UC — that's yours. The $80M/day cutover? That's the system's throughput, which you helped migrate, not your personal impact.
- **Be specific about your role**. "Designed and built" vs. "contributed to" vs. "helped integrate" are different. Use the right one.
- **If unsure, qualify it**. "Built an internal AI pipeline processing Teams meeting audio" is accurate. "Built a production AI platform" overstates it.

### Skill Claims
- **Only claim skills you've actively used**. Bedrock, Transcribe, Lambda orchestration — you built with these. SageMaker — understand it and have used it. Don't upgrade "familiar with" to "expert in."
- **Distinguish depth**: "Built with" vs. "deployed to production" vs. "familiar with the API" all mean different things.

### Work Ownership
- **Credit your team and context**. The UC AI pipeline was a project you built. The GE dev platform was a team effort you led key parts of. Be accurate about scope.
- **Don't claim what was collaborative**. If a model integration worked because of your pipeline design AND your team's testing, say so.

### Stories & Framing
- **Stories must be technically truthful**. You can frame the Terraform state isolation work as AI-infra (foundation for ML workload environments) — that's a legitimate lens. You can't say "designed ML infrastructure platform" if it was general IaC work.
- **Adapt, don't invent**. Each story is a real experience; different positionings just emphasize different aspects.
- **Be prepared to go deep**. If you tell a story about Bedrock/Transcribe orchestration, you should be able to walk through the Lambda trigger patterns, async execution, retry logic, and cost controls.

---

## Red Lines (Never Cross)

1. **Do not fabricate projects**. Never list an AI/ML project you didn't work on.
2. **Do not exaggerate scale**. "Internal tooling for a team" is not "enterprise AI platform."
3. **Do not claim ML expertise you don't have**. Infra for AI workloads ≠ ML research or model training expertise.
4. **Do not mislead about collaboration**. Own your role without diminishing your team's.
5. **Do not commit fraud**. Employers in AI/ML often have strong technical interviewers who will go deep. Any fabrication will surface.

---

## AI/ML Infra Framing: Honest Examples

### Same Project, Two Honest Frames

**The work**: Built serverless pipeline with Lambda, Bedrock, and Transcribe to process Teams meeting recordings

**AI-infra frame**: "Designed and built a serverless AI orchestration pipeline using AWS Lambda, Bedrock, and Transcribe — processing meeting audio into structured summaries with zero standing infrastructure and per-execution cost model."

**Automation frame**: "Built event-driven Lambda pipeline that automatically processes uploaded audio files through AWS AI services, eliminating manual transcription and summarization workflows."

Both are true. The AI-infra frame leads with the system design and AI services. The automation frame leads with the event-driven pattern and toil elimination. Neither fabricates anything.

### Honest Scale Framing

**The work**: Built internal AI tooling for a university team

**Dishonest**: "Built production AI platform serving enterprise users"

**Honest**: "Built internal serverless AI pipeline for research team, processing meeting recordings using AWS Bedrock and Transcribe with automated summarization"

---

## Career Trajectory Integrity

Your long-term trajectory: **Infrastructure Automation → Platform Engineering → AI Infrastructure → Artifact-based Freelance Infra Systems**

AI infrastructure is the destination, not a fabricated shortcut. Build on real experience with Bedrock, Transcribe, Lambda orchestration, and cost-aware AI systems — not on hypotheticals.

---

## When in Doubt

- **Ask yourself**: Could I whiteboard this system design in an interview?
- **Apply the reverse test**: If a senior ML engineer asks me to walk through this implementation, can I do it?
- **Check your instinct**: Is this honest emphasis of real work, or am I inflating it?

If you're inflating, dial it back.
