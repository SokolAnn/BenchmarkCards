# GUIDED BENCH

## 📊 Benchmark Details

**Name**: GUIDED BENCH

**Overview**: GUIDED BENCH is a benchmark comprising a curated harmful question dataset and a case-by-case evaluation framework (GUIDED EVAL) for accurately measuring the effectiveness of jailbreak methods in large language models (LLMs). It aims to address discrepancies in existing evaluation paradigms.

**Data Type**: harmful question dataset

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://sproutnan.github.io/AI-Safety_Benchmark/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more accurate and nuanced evaluation system for jailbreak methods targeting LLMs, helping researchers uncover vulnerabilities and improve safety protocols.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners

**Tasks**:
- Jailbreak Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from multiple existing datasets including StrongREJECT, HarmBench, and ForbiddenQuestionSet, along with new cases created specifically for this benchmark.

**Size**: 200 harmful question instances

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Guideline-based evaluation
- LLM-as-a-judge evaluations

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: The percentage of scoring points fulfilled in guideline-defined evaluations is calculated as the ASR.

**Interpretation**: Higher ASR indicates better effectiveness of the jailbreak methods evaluated against the established guidelines.

**Baseline Results**: N/A

**Validation**: Evaluation of jailbreak methods based on comparative ASR across different victim LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
