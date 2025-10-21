# MMDocRAG

## 📊 Benchmark Details

**Name**: MMDocRAG

**Overview**: MMDocRAG is a comprehensive benchmark featuring 4,055 expert-annotated QA pairs with multi-page, cross-modal evidence chains for evaluating multimodal document question answering (DocVQA) and retrieval-augmented generation (RAG).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DocVQA
- MMLongBench-Doc
- DUDE

**Resources**:
- [Resource](https://mmdocrag.github.io/MMDocRAG/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous testing ground for multimodal document question answering systems and improve evaluation methodologies for retrieval-augmented generators.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MMDocIR dataset

**Size**: 4,055 QA pairs

**Format**: JSON

**Annotation**: Expert annotations for multimodal evidence and question-answer pairs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are computed across quote selection accuracy and multimodal answer generation quality.

**Interpretation**: Higher scores indicate better performance in selecting relevant quotes and generating coherent multimodal responses.

**Baseline Results**: Not explicitly stated in the paper.

**Validation**: Comprehensive evaluations were conducted using various VLM/LLM models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache License 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
