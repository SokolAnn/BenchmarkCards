# AstroCaptions

## 📊 Benchmark Details

**Name**: AstroCaptions

**Overview**: AstroCaptions is a novel domain-specific image captioning dataset with a high number of recognizable public figures. It contains 44,115 publicly available NASA archive images, including both very recent photos and old archive pictures from the first Apollo missions, accompanied by captions for image captioning tasks.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/momentslab/AstroCaptions)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the AstroCaptions dataset is to improve image captioning by inserting identified people's names into captions to enhance their factual accuracy and contextual relevance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: NASA archive images and descriptions scraped from public NASA website.

**Size**: 44,115 images

**Format**: N/A

**Annotation**: Captions were derived from public descriptions and enhanced using GPT-4 model.

## 🔬 Methodology

**Methods**:
- Image Captioning
- Face Detection
- Attention Guided Fusion

**Metrics**:
- BLEU
- ROUGE
- CIDEr
- METEOR

**Calculation**: Metrics are calculated based on the degree of semantic overlap between generated captions and reference captions.

**Interpretation**: Higher scores indicate better quality and relevancy of generated image captions.

**Baseline Results**: BLIP2-FlanT5-XXL achieved BLEU score of 0.63 after merging.

**Validation**: Results were validated by comparing model outputs with ground truth and GPT-4 generated captions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['The method may introduce new types of biases based on face detection and identification systems.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper emphasizes the need for consent and caution when using biometric identification technologies.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
