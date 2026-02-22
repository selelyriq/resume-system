# Resume Versioning & Interview Positioning System

A Git-based resume versioning system that maintains a canonical primary resume while supporting multiple positioned variants aligned to different career trajectories. Includes integrated interview preparation, technical refresh notes, and story libraries with YAML-tagged cross-positioning.

## Overview

This system ensures consistency between:
- **Resume positioning** (what you emphasize for different roles)
- **Interview narrative** (the stories you tell and how you frame them)
- **Technical prep focus** (what to study based on positioning)

Think of your resume like a software product: it evolves intentionally through versions, has multiple branches for different use cases, and ships with comprehensive documentation.

## Quick Start

### Check Your Current Positioning

```bash
git branch -a
```

You're on `main` if you see `* main`. This is Platform Engineering focus.

### Switch to Different Positioning

```bash
git checkout automation-devops      # for DevOps/Automation roles
git checkout security-enterprise    # for Security/Enterprise roles
git checkout ai-infra               # for AI Systems Engineering roles
git checkout main                   # back to Platform Engineering
```

### View Your Resume

```bash
cat resume/main/resume.md           # Full resume
cat resume/main/summary.md          # Your positioning pitch (changes per branch)
cat resume/main/highlights.md       # Key impact bullets (reordered per branch)
```

### Prepare for an Interview

1. **Understand the positioning**: `cat positioning/<identity>-identity.md`
2. **Study technical prep**: `cat prep/<positioning>-deep-dive.md`
3. **Prepare stories**: Read stories in `stories/*.md`, focus on relevant ones
4. **Practice interview answers**: `cat prep/common-interview-questions.md`

## Repository Structure

```
resume-system/
├── resume/
│   └── main/
│       ├── resume.md              # Canonical resume (Markdown source)
│       ├── summary.md             # Positioning-customizable pitch
│       └── highlights.md          # Reorderable impact bullets
│
├── positioning/
│   ├── platform-identity.md       # Platform engineering identity definition
│   ├── automation-identity.md     # DevOps/Automation identity
│   ├── security-identity.md       # Security/Enterprise identity
│   └── ai-infra-identity.md       # AI Infrastructure identity
│
├── stories/
│   ├── terraform-state-isolation.md           # Blast radius & modularity
│   ├── github-enterprise-migration.md         # Large-scale migrations
│   ├── internal-developer-platform.md         # Developer experience
│   ├── cloud-cutover.md                       # High-stakes infrastructure
│   ├── kubernetes-deployment.md               # Deployment scale & reliability
│   ├── cost-aware-llm.md                      # AI systems & cost control
│   └── failure-lessons.md                     # Learning & evolution
│
├── prep/
│   ├── platform-deep-dive.md                  # Multi-account, state management, architecture
│   ├── automation-devops.md                   # CI/CD, GitOps, drift detection
│   ├── security-enterprise.md                 # IAM, compliance, incident response
│   ├── ai-infra.md                            # ML systems, feature stores, observability
│   └── common-interview-questions.md          # Universal interview prep
│
├── .github/workflows/
│   └── build-pdf.yml               # Pandoc pipeline: Markdown → PDF
│
├── POSITIONING-RULES.md            # Ethics guardrails (honesty > optimization)
├── CHANGELOG.md                    # Version history & release notes
├── INDEX.md                        # Cross-reference guide
├── README.md                       # This file
└── .gitignore
```

## Branches & Positioning

### main (Platform Engineering)
**Focus**: System design, infrastructure as a product, multi-account architecture, scalability
**Best for**: Infrastructure systems engineer, platform engineer roles
**Core narrative**: "I design scalable infrastructure systems that reduce operational and organizational risk."

### automation-devops
**Focus**: CI/CD, GitOps, eliminating manual toil, event-driven systems
**Best for**: DevOps engineer, cloud infrastructure engineer roles
**Core narrative**: "I eliminate operational friction through automation and event-driven systems."

### security-enterprise
**Focus**: IAM boundaries, blast radius minimization, compliance, risk reduction
**Best for**: Security engineer, enterprise cloud architect roles
**Core narrative**: "I design guardrails that reduce cloud misconfiguration and limit incident impact."

### ai-infra
**Focus**: ML workload infrastructure, data pipelines, cost optimization, model lifecycle
**Best for**: AI systems engineer, ML infrastructure engineer roles
**Core narrative**: "I build infrastructure systems that support production AI workloads."

## Using This System

### For Job Applications

1. Identify the role's primary focus (Platform? DevOps? Security? AI?)
2. Check out the corresponding branch
3. Review the positioning definition (`positioning/<identity>-identity.md`)
4. Review the technical prep guide (`prep/<positioning>-deep-dive.md`)
5. Your resume and position-specific materials are ready

### For Interview Preparation

1. **Days before**: Study positioning and technical deep-dive
2. **Day before**: Review your 3-5 anchor stories
3. **Day of**: Skim common-interview-questions with your positioning lens
4. **During**: Use STAR method (Situation, Task, Action, Result) for storytelling
5. **After**: Document what you learned, update stories if needed

### For Resume Updates

Core resume content changes rarely. Only update:
- Major project completion
- Significant achievement or metric
- Career evolution

When updating resume/main/resume.md on main, merge changes to other branches:
```bash
git commit -am "Update resume with new achievement"
git checkout automation-devops && git merge main
git checkout security-enterprise && git merge main
git checkout ai-infra && git merge main
```

## Key Files

### Must Read
- `POSITIONING-RULES.md` — Start here. Ethics and integrity guardrails.
- `positioning/<your-positioning>-identity.md` — Understand your focus
- `INDEX.md` — Navigate the system

### Interview Prep
- `prep/common-interview-questions.md` — Universal interview framework
- `prep/<positioning>-deep-dive.md` — Technical depth for your branch
- `stories/*.md` — Anchor stories (read ones tagged with your identity)

### Maintenance
- `CHANGELOG.md` — Version history
- `.github/workflows/build-pdf.yml` — PDF generation pipeline

## Generating PDFs

The Pandoc build pipeline automatically generates PDFs from Markdown source:

```bash
pandoc resume/main/resume.md -o resume.pdf
```

Or trigger the GitHub Actions workflow:
```bash
git push  # automatically builds PDF on push
```

## Versioning Strategy

Releases are tagged in Git:
- `v1.0-platform` — Platform engineering primary
- `v1.1-automation` — Automation DevOps emphasis
- `v2.0-ai-infra` — AI Infrastructure focus

See `CHANGELOG.md` for detailed release notes.

## Ethics & Integrity

**Positioning is about emphasis and framing, never fabrication.**

Read `POSITIONING-RULES.md` for complete guidelines:
- ✅ What is honest positioning (reorder, reframe, emphasize)
- ❌ What is not acceptable (fabricate, exaggerate, claim false ownership)
- How to adapt stories ethically
- Red lines you should never cross

## Long-Term Trajectory

Your career direction:
**Platform Engineering** → **AI Infrastructure** → **Artifact-based Freelance Systems**

Automation and security are tools. Platform thinking is core. Build toward this intentionally.

## Contributing

This system is yours to evolve:
- Add new stories as projects complete
- Update positioning as your focus shifts
- Refresh technical prep as you learn
- Version releases with Git tags
- Document lessons learned

## Support

Need help?
- Check `INDEX.md` for navigation and cross-references
- Review specific identity definition for positioning clarity
- Reread `POSITIONING-RULES.md` if in doubt about ethics
- Read through `prep/common-interview-questions.md` for interview prep structure

---

**Version**: v1.0-platform  
**Last updated**: 2026-02-22  
**Branches**: 4 active (main, automation-devops, security-enterprise, ai-infra)
