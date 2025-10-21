# PALLM (Palliative Care Language Model)

## 📊 Benchmark Details

**Name**: PALLM (Palliative Care Language Model)

**Overview**: This study explores the use of large language models (LLMs) to evaluate palliative care communication quality, leveraging simulated scripts created and labeled by healthcare professionals to assess metrics such as understanding, empathy, and emotion.

**Data Type**: simulated clinical conversation scripts

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- CommSense

**Resources**:
- [GitHub Repository](https://github.com/BarnesLab/PALLM/tree/main/scripts)

## 🎯 Purpose and Intended Users

**Goal**: To advance the evaluation and understanding of palliative care communication through the application of large language models.

**Target Audience**:
- Healthcare Professionals
- ML Researchers
- Clinicians

**Tasks**:
- Communication Quality Assessment

**Limitations**: While this foundational study explores the capability of LLMs in evaluating clinical communication, it acknowledges that the created scripts may not provide a comprehensive assessment for real-world clinical interactions.

## 💾 Data

**Source**: Eight simulated clinical communication scripts created and labeled by healthcare professionals to simulate real-world interactions.

**Size**: 8 scripts

**Format**: JSON

**Annotation**: Annotated by clinical team members based on operational rules for understanding, empathy, emotion, presence, and clarity.

## 🔬 Methodology

**Methods**:
- Evaluation using Large Language Models
- Prompt Engineering

**Metrics**:
- Balanced Accuracy
- Precision
- Recall

**Calculation**: Balanced accuracy calculated to account for class imbalances in evaluation of communication metrics.

**Interpretation**: Models accurately classify communication segments as 'Good' or 'Bad' based on established operational rules.

**Baseline Results**: GPT-4 achieved over 90% accuracy in evaluating understanding and empathy metrics.

**Validation**: Results were compared with human expert annotations across evaluated scripts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data usage is in compliance with ethical standards to ensure patient privacy and informed consent.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants in the study were informed and consented to use of simulated scripts for evaluation.

**Compliance With Regulations**: The study adheres to HIPAA standards for the handling of clinical data.
