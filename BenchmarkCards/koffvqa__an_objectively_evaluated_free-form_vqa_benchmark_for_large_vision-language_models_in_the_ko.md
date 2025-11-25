# KOFFVQA: An Objectively Evaluated Free-form VQA Benchmark for Large Vision-Language Models in the Korean Language

## 📊 Benchmark Details

**Name**: KOFFVQA: An Objectively Evaluated Free-form VQA Benchmark for Large Vision-Language Models in the Korean Language

**Overview**: KOFFVQA is a general-purpose free-form visual question answering benchmark in the Korean language for the evaluation of vision-language models (VLMs). It consists of 275 carefully crafted questions each paired with an image and grading criteria covering 10 different aspects of VLM performance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Similar Benchmarks**:
- VLR-Bench
- VARCO-VISION
- K-MMBench
- K-SEED
- K-MMStar

**Resources**:
- [GitHub Repository](https://github.com/maum-ai/KOFFVQA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the KOFFVQA benchmark is to provide an objective evaluation framework for VLMs in the Korean language, allowing for the assessment of various aspects of their performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Images are sourced from various online repositories, including the Open Images v7 dataset and the KAIST Scene Text dataset, along with curated questions.

**Size**: 275 questions

**Format**: N/A

**Annotation**: Questions and grading criteria are created by human annotators.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge evaluation

**Metrics**:
- Accuracy

**Calculation**: Scores are computed based on predefined grading criteria, with evaluations scaled from 0 to 10, and then transformed to a range of 0 to 100.

**Interpretation**: Higher average scores indicate better performance, which is directly comparable with other benchmarks.

**Validation**: Evaluation compared against human scores for accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
