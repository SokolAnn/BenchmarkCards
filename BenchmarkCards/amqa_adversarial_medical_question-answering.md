# AMQA (Adversarial Medical Question-Answering)

## 📊 Benchmark Details

**Name**: AMQA (Adversarial Medical Question-Answering)

**Overview**: AMQA is an Adversarial Medical Question-Answering dataset built for automated, large-scale bias evaluation of LLMs in medical QA. It includes 4,806 medical QA pairs designed to systematically control sensitive attributes like race, gender, and socioeconomic status while maintaining clinical integrity.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- EquityMedQA
- CPV

**Resources**:
- [GitHub Repository](https://github.com/XY-Showing/AMQA)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate automated and reproducible assessment of biases in large language models within medical contexts.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers
- Ethics Researchers

**Tasks**:
- Bias Evaluation
- Medical Question Answering

**Limitations**: AMQA models sensitive attributes as binary variables, which may overlook important demographic subgroups.

## 💾 Data

**Source**: Derived from the United States Medical Licensing Examination (USMLE) dataset.

**Size**: 4,806 question-answering pairs

**Format**: N/A

**Annotation**: Generated through a multi-agent framework with manual review of clinical validity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Bias-triggering assessment

**Metrics**:
- Counterfactual fairness
- Statistical Parity Difference (SPD)

**Calculation**: Counterfactual fairness measured by comparing a model's responses to neutral and adversarial variants.

**Interpretation**: Good performance constitutes consistent model responses regardless of sensitive attribute changes.

**Baseline Results**: Evaluated against existing benchmarks such as CPV.

**Validation**: Validity tested through a comprehensive human review process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Evaluates biases across sensitive attributes like race, gender, and socioeconomic status.

**Potential Harm**: ['Potential reinforcement of healthcare disparities.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
