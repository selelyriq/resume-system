# Changelog

## [v2.0] - 2026-03-06

### Changed
- **Rebuilt branch structure**: Replaced main/automation-devops/security-enterprise/ai-infra with master/platform-engineering/infra-automation/ai-ml-infra
- **Introduced `master` as internal source of truth**: Generic resume, all positioning docs, all stories — not public-facing
- **Removed security identity**: Branch deleted, files removed from all branches
- **Upgraded PDF pipeline**: Replaced Pandoc with Claude API → LaTeX → pdflatex pipeline
- **Named PDF outputs**: Each identity branch now produces an identity-named PDF instead of a generic filename
  - `Lyriq-Davis-Platform-Engineering.pdf`
  - `Lyriq-Davis-Infra-Automation.pdf`
  - `Lyriq-Davis-AI-ML-Infra.pdf`

### Added
- **Identity-tailored resumes**: Each branch has fully rewritten resume.md and highlights.md with identity-specific framing, not just reordered bullets
- **New story**: `serverless-ai-pipeline.md` — UC Bedrock/Transcribe AI orchestration pipeline
- **Identity lenses on all stories**: Every story now has a **Result by Identity** section covering all three active identities
- **Prep files scoped per branch**: Each identity branch carries only its own prep file and common-interview-questions.md

### Removed
- Security identity positioning and prep files
- `security-enterprise` branch
- Generic Pandoc pipeline

---

## [v1.0] - 2026-02-22

### Added
- Initial release with 4 branches: main (platform), automation-devops, security-enterprise, ai-infra
- 7 anchor stories with YAML frontmatter identity tagging
- Technical prep deep-dives for each identity
- Common interview questions with STAR framework
- Positioning rules and ethics guardrails
- Pandoc PDF build pipeline
