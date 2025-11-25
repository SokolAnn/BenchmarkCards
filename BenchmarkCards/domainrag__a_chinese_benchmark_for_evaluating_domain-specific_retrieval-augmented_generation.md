# DomainRAG: A Chinese Benchmark for Evaluating Domain-specific Retrieval-Augmented Generation

## 📊 Benchmark Details

**Name**: DomainRAG: A Chinese Benchmark for Evaluating Domain-specific Retrieval-Augmented Generation

**Overview**: DomainRAG is designed to evaluate Retrieval-Augmented Generation (RAG) models in a domain-specific context, focusing on college enrollment. It includes six sub-datasets that assess abilities such as conversational RAG, structural information analysis, faithfulness to expert knowledge, denoising, solving time-sensitive problems, and understanding of multi-document interactions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/ShootingWong/DomainRAG)

## 🎯 Purpose and Intended Users

**Goal**: To assess crucial abilities of RAG models in a domain-specific scenario where traditional language models struggle.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Web pages from the admission official website of a Chinese university were crawled with official permission.

**Size**: 14,406 passages

**Format**: Text (HTML and pure text)

**Annotation**: Manually generated and corrected question-answer pairs using LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the comparison of predicted answers to the ground truth answers.

**Interpretation**: Higher scores indicate better performance in answering domain-specific questions.

**Validation**: Performance evaluated across several popular LLMs in domain-specific contexts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
