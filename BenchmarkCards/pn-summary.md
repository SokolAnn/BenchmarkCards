# pn-summary

## 📊 Benchmark Details

**Name**: pn-summary

**Overview**: The paper introduces a novel dataset named pn-summary for Persian abstractive text summarization, which is publicly available for future research.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Resources**:
- [GitHub Repository](http://github.com/hooshvare/pn-summary)

## 🎯 Purpose and Intended Users

**Goal**: To create an abstractive text summarization framework for the Persian language and compose a new properly formatted dataset for this task.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Crawled articles along with their summaries from 6 different news agency websites.

**Size**: 93,207 documents

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Fine-tuning on the pn-summary dataset
- Using Seq2Seq models

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: The F1 scores on ROUGE metrics are calculated to evaluate the summarization performance.

**Interpretation**: Higher ROUGE F1 scores indicate better summarization performance.

**Baseline Results**: F1 scores: mT5 (R-1: 42.25, R-2: 24.36, R-L: 35.94) and BERT2BERT (R-1: 44.01, R-2: 25.07, R-L: 37.76).

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
