# Changelog — ai-ml-infra

Branch-specific change history. For full system history, see `master` branch `CHANGELOG.md`.

---

## [v2.0] — 2026-03-06

### Changed
- **Resume tailored for ai-ml-infra identity**: Summary, skills ordering, and bullet emphasis rewritten to lead with AI services (Bedrock, Transcribe, SageMaker), serverless pipelines, and ML infrastructure
- **highlights.md reordered**: AI/ML impact stories front and center (serverless AI pipeline, cost-aware LLM, ML dev environments)
- **Branch cleanup**: Removed non-AI-infra positioning files (`platform-identity.md`, `automation-identity.md`) and non-relevant prep files
- **Stories updated**: All 8 stories rewritten with identity-specific lenses, including new `serverless-ai-pipeline.md` — the primary AI story for this identity
- **PDF pipeline fixed**: Branch triggers updated from old names (`ai-infra`) to `ai-ml-infra`; output renamed to `Lyriq-Davis-AI-ML-Infra.pdf`
- **Docs overhauled**: README, INDEX, CHANGELOG, POSITIONING-RULES all updated to reflect current state

### Pipeline
```
push to ai-ml-infra → GitHub Actions → Claude API (LaTeX) → pdflatex → Lyriq-Davis-AI-ML-Infra.pdf
```

---

## [v1.0] — 2026-02-22

### Added
- Initial branch from original `ai-infra` branch
- AI Infrastructure positioning definition
- LLM deployment and ML systems technical prep
- AI-infra-tagged stories from story library
