# Continuous-Valued Seed Dataset for Word-Order Typology

## 📊 Benchmark Details

**Name**: Continuous-Valued Seed Dataset for Word-Order Typology

**Overview**: This paper introduces a new seed dataset made up of continuous-valued data for linguistic typology that reflects the variability of language, focusing on word-order typology extracted from the Universal Dependencies corpus.

**Data Type**: proportional linguistic feature data

**Domains**:
- Natural Language Processing

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that better represents linguistic variability and improve performance on NLP tasks that utilize typological information.

**Target Audience**:
- Linguistic Researchers
- Natural Language Processing Practitioners

**Tasks**:
- Linguistic Typology Prediction

**Limitations**: The dataset is small, covering fewer than 100 languages across a limited number of features, which may affect the generalizability of analyses.

## 💾 Data

**Source**: Universal Dependencies (UD) treebank corpus

**Size**: Fewer than 100 languages

**Format**: N/A

**Annotation**: Data extracted from part-of-speech annotations.

## 🔬 Methodology

**Methods**:
- Data Collection
- Regression Analysis

**Metrics**:
- Mean Squared Error
- R2 Score

**Calculation**: Metrics calculated to evaluate the performance of regression models predicting linguistic features.

**Interpretation**: Lower mean squared error indicates better predictive performance; R2 Score closer to 1 shows better fit.

**Baseline Results**: Not specified.

**Validation**: Held-out test set for evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
