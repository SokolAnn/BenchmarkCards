# MultiStAR (Multi-Stage Abstract Visual Reasoning)

## 📊 Benchmark Details

**Name**: MultiStAR (Multi-Stage Abstract Visual Reasoning)

**Overview**: MultiStAR is a benchmark designed to evaluate Multimodal Large Language Models (MLLMs) during the abstract visual reasoning (AVR) process through two subtasks: Direct Answer and Logical Chain, focusing on intermediate reasoning steps.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- RA VEN

**Resources**:
- [GitHub Repository](https://github.com/YanbeiJiang/MultiStAR)

## 🎯 Purpose and Intended Users

**Goal**: To assess reasoning across varying levels of complexity in MLLMs while accounting for both intermediate and final answers in abstract visual reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: The intermediate task generation is restricted to datasets with defined object attributes; limits applicability to other AVR datasets lacking such metadata.

## 💾 Data

**Source**: Derived from the RA VEN dataset.

**Size**: 8,100 examples for Direct Answer; 560 examples for Logical Chain.

**Format**: Multiple-Choice Question Answering (MCQA)

**Annotation**: Automatically generated using template-based methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- MSEval

**Calculation**: Accuracy is computed as the proportion of correct answers. MSEval aggregates correctness across all reasoning stages.

**Interpretation**: MSEval provides a more granular analysis of the model’s performance, reflecting the correctness of both intermediate steps and final answers.

**Baseline Results**: Human performance serves as a baseline with ratings exceeding 60% across tasks.

**Validation**: Evaluated through tests against human performances and model capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Evaluation conducted for diverse demographics from crowdsourced human studies.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from human participants for data collection.

**Compliance With Regulations**: Not Applicable
