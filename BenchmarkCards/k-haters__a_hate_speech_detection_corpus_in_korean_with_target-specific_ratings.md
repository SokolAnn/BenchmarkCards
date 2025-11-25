# K-HATERS: A Hate Speech Detection Corpus in Korean with Target-Specific Ratings

## 📊 Benchmark Details

**Name**: K-HATERS: A Hate Speech Detection Corpus in Korean with Target-Specific Ratings

**Overview**: This study introduces K-HATERS, a new corpus for hate speech detection in Korean, comprising approximately 192K news comments with target-specific offensiveness ratings. This resource is the largest offensive language corpus in Korean and is the first to offer target-specific ratings on a three-point Likert scale.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Resources**:
- [GitHub Repository](https://github.com/ssu-humane/K-HATERS)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for the development of hate speech detection models in the Korean language.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Hate Speech Detection

**Limitations**: N/A

## 💾 Data

**Source**: Comments posted on news articles from a major news portal in South Korea.

**Size**: 192,158 comments

**Format**: N/A

**Annotation**: Crowdsourced annotation with a detailed guideline for labeling offensiveness levels.

## 🔬 Methodology

**Methods**:
- BERT fine-tuning

**Metrics**:
- Micro F1
- Macro F1
- Fairness metrics

**Calculation**: Metrics are calculated based on the performance of detection models.

**Interpretation**: Higher Micro and Macro F1 scores indicate better performance in detecting hate speech.

**Baseline Results**: N/A

**Validation**: Validation conducted using separate test splits to confirm labeling quality and model effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
