# SUQL (Structured and Unstructured Query Language)

## 📊 Benchmark Details

**Name**: SUQL (Structured and Unstructured Query Language)

**Overview**: This paper presents the first conversational agent that supports the full generality of hybrid data access for large knowledge corpora through the Structured and Unstructured Query Language (SUQL). It introduces a semantic parser capable of handling hybrid data sources and demonstrates the effectiveness of the approach on the HybridQA dataset, achieving strong performance in combining structured data queries and free-text retrieval techniques.

**Data Type**: crowd-sourced questions and conversations

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HybridQA

**Resources**:
- [GitHub Repository](https://github.com/stanford-oval/suql)

## 🎯 Purpose and Intended Users

**Goal**: To provide a formal query language (SUQL) that can combine structured data queries and free-text retrieval for conversational agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Developers of Conversational Agents

**Tasks**:
- Question Answering
- Conversational Search

**Limitations**: N/A

## 💾 Data

**Source**: Crowd-sourced questions and conversations from Yelp datasets.

**Size**: 1828 restaurant entries with reviews and dishes.

**Format**: N/A

**Annotation**: Crowd-sourced

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match
- F1 Score

**Calculation**: Metrics calculated based on the retrieved results against ground truth from the HybridQA dataset.

**Interpretation**: Higher exact match and F1 score indicate better performance of the conversational agent.

**Baseline Results**: Within 8.9% exact match and 7.1% F1 of the SOTA model in HybridQA.

**Validation**: Validation through comparisons with existing benchmarks in the HybridQA dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Crowdsourcing participants' privacy was respected.

**Data Licensing**: Data will be available under the Apache License, Version 2.0.

**Consent Procedures**: Crowdsourcing processes included user consent for research purposes.

**Compliance With Regulations**: Data collection procedures have been approved by an IRB.
