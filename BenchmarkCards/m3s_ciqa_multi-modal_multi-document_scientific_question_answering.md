# M3S CIQA (Multi-Modal Multi-Document Scientific Question Answering)

## 📊 Benchmark Details

**Name**: M3S CIQA (Multi-Modal Multi-Document Scientific Question Answering)

**Overview**: M3S CIQA is a multi-modal, multi-document scientific question answering benchmark designed for a more comprehensive evaluation of foundation models, containing 1,452 expert-annotated questions spanning 70 natural language processing paper clusters.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yale-nlp/M3SciQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multi-modal reasoning abilities in interpreting multiple scientific documents.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The evaluations presented in this study are met with certain limitations due to inherent disparities in the context window of current open-source and proprietary LLMs and LMMs.

## 💾 Data

**Source**: Expert-annotated questions from the M3S CIQA benchmark.

**Size**: 1,452 questions

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Accuracy
- Recall
- Precision
- F1 Score

**Calculation**: Metrics such as MRR are calculated based on the model's performance in retrieving relevant documents.

**Interpretation**: Higher scores indicate better model performance in multi-modal reasoning and document understanding.

**Baseline Results**: Expert performance is assessed as a benchmark for comparison.

**Validation**: The benchmark was validated through structured evaluations against human expert performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
