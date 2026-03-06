# Platform Engineering Resume

This branch contains the **Platform Engineering** identity-tailored resume for Lyriq Davis.

**Core narrative**: "I build the foundation other engineers build on."

## What's on this branch

```
resume/main/
├── resume.md              # Platform Engineering tailored resume
└── highlights.md          # Platform Engineering key highlights

positioning/
└── platform-identity.md   # Identity definition, narrative, key stories, interview traps

prep/
├── platform-deep-dive.md       # Technical prep: state isolation, multi-account, IaC design
└── common-interview-questions.md
```

## PDF Output

Every push triggers the CI pipeline: Claude API → LaTeX → pdflatex → `Lyriq-Davis-Platform-Engineering.pdf`

## Interview Prep

```bash
# Read the positioning guide
cat positioning/platform-identity.md

# Read the technical prep
cat prep/platform-deep-dive.md

# Read a story with the platform lens
# (stories live on master — see: git show master:stories/internal-developer-platform.md)
```

**Priority stories for this identity** (read the Platform Engineering lens in each):
- `internal-developer-platform.md` — dev containers, onboarding, standardization
- `terraform-state-isolation.md` — blast radius, parallel team ownership
- `cloud-cutover.md` — risk-aware execution, operational reliability
- `github-enterprise-migration.md` — platform consolidation at scale
- `kubernetes-deployment.md` — deployment platform for application teams

## Updating this resume

New experience goes on `master` first, then gets reframed here with the platform lens.

See `master` branch `INDEX.md` for the full sync workflow.

---

**Identity**: Platform Engineering
**PDF**: `Lyriq-Davis-Platform-Engineering.pdf`
**Source of truth**: `master` branch
