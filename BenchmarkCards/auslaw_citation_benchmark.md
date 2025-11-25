# AusLaw Citation Benchmark

## 📊 Benchmark Details

**Name**: AusLaw Citation Benchmark

**Overview**: The AusLaw Citation Benchmark is a real-world dataset comprising 55,005 Australian legal instances and 18,677 unique citations, aimed at evaluating legal citation prediction using various approach comparisons.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- LEGALBENCH
- LawBench
- LexEval
- BLT
- MAUD
- CUAD

**Resources**:
- [Resource](https://auslawbench.github.iokeywords)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating models on the legal citation prediction task and to establish a dataset to inspire future developments in this legal domain.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Model Developers

**Tasks**:
- Citation Prediction

**Limitations**: N/A

## 💾 Data

**Source**: The NSW Caselaw section of the Open Australian Legal Corpus.

**Size**: 55,005 instances

**Format**: N/A

**Annotation**: Manual checking of LLM-generated descriptions for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy@1
- Accuracy@5

**Calculation**: Metrics are calculated based on the model's prediction accuracy for citations.

**Interpretation**: A higher accuracy indicates better performance in predicting the correct legal citations.

**Baseline Results**: Cite-SaulLM-7B achieved an accuracy of 51.7% and Cite-LLaMA-3.1-8B achieved 46.2% accuracy.

**Validation**: Benchmark validation through systematic testing across multiple LLM approaches and retrieval systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
