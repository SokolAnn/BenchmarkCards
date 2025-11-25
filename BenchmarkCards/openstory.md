# Openstory++

## 📊 Benchmark Details

**Name**: Openstory++

**Overview**: Openstory++ is a large-scale dataset combining additional instance-level annotations with both images and text for training instance-focused story visualization models. It facilitates automated and scalable methods to generate data for visual storytelling and introduces the Cohere-Bench benchmark framework for evaluating image generation tasks.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Cohere-Bench

**Resources**:
- [Resource](https://openstorypp.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To enhance instance-focused story visualization models by providing contextually coherent frames featuring recurring instances for effective visual storytelling.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-modal generation
- Visual storytelling

**Limitations**: While broad, the Openstory++ dataset may not cover all possible scenarios encountered in visual storytelling.

## 💾 Data

**Source**: Open-domain video datasets, including source data from Pandas-70M and InternVid.

**Size**: 100,000,000 examples and 1,000,000 sequence samples

**Format**: N/A

**Annotation**: Instance-level annotations using models like BLIP2 and YOLO-World.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Semantic alignment
- Instance consistency
- BLEU4

**Calculation**: Metrics are calculated based on similarity scores between generated images and text descriptions, using CLIP and other comparison methods.

**Interpretation**: Higher scores indicate better alignment and consistency between generated images and narrative structures.

**Validation**: Evaluation is performed using a validation set carefully curated to maintain story coherence across frames.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
