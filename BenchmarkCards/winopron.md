# WINOPRON

## 📊 Benchmark Details

**Name**: WINOPRON

**Overview**: WINOPRON is a new dataset created to address issues found in the original Winogender Schemas, focusing on evaluation of gender bias in coreference resolution systems with a corrected and more comprehensive set of templates.

**Data Type**: Text

**Domains**:
- Coreference Resolution
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Winogender Schemas
- WinoBias
- WinoNB

**Resources**:
- [GitHub Repository](github.com/uds-lsv/winopron)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate gender bias in coreference resolution systems with a more reliable dataset.

**Target Audience**:
- Researchers in Natural Language Processing
- Coreference Resolution Developers

**Tasks**:
- Coreference resolution evaluation
- Gender bias measurement

**Limitations**: The dataset may not cover all linguistic variability in English.

**Out of Scope Uses**:
- General text classification
- Non-English languages

## 💾 Data

**Source**: Original Winogender Schemas with additional templates.

**Size**: 1440 sentences

**Format**: Textual templates

**Annotation**: Templates verified for grammaticality and unique coreferences.

## 🔬 Methodology

**Methods**:
- Empirical evaluation of coreference resolution models
- Bias evaluation using a novel method

**Metrics**:
- F1 Score
- Accuracy
- Precision
- Recall

**Calculation**: Measured across multiple pronoun sets and grammatical cases.

**Interpretation**: Understanding model performance based on grammatical case effects.

**Validation**: Automatic checks and human verification for grammaticality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data bias
- Evaluation consistency
- Data quality

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: Potential misrepresentation of model capabilities due to bias in training data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data does not contain any personal identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All data creation followed ethical guidelines.
