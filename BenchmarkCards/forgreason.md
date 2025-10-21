# ForgReason

## 📊 Benchmark Details

**Name**: ForgReason

**Overview**: ForgReason is a dataset dedicated to descriptions of forgery evidences in AI-generated images, curated through collaboration between an LLM-based agent and a team of human annotators to enhance model performance.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Genimage
- ForenSynths

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a refined dataset for training models to detect forgery in AI-generated images and to generate explanations that align with human reasoning.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Forensic Analysis
- Image Forgery Detection

**Limitations**: N/A

## 💾 Data

**Source**: Data is sourced from human annotations and LLM-generated captions for AI-generated images.

**Size**: 2,215 images plus 5,000 real and 1,000 fake images

**Format**: N/A

**Annotation**: Annotations are provided by human annotators along with LLM-generated descriptions focusing on authenticity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based explanations evaluation

**Metrics**:
- Mean Accuracy (mAcc)

**Calculation**: Metrics are calculated based on detection accuracy and user evaluations of explanation quality.

**Interpretation**: Higher scores indicate better detection capability and more comprehensible explanations for users.

**Validation**: Model validation is conducted using two major benchmarks and subjective evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
