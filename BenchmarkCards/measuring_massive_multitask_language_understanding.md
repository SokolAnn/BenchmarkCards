# MEASURING MASSIVE MULTITASK LANGUAGE UNDERSTANDING

## 📊 Benchmark Details

**Name**: MEASURING MASSIVE MULTITASK LANGUAGE UNDERSTANDING

**Overview**: The benchmark assesses a text model’s multitask accuracy across 57 diverse tasks spanning subjects from elementary mathematics to advanced professional topics. It measures models' extensive world knowledge and problem-solving abilities in a zero-shot and few-shot context.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Social Sciences
- STEM
- Humanities

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- HellaSwag

**Resources**:
- [GitHub Repository](https://github.com/hendrycks/test)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how well text models understand and apply knowledge learned from extensive pretraining across diverse subjects.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Manually collected questions from freely available educational materials, including practice questions for standardized tests.

**Size**: 15,908 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Models' classification accuracy is computed across all examples and tasks.

**Interpretation**: Performance is measured to track state-of-the-art capabilities compared to expert human accuracy.

**Baseline Results**: Random chance accuracy is around 25%, while expert-level accuracy on the most challenging subjects is approximately 89.8%.

**Validation**: A development and validation set are utilized for hyperparameter tuning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation

**Demographic Analysis**: N/A

**Potential Harm**: ['Inadequate knowledge in areas of law and morality could lead to harmful applications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
