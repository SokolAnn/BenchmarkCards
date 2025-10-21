# FinAR-Bench (Financial Analysis and Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: FinAR-Bench (Financial Analysis and Reasoning Benchmark)

**Overview**: FinAR-Bench is a task-oriented benchmark dataset for evaluating LLMs in financial fundamental analysis, specifically focusing on financial statement analysis.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/SAIFS-AIHub/FinAR-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' capabilities in financial statement analysis as part of fundamental analysis in finance.

**Target Audience**:
- ML Researchers
- Finance Professionals

**Tasks**:
- Information Extraction
- Indicator Computation
- Logical Reasoning

**Limitations**: LLMs demonstrate limitations in performing precise and reliable financial analysis, particularly with inherent computational inaccuracies.

## 💾 Data

**Source**: Financial statement data of 100 companies from the Shanghai Stock Exchange, collected in XBRL and PDF formats.

**Size**: 100 companies

**Format**: Structured data (XBRL), Unstructured data (PDF)

**Annotation**: Automatically generated from XBRL data; manual extraction for PDF.

## 🔬 Methodology

**Methods**:
- Evaluation of LLM responses using RMS metric
- Tournament-style evaluation using LLM as judge for logical reasoning task

**Metrics**:
- RMS Precision
- RMS Recall

**Calculation**: Metrics are calculated based on the structure and accuracy of generated outputs compared to ground truth.

**Interpretation**: Higher precision and recall indicate a model's better accuracy in performing financial statement analysis tasks.

**Baseline Results**: Various LLMs were assessed with performance varying across tasks, highlighting differences in capabilities.

**Validation**: Validation procedures involve systematic comparisons of generated outputs against expected results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
