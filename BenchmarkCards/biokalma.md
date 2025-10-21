# BioKaLMA

## 📊 Benchmark Details

**Name**: BioKaLMA

**Overview**: BioKaLMA is a benchmark dataset facilitating Knowledge-aware Language Model Attribution (KaLMA), which evaluates the ability of language models to generate attributed answers using structured knowledge from knowledge graphs. It includes a unique task design focusing on citation generation from knowledge graphs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/lixinze777/Knowledge-aware-Language-Model-Attribution)

## 🎯 Purpose and Intended Users

**Goal**: To propose a comprehensive evaluation benchmark for Knowledge-aware Language Model Attribution to improve the reliability of language models in generating accurate citations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from biographical data using evolutionary question generation methods and a knowledge graph.

**Size**: 1,085 entries

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall

**Calculation**: Metrics are calculated based on the alignment of generated citations with knowledge from the knowledge graph.

**Interpretation**: Higher scores in metrics indicate better performance of LLMs in generating accurate citations.

**Baseline Results**: N/A

**Validation**: Experimental validation through generated outputs and baseline comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset features a broad demographic variation of subjects, including individuals from 196 countries and 949 cities.

**Potential Harm**: ['Potential harmful input generation if misused.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly available knowledge graphs.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
