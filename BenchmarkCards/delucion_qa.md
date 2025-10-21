# DELUCION QA

## 📊 Benchmark Details

**Name**: DELUCION QA

**Overview**: DELUCION QA is a large dataset for facilitating research on hallucination detection in retrieval-augmented question-answering (QA) systems, specifically targeting domain-specific scenarios requiring high reliability.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/boschresearch/DelucionQA)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on hallucination detection in retrieval-augmented question-answering systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from the Jeep 2023 Gladiator car manual using automated question generation and human annotation.

**Size**: 2,038 examples

**Format**: N/A

**Annotation**: Annotated by human annotators through a process involving majority voting and expert review.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1 Score
- Precision
- Recall

**Calculation**: Macro F1 is calculated based on agreement between annotations and expert reviews.

**Interpretation**: A higher F1 score indicates better performance in detecting hallucinations.

**Baseline Results**: The best-performing baseline achieves a Macro F1 of 71.09% on the test set.

**Validation**: Data is split into training, development, and test sets based on unique questions to avoid leakage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
