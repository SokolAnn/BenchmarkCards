# GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI

## 📊 Benchmark Details

**Name**: GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI

**Overview**: GMAI-MMBench is the most comprehensive general medical AI benchmark with well-categorized data structure and multi-perceptual granularity to evaluate large vision-language models (LVLMs) in clinical practice. It consists of 284 datasets covering 38 medical image modalities, 18 clinical-related tasks, 18 departments, and 4 types of perceptual granularity.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- Medical-Diff-VQA
- PathVQA
- VQA-RAD

**Resources**:
- [Resource](https://uni-medical.github.io/GMAI-MMBench.github.io/)
- [Resource](https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench)
- [Resource](https://opendatalab.com/GMAI/MMBench)
- [GitHub Repository](https://github.com/open-compass/VLMEvalKit)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for large vision-language models in the medical domain.

**Target Audience**:
- ML Researchers
- Medical Practitioners

**Tasks**:
- Clinical Visual Question Answering
- Image Classification
- Image Segmentation
- Object Detection

**Limitations**: N/A

## 💾 Data

**Source**: Combines public datasets and hospital datasets curated for medical image tasks.

**Size**: 26,000 question-answering pairs

**Format**: N/A

**Annotation**: Manually generated and validated question-answering pairs based on clinical data.

## 🔬 Methodology

**Methods**:
- Quantitative Evaluation
- Human Evaluation

**Metrics**:
- Accuracy
- Recall

**Calculation**: Accuracy is calculated based on the ratio of correct predictions to total questions. Recall is based on matched predictions in multiple-choice questions.

**Interpretation**: Higher accuracy and recall rates indicate better model performance on clinical tasks.

**Baseline Results**: N/A

**Validation**: Models are assessed in a zero-shot setting to test generalization capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data used is ethically sourced and anonymized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
