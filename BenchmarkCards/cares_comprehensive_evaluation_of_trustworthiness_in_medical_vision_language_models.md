# CARES (Comprehensive Evaluation of Trustworthiness in Medical Vision Language Models)

## 📊 Benchmark Details

**Name**: CARES (Comprehensive Evaluation of Trustworthiness in Medical Vision Language Models)

**Overview**: CARES is a benchmark designed to evaluate the trustworthiness of Medical Large Vision Language Models (Med-LVLMs) across five dimensions: trustfulness, fairness, safety, privacy, and robustness. It comprises about 41K question-answer pairs covering 16 medical image modalities and 27 anatomical regions.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://cares-ai.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of trustworthiness in Med-LVLMs.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- Domain Experts

**Tasks**:
- Trustworthiness Evaluation
- Medical Diagnosis Assessment

**Limitations**: CARES does not cover all medical image modalities or anatomical sites due to limitations in existing open-source medical data.

## 💾 Data

**Source**: Curated from seven medical multimodal and image classification datasets.

**Size**: 41,000 question-answer pairs and 18,000 images

**Format**: Various formats including closed and open-ended questions

**Annotation**: Constructed using templates and transformations of medical reports and existing datasets.

## 🔬 Methodology

**Methods**:
- Quantitative evaluation using question-answering metrics
- Comparative analysis across multiple models

**Metrics**:
- Accuracy
- Fairness
- Privacy Protection
- Safety Evaluation

**Calculation**: Calculated using the model outputs compared to ground truth responses.

**Interpretation**: Evaluations highlight disparities in model performance across demographic groups and assess the reliability of model responses in clinical contexts.

**Baseline Results**: Existing models exhibit low performance across various metrics, highlighting significant concerns regarding their trustworthiness.

**Validation**: Evaluated based on accuracy and utility in clinical settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**
- **Misuse**

**Demographic Analysis**: Disparities in model performance were observed based on age, gender, and race metrics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Current Med-LVLMs show significant gaps in privacy protection.

**Data Licensing**: The specific licensing of the datasets used is not disclosed.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
