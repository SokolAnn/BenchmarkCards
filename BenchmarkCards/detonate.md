# DETONATE

## 📊 Benchmark Details

**Name**: DETONATE

**Overview**: DETONATE is a large-scale benchmark designed to stress-test alignment in text-to-image (T2I) models through fine-grained, adversarial evaluation. The dataset comprises approximately 100K curated image pairs across race, gender, and disability axes, sourced from hate speech datasets.

**Data Type**: image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To advance alignment in text-to-image generation models through a robust evaluation framework that accounts for social biases.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text-to-Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: Hate speech datasets curated from publicly available sources, focusing on controversial social axes.

**Size**: 100,000 image pairs

**Format**: N/A

**Annotation**: Human-verified preferences based on toxicity assessments and classification of images as hateful or non-hateful.

## 🔬 Methodology

**Methods**:
- Preference-based optimization
- Human evaluation
- Automated metrics

**Metrics**:
- Alignment Quality Index (AQI)

**Calculation**: Based on clustering and geometric distance metrics to assess separability of aligned and misaligned representations.

**Interpretation**: Higher AQI values indicate better separation between safe and unsafe activations in the representation space.

**Validation**: Empirical evaluations reveal AQI scores and various statistical validations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
