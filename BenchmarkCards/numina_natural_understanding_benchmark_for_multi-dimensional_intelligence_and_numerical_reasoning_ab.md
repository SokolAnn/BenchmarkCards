# NUMINA (Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities)

## 📊 Benchmark Details

**Name**: NUMINA (Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities)

**Overview**: NUMINA is the first Natural Understanding benchmark that enhances multimodal indoor perceptual understanding by focusing on fine-grained spatial understanding and numerical reasoning in indoor environments.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ScanRefer
- ScanQA
- Talk2Nav

**Resources**:
- [GitHub Repository](https://github.com/fengshun124/NUMINA)

## 🎯 Purpose and Intended Users

**Goal**: To assess multi-dimensional intelligence and numerical reasoning capabilities of large language models in 3D environments.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Fact Validation
- Prompt Matching
- Numerical Inference

**Limitations**: Although the benchmark encompasses a wide range of tasks, it may not fully capture all aspects of human cognition, particularly those dimensions that are inherently subjective or difficult to quantify.

## 💾 Data

**Source**: The dataset is based on 3D indoor scenes from ScanNet and incorporates data from ScanQA.

**Size**: 74,526 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated using NUMINA-Flow, which combines LLM rewriting and rule-based verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Threshold Accuracy

**Calculation**: Threshold Accuracy is calculated as the percentage of predictions falling within a predefined error threshold with respect to ground truth.

**Interpretation**: Accuracy measures the number of correct predictions, while Threshold Accuracy indicates acceptable predictions within defined error margins.

**Validation**: The dataset outputs undergo human and rule-based validation to ensure quality and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The documents of NUMINA do not contain private information and annotating this dataset is not necessary to make judgments about social risks.

**Data Licensing**: The ScanQA dataset is distributed with the CC BY-NC-SA 3.0 license, and ScanNet is available for research use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
