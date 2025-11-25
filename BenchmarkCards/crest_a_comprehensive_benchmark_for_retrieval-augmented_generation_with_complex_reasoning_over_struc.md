# CReSt (A Comprehensive Benchmark for Retrieval-Augmented Generation with Complex Reasoning over Structured Documents)

## 📊 Benchmark Details

**Name**: CReSt (A Comprehensive Benchmark for Retrieval-Augmented Generation with Complex Reasoning over Structured Documents)

**Overview**: CReSt is a benchmark designed to evaluate Retrieval-Augmented Generation (RAG) systems in complex reasoning scenarios over structured documents, incorporating multiple dimensions such as reasoning capabilities, refusal to answer appropriately, citation accuracy, and understanding of document structure.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Korean

**Similar Benchmarks**:
- HotpotQA
- FEVER
- KILT

**Resources**:
- [GitHub Repository](https://github.com/UpstageAI/CReSt)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for evaluating the capabilities necessary for practical RAG applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Documents sourced from Common Crawl and National Assembly Library of Korea.

**Size**: 2,245 examples

**Format**: JSON

**Annotation**: Manual annotation by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Unified Score
- Citation Precision
- Citation Recall

**Calculation**: Metrics are derived from the evaluation of answers against a gold standard using external LLMs for semantic equivalence.

**Interpretation**: Scores reflect both correctness and the ability to identify citations accurately.

**Baseline Results**: Performance evaluated using multiple state-of-the-art models including GPT-4o and Qwen2.5 series.

**Validation**: Each QA pair is verified through human assessment of correctness and evidence alignment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
