# CERTAINLY UNCERTAIN

## 📊 Benchmark Details

**Name**: CERTAINLY UNCERTAIN

**Overview**: CERTAINLY UNCERTAIN is a dataset of approximately 178K visual question answering instances that encompasses diverse types of uncertainties, based on a novel taxonomy distinguishing between epistemic and aleatoric uncertainty in vision-language AI systems.

**Data Type**: visual question answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2407.01942)

## 🎯 Purpose and Intended Users

**Goal**: To improve AI systems' ability to express uncertainty in responses and acknowledge when they do not know the answer.

**Target Audience**:
- ML Researchers
- AI Developers
- Industry Practitioners

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Automatically synthesized dataset based on fine-grained categories of uncertainty.

**Size**: 178,000 examples

**Format**: N/A

**Annotation**: Automatically generated with prompts to large language models.

## 🔬 Methodology

**Methods**:
- Evaluation on standard metrics including accuracy and F1, plus a new confidence-weighted accuracy.

**Metrics**:
- Confidence-weighted accuracy
- Accuracy
- F1 Score

**Calculation**: Confidence-weighted accuracy weights the accuracy by the probability of the model's prediction.

**Interpretation**: Higher confidence-weighted accuracy indicates better model calibration and performance in uncertain scenarios.

**Baseline Results**: N/A

**Validation**: Dataset validation through quality checks to ensure valid question-answer pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
