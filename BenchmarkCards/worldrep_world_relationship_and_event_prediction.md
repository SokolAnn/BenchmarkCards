# WORLDREP (WORLD Relationship and Event Prediction)

## 📊 Benchmark Details

**Name**: WORLDREP (WORLD Relationship and Event Prediction)

**Overview**: WORLDREP is a novel dataset designed to predict future international events from textual information, leveraging large-language models for accurate annotation of complex multilateral relationships.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GDELT

**Resources**:
- [GitHub Repository](https://github.com/eogns282/WORLDREP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable dataset that captures complex multilateral relationships and supports research in text-based event prediction.

**Target Audience**:
- ML Researchers
- Political Analysts
- Data Scientists

**Tasks**:
- Event Prediction
- Relationship Labeling

**Limitations**: Despite covering various international events, WORLDREP may miss less-reported incidents.

## 💾 Data

**Source**: Collected from diverse global news articles using GDELT project links.

**Size**: 44,706 articles

**Format**: JSON

**Annotation**: Annotated by domain experts in political science and international relations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Expert labeling
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on expert-provided labels against predictions from the models.

**Interpretation**: Higher scores represent better alignment with expert annotations, indicating more reliable predictions.

**Baseline Results**: Models trained on WORLDREP labels achieved higher performance than those trained on GDELT.

**Validation**: Extensively validated through comparisons with domain expert labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data comprises publicly available news articles, no personal data included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
