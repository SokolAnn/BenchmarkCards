# SSTQA (Semi-Structured Table Question Answering)

## 📊 Benchmark Details

**Name**: SSTQA (Semi-Structured Table Question Answering)

**Overview**: SSTQA is a dataset specifically designed to evaluate a model’s ability to conduct semi-structured table question answering tasks in real-world scenarios, featuring 764 questions over 102 real-world semi-structured tables.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WikiTQ
- TempTabQA

**Resources**:
- [GitHub Repository](https://github.com/weAIDB/ST-Raptor)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models’ capabilities in answering questions over semi-structured tables accurately and reliably.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated from over 2031 real-world tables across 19 representative scenarios such as administrative and financial management.

**Size**: 764 question-answer pairs

**Format**: JSON

**Annotation**: Manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L

**Calculation**: Accuracy is calculated based on the correct answers retrieved by the model for the questions in the SSTQA dataset.

**Interpretation**: A higher accuracy indicates better performance in answering questions correctly based on the semi-structured tables.

**Baseline Results**: ST-Raptor outperformed nine baselines by up to 20% in answer accuracy.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
