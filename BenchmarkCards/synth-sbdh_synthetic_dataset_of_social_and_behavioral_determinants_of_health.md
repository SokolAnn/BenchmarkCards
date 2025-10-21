# Synth-SBDH (Synthetic Dataset of Social and Behavioral Determinants of Health)

## 📊 Benchmark Details

**Name**: Synth-SBDH (Synthetic Dataset of Social and Behavioral Determinants of Health)

**Overview**: Synth-SBDH is a novel synthetic dataset with detailed SBDH annotations, encompassing status, temporal information, and rationale across 15 SBDH categories. It aims to improve SBDH extraction from clinical texts.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MIMIC-SBDH

**Resources**:
- [GitHub Repository](https://github.com/avipartho/Synth-SBDH)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust and comprehensive dataset for the extraction and analysis of social and behavioral determinants of health (SBDH) from clinical text.

**Target Audience**:
- Healthcare Researchers
- NLP Practitioners

**Tasks**:
- Multi-label Classification
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Synth-SBDH dataset generated using GPT-4.

**Size**: 8,767 examples

**Format**: JSON

**Annotation**: Annotations provided by human experts and via machine learning.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F Score
- Micro F Score

**Calculation**: Metrics are calculated based on true positive, false positive, and false negative counts for SBDH categories.

**Interpretation**: A higher macro F score indicates better overall performance across all categories, particularly in detecting rare categories.

**Baseline Results**: Models trained on Synth-SBDH achieved up to 63.75% improvement in macro F scores over counterparts without Synth-SBDH training.

**Validation**: Expert evaluation of a portion of Synth-SBDH was conducted for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for generating biased models due to synthetic data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not resemble any real patient information to mitigate privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
