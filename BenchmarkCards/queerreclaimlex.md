# QueerReclaimLex

## 📊 Benchmark Details

**Name**: QueerReclaimLex

**Overview**: QueerReclaimLex is a curated dataset of statements containing reclaimed LGBTQ+ slurs, created to facilitate analyses related to gender-queer dialect biases in language models, particularly for harmful speech detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/rebedorn/QueerReclaimLex)

## 🎯 Purpose and Intended Users

**Goal**: To investigate bias in harmful speech classification of gender-queer dialect online and inform the development of equitable content moderation practices.

**Target Audience**:
- ML Researchers
- Content Moderation Practitioners
- LGBTQ+ Advocates

**Tasks**:
- Harmful Speech Detection

**Limitations**: N/A

## 💾 Data

**Source**: Curated templates based on real-world uses of reclaimed slurs in tweets sourced from the NB-TwitCorpus3M dataset.

**Size**: 109 templates

**Format**: Text

**Annotation**: Annotated by gender-queer individuals for subjective harm assessments and pragmatic use types.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on model performance when identifying harmful speech in relation to the author’s identity.

**Interpretation**: High F1 scores indicate better model performance in accurately detecting harmful slur usage.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Annotations were provided by a diverse group of gender-queer individuals, reflecting a range of identities and perspectives.

**Potential Harm**: ['Perpetuation of bias against gender-queer populations through automated content moderation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent was obtained from gender-queer annotators for their participation in the study.

**Compliance With Regulations**: Not Applicable
