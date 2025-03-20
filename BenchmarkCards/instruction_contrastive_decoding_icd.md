# Instruction Contrastive Decoding (ICD)

## 📊 Benchmark Details

**Name**: Instruction Contrastive Decoding (ICD)

**Overview**: The paper introduces a novel method to mitigate hallucinations in Large Vision-Language Models (LVLMs) during inference, aimed at improving their accuracy with respect to visual inputs through contrastive decoding.

**Data Type**: N/A

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- MME
- LLaVa-Bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To reduce hallucinations in LVLM inference, thereby improving the fidelity of generated content to the visual inputs.

**Target Audience**:
- Researchers
- Practitioners in AI and Machine Learning

**Tasks**:
- Mitigation of hallucinations in multimodal models
- Enhancement of perception and recognition capabilities

**Limitations**: N/A

**Out of Scope Uses**:
- Real-time deployment without proper validation
- Applications not related to LVLMs

## 💾 Data

**Source**: N/A

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Instruction Contrastive Decoding (ICD)
- Contrastive decoding with disturbance instructions

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Token probabilities are derived from the contrast between the original and disturbance instruction distributions.

**Interpretation**: IMarchored responses are evaluated based on their fidelity to provided visual contexts.

**Baseline Results**: ICD outperforms baseline LVLM methods such as miniGPT4 and InstructBLIP.

**Validation**: Extensive experiments on benchmarks POPE, MME, and LLaVa-Bench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination in generated content
- Dependence on statistical biases
- Over-reliance on language priors

**Atlas Risks**:
- **Robustness**: Hallucination
- **Fairness**
- **Accuracy**: Poor model accuracy
- **Value Alignment**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
