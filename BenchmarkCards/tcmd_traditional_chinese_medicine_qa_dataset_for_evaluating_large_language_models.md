# TCMD (Traditional Chinese Medicine QA Dataset for Evaluating Large Language Models)

## 📊 Benchmark Details

**Name**: TCMD (Traditional Chinese Medicine QA Dataset for Evaluating Large Language Models)

**Overview**: TCMD is a new medical question-answering (QA) dataset that contains massive manual instruction for solving Traditional Chinese Medicine examination tasks, aimed at comprehensively assessing the capability of large language models in the TCM domain.

**Data Type**: multiple-choice question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MLEC-QA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of different LLMs in solving TCM tasks using a dataset that adheres to the style of the Chinese National Medical Licensing Examination.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions are collected from reference books and Traditional Chinese Medicine enthusiasts, including actual examinations from different years.

**Size**: 2,851 training questions, 600 test questions

**Format**: N/A

**Annotation**: Manually verified and processed for correctness

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the correct answers given by the models on the test set.

**Interpretation**: Good performance is indicated by achieving over 60% accuracy on the multiple-choice questions.

**Baseline Results**: Models tested include General LLMs, Common Medical LLMs, and TCM-domain-specific LLMs, with varying accuracy results.

**Validation**: The dataset has been validated through manual verification and checking of the questions by medical experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
