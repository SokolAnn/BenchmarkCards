# Hostility Detection in UK Politics: A Dataset on Online Abuse Targeting MPs

## 📊 Benchmark Details

**Name**: Hostility Detection in UK Politics: A Dataset on Online Abuse Targeting MPs

**Overview**: This paper presents a dataset of 3,320 English tweets spanning a two-year period, manually annotated for hostility towards UK MPs and targeted identity characteristics, aiming to facilitate the detection of political hostility.

**Data Type**: tweets with hostility and identity annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Agarwal et al. (2021)
- Vidgen and Yasseri (2020)
- Ward and McLoughlin (2020)

**Resources**:
- [Resource](https://zenodo.org/records/10809695)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for the study of hostility towards UK MPs and to evaluate models for hostility detection.

**Target Audience**:
- NLP Researchers
- Political Scientists
- Data Scientists

**Tasks**:
- Binary Hostility Identification
- Multi-class Targeted Identity Type Classification

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from Twitter using Streaming API following accounts of UK MPs.

**Size**: 3,320 tweets

**Format**: CSV

**Annotation**: Manually annotated by experts with guidelines combining definitions for hostility types.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on a 5-fold cross-validation method validating against different sets of annotations.

**Interpretation**: Higher scores indicate better performance at detecting hostility and accurately classifying identity characteristics.

**Baseline Results**: RoBERTa-Hate achieved a macro F1 score of 73.03 for binary hostility detection.

**Validation**: Validation procedures included annotator training and quality control checks during the annotation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: The dataset includes annotations for identity characteristics such as race, gender, and religion.

**Potential Harm**: The dataset aims to detect and understand the nature of online hostility towards politicians, addressing issues of abuse in political discourse.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset uses tweets, which are public; appropriate measures are taken for responsible usage.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
