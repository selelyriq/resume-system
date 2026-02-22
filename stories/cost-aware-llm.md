---
title: "Cost-Aware LLM Orchestration"
identities: [ai-infra]
characters: ["Job Scout"]
tags: [llm, cost-optimization, intelligent-defaults, user-protection]
---

# Cost-Aware LLM Orchestration

## Context

Job Scout is a local-first AI application that matches job postings against candidate profiles using LLM-based ranking. The challenge: LLM API calls are expensive, and users might not realize how much they're spending.

## Challenge

- **Cost explosion**: Without guardrails, users could accidentally run expensive ranking operations on thousands of jobs
- **User trust**: If users incur unexpected costs, they'll stop using the product
- **Feature trade-off**: Aggressive cost-limiting would harm functionality; too-lenient limiting would expose users to cost risks

## Action

**Implemented intelligent cost-limiting**:
- Dynamically calculate maximum number of LLM calls based on user-selected scope (number of jobs, depth of ranking)
- Provide conservative defaults that protect users from unexpected costs
- Allow users to opt-in to more expansive rankings with clear cost warnings
- Log all API calls for transparency

**Design principles**:
- **Default to safety**: Conservative defaults protect users unless they explicitly opt-in
- **Transparency**: Users see exactly how many API calls will be made before they confirm
- **Reversibility**: Users can adjust parameters without major side effects

## Result

Users can confidently use Job Scout's ranking features without fear of surprise bills. The system balances functionality with user protection.

## Key Takeaway

In AI systems with external cost (API calls, inference), cost-awareness isn't nice-to-have—it's foundational. Users need to understand the cost implications of their actions, and the system should protect them by default.
