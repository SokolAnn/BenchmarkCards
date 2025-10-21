# SoSBench (Safety Alignment on Scientific Knowledge)

## 📊 Benchmark Details

**Name**: SoSBench (Safety Alignment on Scientific Knowledge)

**Overview**: SoSBench is a regulation-grounded, hazard-focused benchmark for evaluating the safety alignment of large language models (LLMs) on tasks involving scientific knowledge. It comprises 3,000 prompts designed to elicit potentially high-risk behaviors from LLMs across six scientific domains: chemistry, biology, medicine, pharmacology, physics, and psychology.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://sosbench.github.io/)
- [GitHub Repository](https://github.com/SOSBench/SOSBenchEval)
- [Resource](https://huggingface.co/SOSBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess LLM safety in scientific domains through regulation-based hazards and identify gaps in safety mechanisms.

**Target Audience**:
- ML Researchers
- Safety Engineers
- AI Developers

**Tasks**:
- Risk Assessment
- Safety Alignment Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 3,000 prompts derived from real-world regulations and laws in six scientific domains.

**Size**: 3,000 examples

**Format**: JSON

**Annotation**: Crowdsourced via expert input and LLM-assisted validation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Harmful Rate (HR)

**Calculation**: The Harmful Rate is calculated as the proportion of unsafe responses per total prompts.

**Interpretation**: Lower HR indicates better safety alignment; thresholds for harmful responses are determined based on model evaluations.

**Baseline Results**: HR scores showed high rates of harmful responses across tested LLMs, e.g., 79.1% for Deepseek-R1 and 47.3% for GPT-4.

**Validation**: Each prompt's ability to elicit harmful responses is validated through multiple model evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Robustness

**Atlas Risks**:
- **Privacy**
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All prompts are derived from non-classified, open-source materials; no personal data involved.

**Data Licensing**: The dataset is released under an authentication-gated license restricted to verified research use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
