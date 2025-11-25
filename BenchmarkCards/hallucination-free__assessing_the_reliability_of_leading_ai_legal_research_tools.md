# Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools

## 📊 Benchmark Details

**Name**: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools

**Overview**: This study presents a preregistered empirical evaluation of AI-driven legal research tools, focusing on their tendency to hallucinate as they assist with legal tasks. It introduces a comprehensive dataset for identifying vulnerabilities in these tools and proposes a framework for assessing hallucinations in legal AI systems.

**Data Type**: legal queries

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LegalBench

**Resources**:
- [Resource](https://arxiv.org/abs/2405.20362)

## 🎯 Purpose and Intended Users

**Goal**: To assess and report the performance of retrieval-augmented generation (RAG)-based AI legal research tools and to characterize their hallucination rates.

**Target Audience**:
- Legal Professionals
- AI Researchers
- Law Students

**Tasks**:
- Legal Research
- Fact-checking
- Legal Citation Verification

**Limitations**: High hallucination rates persist, suggesting careful verification of AI outputs is necessary before use.

## 💾 Data

**Source**: Constructed dataset of legal queries tailored for evaluating RAG-based legal research tools.

**Size**: 202 queries

**Format**: JSON

**Annotation**: Manually curated and reviewed by legal experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Systematic assessment of performance
- Statistical analysis

**Metrics**:
- Accuracy
- Hallucination rate
- Response completeness

**Calculation**: Metrics were calculated by comparing model responses to ground truth provided in a manually curated dataset of legal queries.

**Interpretation**: Responses were categorized as accurate, incomplete, or hallucinated based on their correctness and groundedness.

**Validation**: Preregistered study design aimed to ensure rigor in evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Legal malpractice due to reliance on faulty AI outputs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
