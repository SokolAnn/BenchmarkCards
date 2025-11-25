# CHARTOM (CHARt Theory Of Mind)

## 📊 Benchmark Details

**Name**: CHARTOM (CHARt Theory Of Mind)

**Overview**: CHARTOM is a visual theory-of-mind benchmark designed to evaluate multimodal large language models’ capability to understand and reason about misleading data visualizations through charts, consisting of carefully designed charts and associated questions.

**Data Type**: charts and associated questions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2408.14419)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models on their ability to discern factual versus misleading representations in visual data.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: The dataset is relatively small due to the high cost of conducting human experiments.

## 💾 Data

**Source**: Generated dataset comprising 112 charts (56 non-manipulated and 56 manipulated).

**Size**: 112 charts

**Format**: N/A

**Annotation**: Human assessments for the Human Misleadingness Index (HMI) based on participant responses.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- Mean Absolute Error (MAE)

**Calculation**: MAE calculated between LLM’s predicted and ground truth HMI.

**Interpretation**: Higher error rates indicate worse capability of LLMs in estimating misleadingness.

**Baseline Results**: Top LLMs show near or superhuman performance on FACT questions but struggle significantly with manipulated charts.

**Validation**: Performance validated against human baseline through controlled experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinterpretation of data by users if LLMs are relied upon for accurate chart interpretation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from participants in human evaluation.

**Compliance With Regulations**: Not Applicable
