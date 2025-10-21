# MULTI-MODAL CelebA-HQ

## 📊 Benchmark Details

**Name**: MULTI-MODAL CelebA-HQ

**Overview**: A large-scale dataset consisting of real face images and corresponding semantic segmentation maps, sketches, and textual descriptions for text-guided image generation and manipulation.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CelebA-HQ
- CUB
- COCO

**Resources**:
- [GitHub Repository](https://github.com/weihaox/TediGAN)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate text-guided multi-modal image synthesis, allowing for diverse face image generation and manipulation.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text-to-Image Generation
- Text-Guided Image Manipulation

**Limitations**: N/A

## 💾 Data

**Source**: Real face images with their corresponding semantic segmentation maps, sketches, and textual descriptions.

**Size**: 30,000 images

**Format**: N/A

**Annotation**: Images are annotated with semantic segmentation maps, sketches, and textual descriptions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- FID
- LPIPS
- Accuracy
- Realism

**Calculation**: Metrics are calculated based on user evaluations of image quality and coherence with text descriptions.

**Interpretation**: Lower FID and LPIPS values indicate better quality, higher accuracy shows better alignment with text.

**Baseline Results**: N/A

**Validation**: Evaluated against existing state-of-the-art methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Multi-category**: Prompt priming

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
