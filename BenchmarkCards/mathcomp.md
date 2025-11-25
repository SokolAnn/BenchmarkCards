# MathComp

## 📊 Benchmark Details

**Name**: MathComp

**Overview**: MathComp is a controlled benchmark of 300 comparison scenarios designed to isolate framing effects on reasoning in large language models (LLMs). It evaluates how different prompt framings induce biases in model predictions through comparative math problems.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/more_or_less_wrong-33B2)

## 🎯 Purpose and Intended Users

**Goal**: To diagnose reasoning robustness and fairness in LLMs by analyzing how linguistic framing affects model responses to comparative tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Comparative Reasoning

**Limitations**: The dataset size is limited to 300 comparative samples, which may affect the robustness of findings.

## 💾 Data

**Source**: Constructed through a semi-automated process using LLMs and expert filtering.

**Size**: 300 scenarios

**Format**: JSON

**Annotation**: Annotated through expert verification and symbolic validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Directional Error Rate

**Calculation**: The proportion of cases in which the model incorrectly selects an answer among all cases where that answer would be erroneous.

**Interpretation**: A high Directional Error Rate indicates strong bias toward a certain comparative term due to its framing in the prompt.

**Validation**: Validated through expert review and symbolic verification of generated scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias, Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Identifies how demographic cues, such as gender and race, affect model predictions under linguistic framing.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
