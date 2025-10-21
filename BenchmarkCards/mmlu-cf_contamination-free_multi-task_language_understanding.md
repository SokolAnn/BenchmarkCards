# MMLU-CF (Contamination-free Multi-task Language Understanding)

## 📊 Benchmark Details

**Name**: MMLU-CF (Contamination-free Multi-task Language Understanding)

**Overview**: MMLU-CF is a contamination-free and challenging multiple-choice question benchmark for large language models (LLMs), aiming to assess their understanding of world knowledge while minimizing data leakage and contamination.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous and contamination-free evaluation standard for large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multiple-choice Question Answering

**Limitations**: While constructed with objectivity, it may still contain errors, and focuses primarily on multiple-choice questions without covering other modalities.

## 💾 Data

**Source**: Sourced from over 200 billion documents on public open websites, ensuring a diverse collection of questions.

**Size**: 20,000 questions (10,000 for test set and 10,000 for validation set)

**Format**: N/A

**Annotation**: Questions were cleaned and vetted using multiple large language models to ensure quality.

## 🔬 Methodology

**Methods**:
- Evaluation of leading LLMs against the benchmark using 5-shot and 0-shot tests.

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the performance of models on the MMLU-CF test and validation sets.

**Interpretation**: Higher accuracy indicates better understanding and performance of models on the questions.

**Validation**: The validation set is open-source for public evaluation and scrutiny.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Constructed with open-source data to ensure transparency.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
