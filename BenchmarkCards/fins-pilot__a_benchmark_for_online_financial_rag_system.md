# FinS-Pilot: A Benchmark for Online Financial RAG System

## 📊 Benchmark Details

**Name**: FinS-Pilot: A Benchmark for Online Financial RAG System

**Overview**: FinS-Pilot is a benchmark for evaluating retrieval-augmented generation (RAG) systems in online financial applications, constructed from real-world financial assistant interactions and incorporating real-time API data to comprehensively evaluate financial assistants’ capabilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Chinese

**Similar Benchmarks**:
- FinanceBench
- FiQA
- FinQA

**Resources**:
- [GitHub Repository](https://github.com/PhealenWang/financial_rag_benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide an open-source benchmark for financial RAG systems, addressing gaps in existing evaluation methodologies for financial tasks.

**Target Audience**:
- Research Community
- Financial Technologists
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: User interaction logs from an online financial assistant system, supplemented with real-time market data through APIs.

**Size**: 316 queries

**Format**: JSON

**Annotation**: User queries were classified using a hierarchical intent classification system and manually verified for accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L
- BLEU

**Calculation**: Metrics are calculated based on the accuracy of responses for numerical queries and similarity measures for content-based queries.

**Interpretation**: Higher scores indicate better alignment of the generated responses with the expected answers.

**Baseline Results**: Top-performing model Xiaofa-1.0 achieves 91.5% accuracy on numerical queries.

**Validation**: Responses are validated by both automated metrics and manual reviews by experts in finance and AI.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Queries were desensitized to maintain user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
