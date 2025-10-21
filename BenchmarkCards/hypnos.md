# Hypnos

## 📊 Benchmark Details

**Name**: Hypnos

**Overview**: Hypnos is a Chinese Anesthesia model built upon existing LLMs, introducing a standardized benchmark for evaluating medical LLM performance in Anesthesiology.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating the performance of medical LLMs in Anesthesiology.

**Target Audience**:
- Healthcare Practitioners
- Medical Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The pre-trained model may have biases, errors, and incompleteness in the training process.

## 💾 Data

**Source**: Publicly available instances from the Internet and privately obtained cases from the Hospital.

**Size**: 5,900 multiple-choice questions, 556 Q&A, 50 real anesthesia cases

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE

**Calculation**: Metrics are calculated based on the similarity between model outputs and ground truth answers.

**Interpretation**: Higher scores in evaluation metrics indicate better performance in providing accurate anesthesia knowledge.

**Baseline Results**: Compared with state-of-the-art medical LLMs.

**Validation**: Hypnos outperformed existing models in multiple evaluations, confirming its efficacy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected includes healthcare information; measures to anonymize data may not be fully described.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
