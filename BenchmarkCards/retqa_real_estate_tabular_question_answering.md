# RETQA (Real Estate Tabular Question Answering)

## 📊 Benchmark Details

**Name**: RETQA (Real Estate Tabular Question Answering)

**Overview**: RETQA is the first large-scale open-domain Chinese Tabular Question Answering dataset for the Real Estate sector, comprising 4,932 tables and 20,762 question-answer pairs across three major domains: property information, real estate company finance, and land auction information.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- WikiSQL
- WikiTableQuestion
- Spider
- Open-WikiTable
- NQ-TABLES

**Resources**:
- [GitHub Repository](https://github.com/jensenw1/RETQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging resource for TQA research, particularly in handling open-domain, long tables and multi-domain queries.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available real estate data from major Chinese cities, including property transaction data, company financial disclosures, and land auction information.

**Size**: 20,762 question-answer pairs

**Format**: Markdown, SQL, Natural Language

**Annotation**: Automatically generated QA pairs using template-based approaches with human review and inclusion of Spoken Language Understanding (SLU) labels.

## 🔬 Methodology

**Methods**:
- In-context learning
- Fine-tuning a BERT model

**Metrics**:
- Executable Code Ratio (ECR)
- Pass Rate (pass@1)
- Table Exact Match accuracy (Table EM)
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on model outputs against the ground truth data and evaluated using precision and recall based methods.

**Interpretation**: Higher metrics indicate better model performance in answering questions related to tabular data.

**Baseline Results**: Performance comparison with baseline LLMs demonstrates significant improvements with the SLUTQA framework.

**Validation**: Validation conducted through extensive experimental results showing the effectiveness of methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Data poisoning
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
