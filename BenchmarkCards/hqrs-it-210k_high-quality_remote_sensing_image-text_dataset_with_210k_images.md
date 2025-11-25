# HQRS-IT-210K (High-Quality Remote Sensing Image-Text Dataset with 210K images)

## 📊 Benchmark Details

**Name**: HQRS-IT-210K (High-Quality Remote Sensing Image-Text Dataset with 210K images)

**Overview**: The dataset includes approximately 210,000 RS images and 1.26 million image-text pairs generated through a two-stage captioning method that utilizes advanced large language models for improved description quality.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/YiguoHe/HQRS-210K-and-HQRS-CLIP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality, large-scale image-text paired dataset for advancing research in remote sensing vision-language applications.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Image Captioning
- Image-Text Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Collected from 23 public satellite and UAV imagery datasets.

**Size**: 210,000 images and 1.3 million captions

**Format**: N/A

**Annotation**: Generated using a two-stage framework involving rule-based generation and large language models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L
- CIDEr
- SPICE

**Calculation**: Metrics are calculated based on model performance in various tasks including image captioning and retrieval.

**Interpretation**: Higher scores in metrics indicate better performance in generating high-quality captions and effective retrieval.

**Baseline Results**: N/A

**Validation**: The dataset was validated through ablation studies showing improvement in model performance across various metrics.

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

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
