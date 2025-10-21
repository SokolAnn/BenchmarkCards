# HalluDial (A Large-Scale Benchmark for Automatic Dialogue-Level Hallucination Evaluation)

## 📊 Benchmark Details

**Name**: HalluDial (A Large-Scale Benchmark for Automatic Dialogue-Level Hallucination Evaluation)

**Overview**: HalluDial is the first comprehensive large-scale benchmark for automatic dialogue-level hallucination evaluation, covering both spontaneous and induced hallucination scenarios, including factuality and faithfulness hallucinations with a total of 146,856 samples.

**Data Type**: dialogue samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- HaluEval

**Resources**:
- [GitHub Repository](https://github.com/FlagOpen/HalluDial)

## 🎯 Purpose and Intended Users

**Goal**: To study and evaluate hallucinations of large language models in information-seeking dialogues.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Hallucination Detection
- Evaluation of Language Models

**Limitations**: While the HalluDial dataset is relatively large, it may not fully capture all real-world conversation scenarios.

## 💾 Data

**Source**: Derived from an information-seeking dialogue dataset.

**Size**: 146,856 samples

**Format**: N/A

**Annotation**: Automatically annotated using GPT-4.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score
- Accuracy
- Average Precision
- Average Recall

**Calculation**: Metrics are calculated based on hallucination detection tasks using evaluators like HalluJudge and other language models.

**Interpretation**: A higher F1 score indicates better performance in detecting hallucinations.

**Baseline Results**: HalluJudge achieved an F1 Score of 84.92.

**Validation**: Validation through performance comparison with established LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: May contain potentially sensitive topics related to big events.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All dialogues are sourced from publicly available data, minimizing privacy risks.

**Data Licensing**: CC BY-NC-SA

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
