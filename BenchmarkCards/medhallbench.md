# MedHallBench

## 📊 Benchmark Details

**Name**: MedHallBench

**Overview**: MedHallBench is a comprehensive benchmark framework for evaluating and mitigating hallucinations in Medical Large Language Models (MLLMs) using expert-validated medical case scenarios along with established medical databases.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MedMCQA
- MultiMedQA
- Med-HALT

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundational framework for addressing hallucinations in medical large language models and to ensure their reliability in healthcare applications.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Medical Data Scientists

**Tasks**:
- Evaluating Hallucination in Medical Language Models

**Limitations**: N/A

## 💾 Data

**Source**: Expert-validated medical case scenarios and established medical databases.

**Size**: N/A

**Format**: N/A

**Annotation**: Expert annotation by medical professionals with structured evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ACHMI (Assessment of Caption Hallucinations in Medical Imagery)

**Calculation**: The ACHMI metrics assess the proportion of hallucinated components in model outputs and compare them with ground truth.

**Interpretation**: Lower ACHMI values indicate fewer hallucinations.

**Baseline Results**: N/A

**Validation**: Evaluation by expert medical professionals to establish a gold standard.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
