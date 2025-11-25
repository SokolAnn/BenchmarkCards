# MMLU (Massive Multitask Language Understanding)

## 📊 Benchmark Details

**Name**: MMLU (Massive Multitask Language Understanding)

**Overview**: This study measures the impact of user-provided suggestions on Large Language Models (LLMs) in an educational context, specifically focusing on the phenomenon of sycophancy, where LLMs may agree with user suggestions even when they are incorrect.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2506.10297)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to measure the sycophancy effects in LLMs used in educational settings, revealing how user framing can affect model performance.

**Target Audience**:
- ML Researchers
- Educators
- Educational Technologists

**Tasks**:
- Question Answering

**Limitations**: The MMLU dataset is acknowledged to have incorrect ground truth labels in about 6.5% of cases.

## 💾 Data

**Source**: The MMLU dataset consists of 14,042 unique question and answer prompts with labeled correct answers.

**Size**: 14,042 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Experimental design

**Metrics**:
- Accuracy

**Calculation**: Model accuracy is calculated by measuring how often the LLM identifies the correct answer programmatically.

**Interpretation**: Higher accuracy indicates that LLMs are more likely to provide correct answers when users suggest the correct answer, demonstrating a sycophancy effect.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
