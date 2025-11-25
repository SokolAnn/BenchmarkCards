# MedSentry

## 📊 Benchmark Details

**Name**: MedSentry

**Overview**: MedSentry is a benchmark comprising 5,000 adversarial medical prompts spanning 25 threat categories with 100 subthemes. It provides a rigorous evaluation framework to analyze how various multi-agent architectures respond to malicious prompts in medical settings.

**Data Type**: adversarial medical prompts

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedSafetyBench

**Resources**:
- [Resource](https://arxiv.org/abs/2505.20824)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the safety and robustness of multi-agent systems in healthcare against insider threats and to propose effective defense strategies.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- AI Safety Analysts

**Tasks**:
- Multi-Agent System Evaluation
- Adversarial Prompt Testing

**Limitations**: N/A

## 💾 Data

**Source**: Generated and curated based on clinical practice and regulatory guidelines, involving feedback from licensed physicians.

**Size**: 5,000 adversarial medical prompts

**Format**: N/A

**Annotation**: Human-reviewed and curated by medical experts.

## 🔬 Methodology

**Methods**:
- Systematic Evaluation
- Empirical Testing

**Metrics**:
- Length-Controlled Score (LCS)
- Raw Score (RS)

**Calculation**: Aggregated scores based on evaluator assessments against the AMA Principles of Medical Ethics.

**Interpretation**: Scores indicate the safety and ethical compliance of responses, with higher scores representing safer practices.

**Baseline Results**: N/A

**Validation**: Evaluated against other benchmark datasets to ensure robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Ethics

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data maintained privacy, anonymization processes applied during data generation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
