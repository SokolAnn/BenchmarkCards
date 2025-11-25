# CliniDial

## 📊 Benchmark Details

**Name**: CliniDial

**Overview**: CliniDial is a naturally emerging multimodal dialogue dataset for team reflection during clinical operations, capturing audio data, simulated physiology signals, and team operations from two camera angles, annotated to understand teamwork.

**Data Type**: multimodal dialogue data

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/MichiganNLP/CliniDial)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that models communications and teamwork during medical operations to facilitate future NLP research.

**Target Audience**:
- Healthcare Researchers
- NLP Researchers

**Tasks**:
- Dialogue Analysis
- Teamwork Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Simulated operation sessions with medical professionals.

**Size**: 6,900 annotated dialogues

**Format**: Transcriptions, audio files, physiological signals

**Annotation**: Manual annotation using a team reflection behavior framework.

## 🔬 Methodology

**Methods**:
- Evaluation of existing LLMs
- Performance metrics comparison

**Metrics**:
- Macro F1 Score
- Micro F1 Score

**Calculation**: Average macro and micro F1 scores across different setups.

**Interpretation**: Higher macro F1 score indicates better overall performance across all classes.

**Baseline Results**: Best-performing model achieves a macro F1 score of 51.09.

**Validation**: Ten-fold cross-validation was used for the dataset.

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

**Privacy And Anonymity**: Privacy measures have been taken; data will not be released without anonymization.

**Data Licensing**: Not Applicable

**Consent Procedures**: Study approved by the Institutional Review Board.

**Compliance With Regulations**: Not Applicable
