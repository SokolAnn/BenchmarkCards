# Prompt Steerability Benchmark

## 📊 Benchmark Details

**Name**: Prompt Steerability Benchmark

**Overview**: A benchmark for evaluating the steerability of model personas based on prompting, measuring how well models can reflect various personas in their responses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/IBM/prompt-steering)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the degree to which large language models can be steered to reflect various personas through prompting.

**Target Audience**:
- ML Researchers
- AI Developers
- Ethicists

**Tasks**:
- Persona Evaluation
- Model Calibration

**Limitations**: N/A

## 💾 Data

**Source**: Anthropic's persona dataset, comprising various dimensions of personas.

**Size**: 32 dimensions, each with 300 examples for both positive and negative prompts

**Format**: N/A

**Annotation**: Annotations based on label confidence indicating the expected accuracy of persona dimensions.

## 🔬 Methodology

**Methods**:
- Profiling Questions
- Steering Statements

**Metrics**:
- Steerability Indices

**Calculation**: Steerability indices calculated using the Wasserstein distance between baseline and steered profiles.

**Interpretation**: Higher values of steerability indices indicate better steerability towards intended personas.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
