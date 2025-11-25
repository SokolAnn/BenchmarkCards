# IMPLIRET (Implicit Fact Retrieval Challenge)

## 📊 Benchmark Details

**Name**: IMPLIRET (Implicit Fact Retrieval Challenge)

**Overview**: IMPLIRET introduces a benchmark for evaluating retrieval models when relevance depends on document-side reasoning on implicit facts. It focuses on reasoning categories such as world knowledge, arithmetic, and temporal.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BEIR
- RAR-b
- BIRCO
- BRIGHT

**Resources**:
- [GitHub Repository](https://github.com/ZeinabTaghavi/IMPLIRET)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate retrieval systems on their ability to retrieve relevant documents based on implicit knowledge rather than surface-level matching.

**Target Audience**:
- NLP Researchers
- Model Developers

**Tasks**:
- Retrieval
- Document-Reasoning

**Limitations**: While carefully designed, IMPLIRET data may differ slightly from naturally occurring text in discourse structure or topic diversity.

## 💾 Data

**Source**: Synthetically generated using LLMs and structured templates.

**Size**: 90,000 examples

**Format**: JSON

**Annotation**: Automatically generated and semi-automated with human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- nDCG@10
- ROUGE-1

**Calculation**: Metrics were calculated based on retrieval performance against implicit queries.

**Interpretation**: Higher nDCG@10 and ROUGE-1 recall indicate better performance in retrieving relevant documents.

**Baseline Results**: The best nDCG@10 achieved was 14.91% using dense retrieval methods.

**Validation**: Validation includes sanity checks on fluency and implicit support for the queried facts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
