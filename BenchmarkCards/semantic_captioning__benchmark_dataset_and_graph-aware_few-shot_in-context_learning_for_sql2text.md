# Semantic Captioning: Benchmark Dataset and Graph-Aware Few-Shot In-Context Learning for SQL2Text

## 📊 Benchmark Details

**Name**: Semantic Captioning: Benchmark Dataset and Graph-Aware Few-Shot In-Context Learning for SQL2Text

**Overview**: This paper introduces semantic captioning as a new task that focuses on translating SQL queries into natural language utterances. It develops the first dataset for semantic captioning using iterative in-context learning (ICL) techniques, contributing to the understanding of code comprehension by large language models (LLMs) and generating meaningful descriptions of SQL queries.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CoSQL
- Spider
- SParC

**Resources**:
- [GitHub Repository](https://github.com/aliwister/ast-icl)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the capacity of LLMs to understand SQL queries by generating natural language descriptions, thereby facilitating better integration into coding and educational platforms.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Semantic Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Repurposed from Three Benchmark Text2SQL Datasets: CoSQL, Spider, and SParC

**Size**: 853 SQL queries and 2559 generated utterances

**Format**: N/A

**Annotation**: Generated using an iterative process with human expert evaluations for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU-4
- BERTScore
- AlignScore

**Calculation**: Metrics were calculated based on both semantic and logical consistency comparisons with original SQL utterances and generated captions.

**Interpretation**: Higher scores indicate better alignment, semantic accuracy, and logical consistency between the generated captions and the SQL queries they represent.

**Baseline Results**: Evaluation revealed strong inter-rater reliability with Fleiss’ Kappa κ= 0.802, demonstrating high-quality caption generation.

**Validation**: The dataset and model performance were assessed through a structured evaluation framework involving human experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
