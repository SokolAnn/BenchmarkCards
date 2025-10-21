# MENTAL MANIP

## 📊 Benchmark Details

**Name**: MENTAL MANIP

**Overview**: MENTAL MANIP is a dataset consisting of 4,000 annotated movie dialogues for the fine-grained analysis of mental manipulation in conversations, designed to assist in the detection and classification of manipulative language and the vulnerabilities targeted in victims.

**Data Type**: dialogue

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Dreaddit
- SDCNL
- ToxiGen
- DetexD
- Fox News
- TalkDown
- ToxiChat
- MDRDC

**Resources**:
- [GitHub Repository](https://github.com/audreycs/MentalManip)

## 🎯 Purpose and Intended Users

**Goal**: To identify and classify mental manipulation in dialogues for better understanding and mitigation of its impact in conversations.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Social Scientists

**Tasks**:
- Classification of manipulative dialogues
- Detection of manipulation techniques
- Identification of targeted vulnerabilities

**Limitations**: N/A

## 💾 Data

**Source**: Cornell Movie Dialogs Corpus

**Size**: 4,000 dialogues

**Format**: CSV

**Annotation**: Annotated by 17 college students through a multi-level taxonomy involving extensive guidelines and training

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated using standard classification evaluations based on predictions vs. true labels.

**Interpretation**: Higher scores in accuracy, precision, and recall indicate better model performance on identifying manipulation.

**Baseline Results**: N/A

**Validation**: Evaluated through inter-annotator agreement scores and model performance on test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: The dataset includes sensitive content which poses risks if used for malicious purposes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
