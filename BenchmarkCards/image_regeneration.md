# Image Regeneration

## 📊 Benchmark Details

**Name**: Image Regeneration

**Overview**: We introduce the Image Regeneration task to assess text-to-image models by tasking the T2I model with generating an image according to the reference image, utilizing MLLM to bridge the reference image and text input.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the generative capabilities of text-to-image models through the Image Regeneration task.

**Target Audience**:
- Academic Researchers
- Industry Practitioners

**Tasks**:
- Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: Two regeneration datasets spanning content-diverse and style-diverse evaluation datasets.

**Size**: 200 text-image samples with 10 different styles for style-diverse, 100 samples with 4 different content types for content-diverse.

**Format**: N/A

**Annotation**: Manually collected and normalized using ChatGPT.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CLIP
- DINOv2
- GPT-4V

**Calculation**: Metrics for evaluating the generated images and their similarity to the reference images are computed through CLIP and DINOv2 scores.

**Interpretation**: Higher scores indicate better image quality and alignment with human perception.

**Baseline Results**: CLIP-based metrics and user study ratings.

**Validation**: Validation is done through human evaluations using Likert scale for content consistency and perceptual quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
