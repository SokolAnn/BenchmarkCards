# OmniEval

## 📊 Benchmark Details

**Name**: OmniEval

**Overview**: OmniEval is an omnidirectional and automatic benchmark for evaluating retrieval-augmented generation (RAG) systems in the financial domain. It features a multi-dimensional evaluation framework with a structured assessment across various financial topics.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- PIXIU
- FinanceBench
- AlphaFin

**Resources**:
- [GitHub Repository](https://github.com/RUC-NLPIR/OmniEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and automatic evaluation benchmark for RAG systems in the finance domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Extractive Question Answering
- Multi-hop Reasoning
- Contrast Question Answering
- Long-form Question Answering
- Conversational Question Answering

**Limitations**: The benchmark may exhibit biases due to limited data availability and human annotation constraints.

## 💾 Data

**Source**: Created from a variety of financial documents, including web pages and repositories specific to finance.

**Size**: 11,400 examples

**Format**: JSON

**Annotation**: Combination of automated and human annotation methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Rouge-L
- Mean Average Precision (MAP)

**Calculation**: Metrics are calculated based on test examples generated through automated and human annotation methods.

**Interpretation**: Evaluations are interpreted through semantic alignment norms and accuracy measures referencing ground truth answers.

**Baseline Results**: Various RAG models were compared using the OmniEval dataset.

**Validation**: The validation process involved both automated quality checks and human corrections.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
