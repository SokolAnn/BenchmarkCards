# EchoBench

## 📊 Benchmark Details

**Name**: EchoBench

**Overview**: EchoBench is the first benchmark specifically designed to systematically evaluate sycophantic tendencies in medical LVLMs, comprising 2,122 medical images across 18 clinical departments, paired with 90 prompts simulating biased inputs.

**Data Type**: medical images and prompts

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/BotaiYuan/Medical_LVLM_Sycophancy)
- [Resource](https://huggingface.co/datasets/Botai666/Medical_VLM_Sycophancy)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of EchoBench is to evaluate sycophantic behaviors in medical LVLMs and provide insights to improve their reliability in clinical settings.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Evaluating sycophantic tendencies in medical language models

**Limitations**: N/A

## 💾 Data

**Source**: 2,122 medical images from real-world datasets spanning various clinical departments.

**Size**: 2,122 images

**Format**: Various image formats based on modality

**Annotation**: Carefully designed prompts simulating biases from patients, medical students, and physicians.

## 🔬 Methodology

**Methods**:
- Empirical evaluation across various medical language models
- Prompt-based evaluation strategies

**Metrics**:
- Sycophancy Rate
- Accuracy

**Calculation**: Sycophancy Rate is calculated based on the percentage of biased prompts the model aligns with, while accuracy is based on correct predictions.

**Interpretation**: Higher sycophancy rates indicate stronger alignment with biased prompts, which may reflect a lack of model reliability.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
