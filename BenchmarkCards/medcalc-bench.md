# MedCalc-Bench

## 📊 Benchmark Details

**Name**: MedCalc-Bench

**Overview**: MedCalc-Bench evaluates the performance of large language models on real-world medical calculation tasks by proposing a step-by-step evaluation framework that checks formula selection, entity extraction, and arithmetic computation, addressing the limitations of existing benchmarks.

**Data Type**: clinical calculation tasks

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- PubMedQA
- MedMCQA

**Resources**:
- [GitHub Repository](https://github.com/Super-Billy/EMNLP-2025-MedRaC)

## 🎯 Purpose and Intended Users

**Goal**: Provide a more granular evaluation method for assessing LLM performance on medical calculations and enhance clinical trustworthiness.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Clinical Decision Support System Developers

**Tasks**:
- Medical Calculation Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: MedCalc-Bench dataset

**Size**: 940 cases

**Format**: JSON

**Annotation**: Manually reviewed and curated by expert clinicians

## 🔬 Methodology

**Methods**:
- Step-wise evaluation pipeline
- Human evaluation
- Automated metrics

**Metrics**:
- Step-wise evaluation accuracy

**Calculation**: Each component of the medical calculation is assessed independently for correctness.

**Interpretation**: Performance is evaluated based on validation of formula selection, variable extraction, arithmetic calculation, and final answer.

**Baseline Results**: Zero-shot Chain-of-Thought (CoT) prompting serves as the baseline.

**Validation**: Accuracy of evaluations is confirmed against expert human annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate clinical judgments based on faulty calculations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache-2.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
