# HIFI-KPI (Hierarchical Financial Key Performance Indicator)

## 📊 Benchmark Details

**Name**: HIFI-KPI (Hierarchical Financial Key Performance Indicator)

**Overview**: HIFI-KPI is a dataset designed to facilitate numerical KPI extraction from unstructured financial text, containing approximately 1.8 million paragraphs and 5 million entities associated with a complex hierarchy based on the iXBRL standard.

**Data Type**: paragraphs and entities

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FiNER
- MultiFin

**Resources**:
- [GitHub Repository](https://github.com/aaunlp/HiFi-KPI)

## 🎯 Purpose and Intended Users

**Goal**: To structure the iXBRL label set for financial data extraction and enable varying levels of granularity in predictions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Named Entity Recognition
- Structured Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Financial filings from public companies (10-Q and 10-K filings) collected between 2017 and 2024.

**Size**: 1.8 million paragraphs, 5 million entities

**Format**: JSON

**Annotation**: Manually curated with expert mappings for HIFI-KPI Lite.

## 🔬 Methodology

**Methods**:
- Text Classification
- Sequence Labeling
- LLM-based Structure Extraction

**Metrics**:
- Precision
- Recall
- Macro F1

**Calculation**: Precision, Recall, and F1 metrics computed based on correctly predicted labels against the ground truth.

**Interpretation**: Higher precision and recall indicate better extraction performance, particularly in labeling financial entities.

**Baseline Results**: Performance varies across tasks with higher granularities yielding better results, particularly in sequence labeling.

**Validation**: Validated against expert-labeled subsets and evaluated using various model approaches.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
