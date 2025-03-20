# QL-Bench

## 📊 Benchmark Details

**Name**: QL-Bench

**Overview**: QL-Bench is a benchmark designed to measure the self-awareness ability of Multi-modality Large Language Models (MLLMs) in low-level visual tasks. It comprises a dataset focused on simulating human responses to low-level visual perception through visual question answering.

**Data Type**: Images and Questions

**Domains**:
- Visual Perception
- Machine Learning
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- MmBench
- MVLM

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the self-awareness of MLLMs in low-level visual perception tasks.

**Target Audience**:
- Researchers
- AI Developers

**Tasks**:
- Visual Question Answering
- Self-awareness Evaluation

**Limitations**: None

**Out of Scope Uses**:
- High-level visual tasks

## 💾 Data

**Source**: Various diverse sources (10 sources)

**Size**: 2,990 single images and 1,999 image pairs

**Format**: Images and Open-ended Questions

**Annotation**: Each image has a low-level related question, correct answer, false answers, and 'I don't know' option.

## 🔬 Methodology

**Methods**:
- Evaluation of self-awareness through QL-Bench
- Comparative analysis across MLLMs

**Metrics**:
- score cc
- score rc
- score sa

**Calculation**: score sa = score cc + score rc

**Interpretation**: Higher scores reflect better self-awareness in answering questions correctly and acknowledging uncertainty.

**Validation**: Fifteen popular MLLMs evaluated for self-awareness capability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Explainability
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias, Output bias
- **Explainability**: Inaccessible training data, Untraceable attribution
- **Robustness**: Prompt injection attack, Data poisoning

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
