# RJUA-MedDQA: A Multimodal Benchmark for Medical Document Question Answering and Clinical Reasoning

## 📊 Benchmark Details

**Name**: RJUA-MedDQA: A Multimodal Benchmark for Medical Document Question Answering and Clinical Reasoning

**Overview**: RJUA-MedDQA is a comprehensive benchmark for visually-rich medical report understanding in Chinese, focusing on Urology. It contains 2000 real-world Chinese medical report images designed to challenge models in interpreting image content and enabling robust clinical reasoning for medical diagnoses.

**Data Type**: image

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- DocVQA
- TAT-DQA
- SLAKE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To measure progress on image content extractions and clinical reasoning from visually-rich medical documents.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Clinical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the Urology Department Database of Renji Hospital with real-world medical reports.

**Size**: 2,000 images

**Format**: N/A

**Annotation**: Annotated by medical professionals using the Efficient Structural Restoration Annotation (ESRA) method.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L

**Calculation**: Metrics are calculated based on the prediction accuracy of models on various task questions related to medical reports.

**Interpretation**: Higher scores indicate better performance in correctly answering questions based on medical report images.

**Baseline Results**: Baseline models include various LMMs such as Qwen-VL-Plus and GPT-4v, showing significant variability in task performance.

**Validation**: Validation includes automated metrics checks and human evaluations for ensuring correctness in annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset has been anonymized to protect patient privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
