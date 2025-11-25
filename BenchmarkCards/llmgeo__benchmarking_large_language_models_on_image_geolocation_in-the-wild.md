# LLMGeo: Benchmarking Large Language Models on Image Geolocation In-the-wild

## 📊 Benchmark Details

**Name**: LLMGeo: Benchmarking Large Language Models on Image Geolocation In-the-wild

**Overview**: We present a new dataset, exclusively sourced from Google Street View, designed to challenge Large Multimodal Models (LMMs) through real-world, in-the-wild random images. This dataset is intended to serve as a robust benchmark for assessing these models’ ability to identify image locations accurately.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/yeyimilk/LLMGeo)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the geolocation capabilities of multimodal language models using a novel image dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Geolocation

**Limitations**: Evaluations were confined to country-level geolocation without extending it to more granular levels, such as state and city identifications.

## 💾 Data

**Source**: Images collected from Google Street View API.

**Size**: 10,826 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Training-free evaluation
- Training-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics evaluated at the country level based on model predictions.

**Interpretation**: Higher accuracy indicates better performance in correctly identifying image geolocations.

**Baseline Results**: Gemini model achieved an accuracy of up to 0.746 using few-shot prompting.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
