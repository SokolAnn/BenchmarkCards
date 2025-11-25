# PALOMA (Perplexity Analysis for Language Model Assessment)

## 📊 Benchmark Details

**Name**: PALOMA (Perplexity Analysis for Language Model Assessment)

**Overview**: PALOMA is a benchmark to measure language model (LM) fit to 546 English and code domains by analyzing perplexity across various data distributions, enabling more accurate evaluation of LMs across different types of textual and programming data.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- C4
- MC4-EN
- WIKITEXT-103
- PENN TREEBANK
- REDPAJAMA
- DOLMA

**Resources**:
- [Resource](https://paloma.allen.ai)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PALOMA is to provide a standardized benchmark for evaluating language model fit across diverse domains, emphasizing the importance of perplexity measurement for scientific comparison.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Language Modeling

**Limitations**: The focus is primarily on English and code data, potentially limiting its applicability to other languages and domains.

## 💾 Data

**Source**: PALOMA consists of 16 sources curated to create language modeling evaluations, including datasets for standard language modeling benchmarks and fine-grained domain evaluations, e.g., from the top 100 subreddits and programming languages.

**Size**: 123,683,201 tokens

**Format**: Plain text

**Annotation**: Automated filtering and metadata curation.

## 🔬 Methodology

**Methods**:
- Perplexity evaluation
- Human evaluation

**Metrics**:
- Perplexity

**Calculation**: Perplexity is calculated per token based on the log likelihood of evaluation data, normalizing the likelihood by the number of tokens in the evaluated documents.

**Interpretation**: Lower perplexity values indicate better model fit to the evaluated domain.

**Baseline Results**: Baseline models include 1 billion parameter LMs pretrained on data sources such as C4, MC4-EN, and others as detailed in the paper.

**Validation**: The benchmark was validated through comparison of perplexity results across different model configurations and domains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Includes analysis of disparities in language model performance on different dialects and communities.

**Potential Harm**: ['Potential for reinforcing biases found in training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
