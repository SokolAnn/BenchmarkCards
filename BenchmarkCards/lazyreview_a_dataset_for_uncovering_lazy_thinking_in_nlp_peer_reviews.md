# LAZYREVIEW (A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews)

## 📊 Benchmark Details

**Name**: LAZYREVIEW (A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews)

**Overview**: LAZYREVIEW is a dataset of peer-review sentences annotated with fine-grained lazy thinking categories to help automate the detection of heuristics leading to compromised review quality.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/UKPLab/acl2025-lazy-review)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for detecting lazy thinking in NLP peer reviews and improve review quality through automated methods.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: ARR 2022 reviews collected from the NLP EER Dataset.

**Size**: 1,776 review segments

**Format**: N/A

**Annotation**: Expert-annotated with guidelines developed over three rounds.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Not specifically detailed, but based on direct annotation and LLM assessments.

**Interpretation**: N/A

**Baseline Results**: N/A

**Validation**: The guidelines were validated through inter-annotator agreement, achieving Cohen's κ values of 0.32, 0.36, and 0.48 across annotation rounds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
