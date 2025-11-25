# HURRICANE SARC

## 📊 Benchmark Details

**Name**: HURRICANE SARC

**Overview**: HURRICANE SARC is a dataset of 15,000 tweets annotated for intended sarcasm in a disaster context, specifically from hurricane events. The dataset enables the investigation of sarcasm detection using pre-trained language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- iSarcasm
- SARC

**Resources**:
- [GitHub Repository](https://github.com/tsosea2/HurricaneSarc)

## 🎯 Purpose and Intended Users

**Goal**: To measure progress on sarcasm detection specifically in the disaster domain and to spur research on understanding sarcasm in online content during critical events.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Sarcasm Detection

**Limitations**: The label distribution in HURRICANE SARC is skewed, with non-sarcastic examples being much more prevalent than sarcastic ones.

## 💾 Data

**Source**: 15,000 tweets sampled from the Twitter data repository during Hurricanes Irma, Harvey, and Maria, annotated using crowdsourcing.

**Size**: 15,000 examples

**Format**: JSON

**Annotation**: Annotated by crowdsourced workers on Amazon Mechanical Turk using majority voting.

## 🔬 Methodology

**Methods**:
- BERTweet
- Bi-LSTM
- CNN

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: F1 Score is calculated based on true positives, false positives, and false negatives for sarcasm detection.

**Interpretation**: High F1 Score indicates better performance of sarcasm detection models.

**Baseline Results**: Best model achieved 0.70 F1 Score.

**Validation**: Models were validated using separate training, validation, and test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
