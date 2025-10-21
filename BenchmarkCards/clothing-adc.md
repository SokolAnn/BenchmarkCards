# Clothing-ADC

## 📊 Benchmark Details

**Name**: Clothing-ADC

**Overview**: The Clothing-ADC dataset comprises a substantial collection of clothing images created using the Automatic Dataset Construction (ADC) pipeline, designed for automated image dataset generation with a focus on mitigating label noise and class imbalance.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- Clothing1M
- iNaturalist
- WebVision

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality image dataset specifically focused on label noise detection, label noise learning, and class-imbalanced learning in a structured manner.

**Target Audience**:
- ML Researchers
- Domain Experts
- Data Scientists

**Tasks**:
- Image Classification
- Label Noise Detection
- Class Imbalanced Learning

**Limitations**: N/A

## 💾 Data

**Source**: Collecting image samples via search engines using the ADC pipeline.

**Size**: 1,076,738 images

**Format**: N/A

**Annotation**: Automatically generated with human verification for cleanliness.

## 🔬 Methodology

**Methods**:
- Automated querying and sample collection from Google Images or Bing Images
- Human evaluation for label correction
- Automated data curation
- Use of existing methods for label error detection

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: F1 Score calculated as the harmonic mean of precision and recall.

**Interpretation**: An F1 Score closer to 1 indicates better performance with fewer misclassified instances.

**Baseline Results**: Results compared against existing methods like CORES, deep k-NN, and others for label noise detection tasks.

**Validation**: Empirical evaluations conducted using a subset of 20,000 samples

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
