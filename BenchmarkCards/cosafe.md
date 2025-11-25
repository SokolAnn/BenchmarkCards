# CoSafe

## 📊 Benchmark Details

**Name**: CoSafe

**Overview**: CoSafe is a dataset comprising 1,400 multi-turn dialogue coreference questions across 14 categories, designed to evaluate the safety of large language models (LLMs) in dialogue coreference contexts.

**Data Type**: multi-turn dialogue coreference questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- SaFeRDialogues
- HarmfulQ

**Resources**:
- [GitHub Repository](https://github.com/ErxinYu/CoSafe-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the safety of large language models in multi-turn dialogue scenarios by identifying vulnerabilities related to coreference.

**Target Audience**:
- ML Researchers
- Model Developers
- Safety Analysts

**Tasks**:
- Safety Evaluation
- Dialogue Coreference Analysis

**Limitations**: Semantic drift in multi-turn questions; high cost of generating multi-turn dialogue coreferences.

## 💾 Data

**Source**: Dataset created using prompts derived from BeaverTails (Ji et al. 2023) and expanded using GPT-4.

**Size**: 1,400 examples

**Format**: JSON

**Annotation**: Automated expansion of prompts into multi-turn dialogues using GPT-4 with manual refinement.

## 🔬 Methodology

**Methods**:
- QA Moderation
- Human Evaluation
- LLM Evaluation

**Metrics**:
- Attack Successful Rate
- Harmful Rate

**Calculation**: Metrics calculated through comparisons between responses generated for single prompts and multi-turn dialogues.

**Interpretation**: Higher attack successful rates indicate increased vulnerabilities in dialogue coreference scenarios.

**Validation**: Validation was conducted using multiple evaluation methods and cross-comparisons of harmful rates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Bias

**Atlas Risks**:
- **Robustness**: Prompt leaking, Data poisoning
- **Fairness**: Output bias

**Demographic Analysis**: Analysis of model responses indicated varying harmfulness across demographic categories.

**Potential Harm**: ['Potential to generate harmful or unsafe responses due to coreference manipulation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
