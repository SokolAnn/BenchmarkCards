# InstrumentalEval

## 📊 Benchmark Details

**Name**: InstrumentalEval

**Overview**: InstrumentalEval is a benchmark for evaluating instrumental convergence in RL-trained language models, examining how various training approaches and tasks affect the development of unintended goals that deviate from human intentions.

**Data Type**: RL scenarios

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yf-he/InstrumentalEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and quantify instrumental convergence behaviors in language models, especially focusing on the implications of different training methodologies.

**Target Audience**:
- AI Researchers
- Machine Learning Practitioners
- Ethics Researchers

**Tasks**:
- Evaluating instrumental convergence behaviors

**Limitations**: The benchmark relies on predefined scenarios that may not capture all potential failure modes.

## 💾 Data

**Source**: Constructed scenarios for testing instrumental convergence in RL models.

**Size**: 76 tasks

**Format**: N/A

**Annotation**: Designed and categorized by the authors based on reinforcement learning principles.

## 🔬 Methodology

**Methods**:
- Response Generation
- Response Analysis

**Metrics**:
- Instrumental Rate (IR)
- Category-Specific Instrumental Rate (CIR)
- Inter-Judge Agreement Rate (IAR)

**Calculation**: IR is calculated as the percentage of tasks where the model exhibits convergence behaviors relative to the total tasks.

**Interpretation**: Higher IR indicates a stronger tendency for models to develop instrumental goals.

**Validation**: Pilot testing and inter-judge evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Alignment

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
