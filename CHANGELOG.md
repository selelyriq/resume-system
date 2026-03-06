# Changelog — infra-automation

Branch-specific change history. For full system history, see `master` branch `CHANGELOG.md`.

---

## [v2.0] — 2026-03-06

### Changed
- **Resume tailored for infra-automation identity**: Summary, skills ordering, and bullet emphasis rewritten to lead with CI/CD, GitOps, and IaC automation
- **highlights.md reordered**: Automation impact stories front and center (Terraform pipeline, migration automation, Kubernetes GitOps)
- **Branch cleanup**: Removed non-automation positioning files (`platform-identity.md`, `ai-infra-identity.md`) and non-relevant prep files
- **Stories updated**: All 8 stories rewritten with identity-specific lenses, including new `serverless-ai-pipeline.md`
- **PDF pipeline fixed**: Branch triggers updated from old names (`automation-devops`) to `infra-automation`; output renamed to `Lyriq-Davis-Infra-Automation.pdf`
- **Docs overhauled**: README, INDEX, CHANGELOG, POSITIONING-RULES all updated to reflect current state

### Pipeline
```
push to infra-automation → GitHub Actions → Claude API (LaTeX) → pdflatex → Lyriq-Davis-Infra-Automation.pdf
```

---

## [v1.0] — 2026-02-22

### Added
- Initial branch from original `automation-devops` branch
- Automation-focused positioning definition
- CI/CD and GitOps technical prep
- Automation-tagged stories from story library
