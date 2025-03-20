# GAP-Subjective

## 📊 Benchmark Details

**Name**: GAP-Subjective

**Overview**: GAP-Subjective is a modified version of the GAP dataset that includes subjective sentences for evaluating gender bias in coreference resolution.

**Data Type**: Evaluation dataset

**Domains**:
- Natural Language Processing
- Gender Bias Detection

**Languages**:
- English

**Similar Benchmarks**:
- GAP dataset
- Wiki Neutrality Corpus

**Resources**:
- [Resource](GAP-Subjective dataset)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models for gender bias detection in both subjective and objective sentences.

**Target Audience**:
- Researchers
- NLP practitioners

**Tasks**:
- Gender bias detection
- Coreference resolution evaluation

**Limitations**: N/A

**Out of Scope Uses**:
- Non-gender bias related evaluations

## 💾 Data

**Source**: Wikipedia

**Size**: 8,908 ambiguous pronoun-name pairs

**Format**: Dataset includes both subjective and objective sentences

**Annotation**: Human-labeled

## 🔬 Methodology

**Methods**:
- Sequence-to-sequence style transfer
- Thresholding techniques for sentence quality

**Metrics**:
- F1 score
- Gender bias ratio

**Calculation**: Gender bias defined as the ratio of feminine to masculine F1 scores.

**Interpretation**: Model performance assessed based on predictive accuracy and bias.

**Baseline Results**: GAP: Overall F1 = 0.796, GAP-Subjective: Overall F1 = 0.789

**Validation**: Human evaluations showed an increase in subjectivity with a minor decrease in fluency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
