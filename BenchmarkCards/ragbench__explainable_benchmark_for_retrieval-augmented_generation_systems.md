# RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems

## 📊 Benchmark Details

**Name**: RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems

**Overview**: RAGBench is the first comprehensive, large-scale RAG benchmark dataset of 100k examples. It covers five unique industry-specific domains and various RAG task types, sourced from industry corpora such as user manuals, and formalizes the TRACe evaluation framework for explainable RAG evaluation metrics.

**Data Type**: text

**Domains**:
- Biomedical Research
- General Knowledge
- Legal
- Customer Support
- Finance

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/rungalileo/ragbench)
- [GitHub Repository](https://github.com/rungalileo/ragbench/tree/main/ragbench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a comprehensive dataset for training and benchmarking RAG evaluation models, thereby enabling iterative improvements in RAG systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Retrieval-Augmented Generation

**Limitations**: N/A

## 💾 Data

**Source**: The RAGBench dataset is sourced from various open-book Question-Answer datasets and industry-specific corpora for real-world RAG applications.

**Size**: 100,000 examples

**Format**: JSON

**Annotation**: Responses are generated with proprietary LLMs, and the dataset is annotated using LLMs for adherence, relevance, and utilization.

## 🔬 Methodology

**Methods**:
- Automated evaluation using LLMs
- Fine-tuning of DeBERTa model for RAG metrics

**Metrics**:
- Utilization
- Relevance
- Adherence
- Completeness

**Calculation**: Metrics are calculated based on definitions outlined using relevance and utilization evaluations via comprehensively annotated datasets.

**Interpretation**: Higher values for utilization, relevance, and adherence indicate a better performing RAG system with respect to grounding and information fidelity.

**Baseline Results**: Finetuned DeBERTa-based models outperform existing LLM-based evaluation methods.

**Validation**: Involves leveraging the labeled dataset for systematic evaluation against existing RAG evaluation frameworks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack, Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: None of the component datasets contain personally identifiable information or offensive content as stated in the paper.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
