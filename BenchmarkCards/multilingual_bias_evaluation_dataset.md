# Multilingual Bias Evaluation Dataset

## 📊 Benchmark Details

**Name**: Multilingual Bias Evaluation Dataset

**Overview**: This study constructs a multilingual bias evaluation dataset to assess bias across different languages and experiments with debiasing methods in low-resource settings.

**Data Type**: bias evaluation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Russian
- Indonesian
- Thai

**Similar Benchmarks**:
- CrowS-Pairs

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate model bias in a multilingual setting and investigate the effectiveness of debiasing methods across low-resource languages.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Fairness Researchers

**Tasks**:
- Bias Evaluation
- Debiasing

**Limitations**: The dataset is based on translations from English, which may bias the evaluation process.

## 💾 Data

**Source**: Constructed from the CrowS-Pairs dataset translated into multiple languages.

**Size**: 1,508 examples

**Format**: CSV

**Annotation**: Automated translation with downstream bias evaluation metrics applied.

## 🔬 Methodology

**Methods**:
- Normalized Bias Score (NBS)
- Debiasing Methods Evaluation

**Metrics**:
- Normalized Bias Score (NBS)

**Calculation**: The NBS is calculated based on the likelihood of stereotypical vs. non-stereotypical sentences and standardizes comparison across languages.

**Interpretation**: Lower NBS values indicate lower bias in the evaluated models.

**Validation**: Models were evaluated under controlled conditions to ensure fair comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis includes gender, race-color, nationality, and religion biases.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
