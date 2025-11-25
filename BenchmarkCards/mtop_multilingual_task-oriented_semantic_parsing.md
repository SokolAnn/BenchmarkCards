# MTOP (Multilingual Task-Oriented Semantic Parsing)

## 📊 Benchmark Details

**Name**: MTOP (Multilingual Task-Oriented Semantic Parsing)

**Overview**: We present a new multilingual dataset, called MTOP, comprising of 100k annotated utterances in 6 languages across 11 domains to facilitate task-oriented semantic parsing.

**Data Type**: annotated utterances

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- French
- Spanish
- Hindi
- Thai

**Resources**:
- [Resource](https://fb.me/mtop_dataset)

## 🎯 Purpose and Intended Users

**Goal**: To scale semantic parsing models for task-oriented dialog systems to new languages effectively and efficiently.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Semantic Parsing

**Limitations**: N/A

## 💾 Data

**Source**: Generated and annotated by crowdsourced workers, with translations and post-processing for six languages.

**Size**: 100,000 examples

**Format**: N/A

**Annotation**: Generated synthetic utterances and annotated in English, followed by translation and label transfer.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match Accuracy
- Slot F1

**Calculation**: Metrics are calculated based on the number of correctly predicted slots and intents compared to ground truth.

**Interpretation**: Higher exact match accuracy and slot F1 indicate better model performance.

**Baseline Results**: Exact match accuracy for best in-language model is 77.7%.

**Validation**: Dataset validated through extensive quality control and annotation revision processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
