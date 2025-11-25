# CHRO KNOW BENCH

## 📊 Benchmark Details

**Name**: CHRO KNOW BENCH

**Overview**: CHRO KNOW BENCH is a benchmark dataset designed to evaluate chronologically accumulated knowledge across multiple domains and aspects of temporal knowledge, including time dependency and temporal states.

**Data Type**: structured knowledge relations

**Domains**:
- Natural Language Processing
- Biomedical
- Legal
- Computer Science
- Commonsense
- Mathematics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/dmis-lab/ChroKnowledge)

## 🎯 Purpose and Intended Users

**Goal**: To assess the ability of large language models to maintain and accurately recall knowledge over time, considering the dynamism of knowledge across various domains.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Knowledge Evaluation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Various structured datasets across domains including Wikidata, Unified Medical Language System (UMLS), Code of Federal Regulations (CFR), and others.

**Size**: 17,000+ examples

**Format**: Structured triples with timestamps

**Annotation**: Automatically generated with manual verification

## 🔬 Methodology

**Methods**:
- Knowledge Elicitation via Temporal Snapshots
- Sampling-based Evaluation
- Automated metrics for accuracy assessment

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the number of correctly recalled knowledge points compared to a predefined answer set.

**Interpretation**: Higher accuracy indicates a better ability of the model to recall and adapt to temporal knowledge.

**Validation**: Validation through extensive testing across different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
