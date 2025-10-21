# MEDAGENTS BENCH

## 📊 Benchmark Details

**Name**: MEDAGENTS BENCH

**Overview**: MEDAGENTS BENCH is a benchmark specifically designed to evaluate complex medical reasoning capabilities where standard benchmarks fall short, focusing on challenging medical questions requiring multi-step clinical reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- PubMedQA
- MedMCQA
- MedBullets
- MMLU
- MMLU-Pro
- MedExQA
- MedXpertQA

**Resources**:
- [GitHub Repository](https://github.com/gersteinlab/medagents-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for complex medical reasoning tasks that current models struggle with.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Medical Question Answering

**Limitations**: While MEDAGENTS BENCH provides a rigorous benchmark for evaluating medical reasoning capabilities, its focus on educational resources may not fully reflect real-world clinical scenarios.

## 💾 Data

**Source**: MEDAGENTS BENCH is constructed from seven established medical datasets.

**Size**: 862 questions

**Format**: N/A

**Annotation**: Questions are annotated by medical professionals to verify reasoning depth.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on performance on the selected HARD subset of questions.

**Interpretation**: Higher accuracy indicates better medical reasoning capabilities.

**Validation**: The benchmark includes thorough contamination analysis and verification by medical professionals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
