# Positioning Rules & Ethics Guardrails

## Core Principles

This resume system is built on a foundation of **complete honesty and integrity**. Positioning is about emphasis and framing, not fabrication.

### What is Positioning?

- Reordering bullets to lead with relevant work
- Emphasizing aspects of a project that align with the target role
- Framing the same work from different angles (automation vs. platform vs. AI-infra)
- Highlighting experiences that match the interview focus
- Being strategic about which stories to tell

### What is NOT Positioning

- Fabricating experiences or projects
- Exaggerating impact metrics ("eliminated all toil" when it was partial)
- Claiming ownership of work done by colleagues
- Adding technical skills not actually used or learned
- Misleading about timeline or responsibility

---

## Specific Guardrails

### Metrics & Impact
- **Only cite metrics you directly influenced**. The 3x deployment speed improvement is real — you worked on it and measured it. Don't claim it as sole credit if it was a team effort.
- **Be specific about your role**. "Led implementation" vs. "contributed to" vs. "participated in" are different. Use the right one.
- **If unsure, qualify it**. "Helped reduce deployment failures by 60%" is more honest than implying sole responsibility.

### Skill Claims
- **Only claim skills you've actively used in production**. If you've read about ArgoCD but never deployed it, that's "familiar with" not "experienced in."
- **Distinguish depth**: "Experience with" vs. "expertise in" vs. "production use of" all mean different things.

### Work Ownership
- **Credit your team**. Infrastructure automation wins are usually team efforts. You were a critical part — say that, not more.
- **Don't claim what was collaborative**. If the migration succeeded because of your scripts AND your team's coordination, say so.

### Stories & Framing
- **Stories must be technically truthful**. You can frame the Terraform state isolation work as automation or platform — both are true. You can't say "designed novel CI/CD architecture from scratch" if you adopted existing patterns.
- **Adapt, don't invent**. Each story is a real experience; different positionings just emphasize different aspects.
- **Be prepared to go deep**. If you tell a story in an interview, you should be able to walk through the full technical implementation.

---

## Red Lines (Never Cross)

1. **Do not fabricate projects**. Never list a project you didn't work on.
2. **Do not exaggerate timelines**. If you automated something over 2 months, don't say 6.
3. **Do not claim skills you don't have**. "Expert Terraform operator" when you've only done basic modules is dangerous.
4. **Do not mislead about collaboration**. Own your role without diminishing your team's.
5. **Do not commit fraud**. Employers fact-check. Any fabrication will be discovered.

---

## Automation-Specific Framing: Honest Examples

### Same Project, Two Honest Frames

**The work**: Built Terraform state isolation with per-environment GitHub Actions pipelines

**Automation frame**: "Implemented per-environment CI/CD pipelines with isolated Terraform state backends, enabling independent deployments and removing cross-team deployment bottlenecks."

**Platform frame**: "Designed modular Terraform state architecture with team ownership boundaries, enabling parallel infrastructure delivery at scale."

Both are true. The automation frame leads with the pipeline and friction removal. The platform frame leads with the architecture and ownership model. Neither fabricates anything.

### Honest Impact Framing

**The work**: Helped reduce deployment times (team effort)

**Dishonest**: "Cut deployment time by 3x" (implies sole responsibility)

**Honest**: "Contributed to 3x deployment speed improvement by implementing Kubernetes orchestration and GitHub Actions CI/CD pipelines"

---

## Career Trajectory Integrity

Your long-term trajectory: **Infrastructure Automation → Platform Engineering → AI Infrastructure → Artifact-based Freelance Infra Systems**

This is honest and ambitious. Automation is not a stepping stone to dismiss — it's core infrastructure competency. Build on it with real skills.

---

## When in Doubt

- **Ask yourself**: Would I be comfortable discussing this in technical depth in an interview?
- **Apply the reverse test**: If the interviewer asks me to walk through this implementation, can I do it?
- **Check your instinct**: Does this feel like honest emphasis, or am I rationalizing?

If you're rationalizing, it's probably not okay.
