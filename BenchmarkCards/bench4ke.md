# Bench4KE

## 📊 Benchmark Details

**Name**: Bench4KE

**Overview**: Bench4KE is an extensible API-based benchmarking system for Knowledge Engineering (KE) automation focused on evaluating tools that generate Competency Questions (CQs) automatically, providing a standardized framework to assess their quality using a curated gold standard dataset.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Knowledge Engineering

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/fossr-project/ontogenia-cini)
- [Resource](https://doi.org/10.5281/zenodo.15397912)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized and extensible evaluation framework for Knowledge Engineering automation tasks, particularly for the generation of Competency Questions.

**Target Audience**:
- Knowledge Engineers
- AI Researchers
- Ontology Developers

**Tasks**:
- Competency Question Generation

**Limitations**: N/A

## 💾 Data

**Source**: Gold standard datasets from four real-world ontology projects combined with user stories and domain-specific datasets.

**Size**: 101 Competency Questions

**Format**: CSV, XML

**Annotation**: Manually crafted by ontology engineers from real-world projects.

## 🔬 Methodology

**Methods**:
- API-based evaluation
- Comparative analysis

**Metrics**:
- Cosine Similarity
- Jaccard Similarity
- BLEU Score
- ROUGE-L
- sBERT
- LLM-based Semantic Scoring

**Calculation**: Metrics are computed by comparing generated CQs against gold standard CQs using various similarity measures.

**Interpretation**: The evaluation results quantify the quality of generated CQs by measuring their semantic similarity to manually crafted CQs.

**Baseline Results**: Comparative performance metrics of four LLM-based CQ generation systems were established.

**Validation**: Bench4KE supports various evaluation scenarios using user stories and structured datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0 License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
