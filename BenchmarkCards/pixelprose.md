# PixelProse

## 📊 Benchmark Details

**Name**: PixelProse

**Overview**: PixelProse is a comprehensive dataset of over 16M synthetically generated captions, leveraging vision-language models for detailed and accurate descriptions of images, addressing the weaknesses of existing alt-text datasets.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/google/cld3)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a high-quality dataset for training vision-language models by providing detailed image captions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Captioning
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is sourced from three different web-scraped databases: CommonPool, CC12M, and RedCaps, comprising images and captions.

**Size**: 16,000,000 images

**Format**: N/A

**Annotation**: Automatically generated captions using vision-language models.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Caption Length
- Toxicity Analysis

**Calculation**: Captions generated using Google Gemini 1.0 Pro Vision Model with a focus on detailed descriptions and aesthetic scoring.

**Interpretation**: PixelProse captions average 506 characters, and toxicity levels are significantly lower compared to original captions.

**Baseline Results**: N/A

**Validation**: Manual verification of generated captions against image content.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['Inclusion of biased or toxic content in training data']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: PII redaction steps are integrated into the data processing pipeline.

**Data Licensing**: CC-BY-4.0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
