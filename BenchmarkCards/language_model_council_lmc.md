# Language Model Council (LMC)

## 📊 Benchmark Details

**Name**: Language Model Council (LMC)

**Overview**: The Language Model Council (LMC) evaluates Large Language Models (LLMs) using a democratic framework where multiple LLMs collaboratively create tests, respond to them, and evaluate each other's responses, thus aiming for an inclusive consensus ranking, specifically demonstrated in a case study on emotional intelligence tasks.

**Data Type**: generated scenarios and responses

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://llm-council.com)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark Large Language Models on highly subjective tasks like emotional intelligence through collective evaluation by a group of LLMs.

**Target Audience**:
- ML Researchers
- AI Developers
- Natural Language Processing Practitioners

**Tasks**:
- Emotional Intelligence Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic expansions of the EmoBench dataset created collaboratively by LLMs.

**Size**: 100 dilemmas

**Format**: text

**Annotation**: Manually reviewed and curated by researchers.

## 🔬 Methodology

**Methods**:
- Pairwise comparison
- Human evaluation
- Monte Carlo simulation

**Metrics**:
- Separability
- Agreement among judges

**Calculation**: Metrics calculated using extensive pairwise comparisons and bootstrapping techniques for confidence intervals.

**Interpretation**: Higher separability indicates better model differentiation in ranking.

**Baseline Results**: Comparison against existing models like GPT-4 and Qwen-1.0.

**Validation**: Validated through human evaluations of model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: The dataset includes a variety of interpersonal conflict scenarios developed through collaborative LLM participation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY license, allowing for redistribution and modification.

**Consent Procedures**: Participants were informed and gave consent for their demographic data to be collected; details provided via Prolific.

**Compliance With Regulations**: Not Applicable
