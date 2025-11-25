# ArithmAttack

## 📊 Benchmark Details

**Name**: ArithmAttack

**Overview**: ArithmAttack is proposed to examine how robust Large Language Models (LLMs) are when encountering noisy prompts that contain extra noise in the form of punctuation marks. It assesses robustness in math problem-solving tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MultiArith

**Resources**:
- [Resource](https://arxiv.org/abs/2501.08203)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of various Large Language Models to noisy inputs in math problem-solving.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Problem Solving

**Limitations**: The study focuses only on one type of noise (punctuation marks) and uses a limited number of datasets and models.

## 💾 Data

**Source**: GSM8K and MultiArith datasets.

**Size**: 8,500 examples (GSM8K) and 180 examples (MultiArith)

**Format**: Text

**Annotation**: Not explicitly stated in the paper.

## 🔬 Methodology

**Methods**:
- Zero-Shot Prompting
- Adversarial Noise Insertion

**Metrics**:
- Accuracy
- Attack Success Rate (ASR)

**Calculation**: ASR is calculated as the ratio of incorrect predictions made after the noise attack to previously correct predictions.

**Interpretation**: Lower ASR values imply better robustness against noise.

**Baseline Results**: Llama3.1 achieved the highest accuracies across both datasets with robustness against noise.

**Validation**: Evaluated performance across different levels of noise (10%, 30%, 50%) on the input data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack, Data poisoning
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
