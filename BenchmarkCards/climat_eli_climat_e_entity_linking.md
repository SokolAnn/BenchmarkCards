# CLIMAT ELI (CLIMAT e Entity LInking)

## 📊 Benchmark Details

**Name**: CLIMAT ELI (CLIMAT e Entity LInking)

**Overview**: CLIMAT ELI is the first manually annotated climate change dataset that links 3,087 entity spans to Wikipedia, designed to evaluate existing entity linking (EL) systems on climate change topics across various genres.

**Data Type**: entity linking annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mainlp/ClimatELI)
- [Resource](https://arxiv.org/abs/2406.16732)

## 🎯 Purpose and Intended Users

**Goal**: To provide a manually annotated corpus for evaluating entity linking on climate change data across various genres.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Entity Linking

**Limitations**: The dataset is limited to English, and does not support nested entity linking.

## 💾 Data

**Source**: Manually annotated from ten English documents across five genres including Wikipedia pages, academic articles, web news, UN reports, and YouTube transcriptions.

**Size**: 3,087 entity links across 12,802 tokens

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on the agreement between human annotators and model predictions.

**Interpretation**: Higher precision and recall indicate better performance in linking entities accurately.

**Baseline Results**: Wikifier shows the best performance for both untyped and typed F1 scores among the evaluated models.

**Validation**: Evaluated through inter-annotator agreement checks

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
