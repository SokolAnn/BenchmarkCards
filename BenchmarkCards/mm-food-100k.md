# MM-Food-100K

## 📊 Benchmark Details

**Name**: MM-Food-100K

**Overview**: MM-Food-100K is a high-quality, 100,000-sample multimodal food intelligence dataset designed for fine-tuning AI models, featuring diverse dishes and ingredients with rich, multi-level annotations.

**Data Type**: image + textual annotation

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/MM-Food-100K)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality, multimodal food intelligence dataset for fine-tuning AI models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Classification
- Nutritional Estimation
- Recipe Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from a larger 1.2 million corpus collected from 87,000+ contributors.

**Size**: 100,000 examples

**Format**: JSON

**Annotation**: Mixed human and AI annotations with evidence and provenance for auditability.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- R2

**Calculation**: Metrics are calculated based on model performance on validation and test sets.

**Interpretation**: Lower MAE and RMSE indicate better model performance, while higher R2 indicates better fit of the data.

**Baseline Results**: Models fine-tuned on MM-Food-100K significantly outperform original Large Vision-Language Models.

**Validation**: Performance is validated using a stratified split (80/10/10) of data by cuisine and source type.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for bias in data representation across different cuisines.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Datasets released under conditions permitting public research use.

**Consent Procedures**: Contributors were invited with zero upfront payment, focusing on attribution and revenue sharing.

**Compliance With Regulations**: Not Applicable
