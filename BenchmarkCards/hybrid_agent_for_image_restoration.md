# Hybrid Agent for Image Restoration

## 📊 Benchmark Details

**Name**: Hybrid Agent for Image Restoration

**Overview**: HybridAgent integrates multiple restoration modes into a unified image restoration model, employing fast, slow, and feedback restoration agents to optimize user interaction and effectively restore images with various types of distortions.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2503.10120)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified model for image restoration that enhances user interaction and performance on various distortion types.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Restoration

**Limitations**: N/A

## 💾 Data

**Source**: Instruction tuning dataset constructed from images with 10 types of distortions, including noise, motion blur, and others.

**Size**: 100,000 image-text pairs

**Format**: N/A

**Annotation**: Generated and manually annotated.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- PSNR
- SSIM
- LPIPS

**Calculation**: Metrics are calculated based on the image restoration results compared to ground truth images.

**Interpretation**: Higher PSNR and SSIM values indicate better restoration quality; lower LPIPS signifies better perceptual quality.

**Baseline Results**: Performance results compared against several state-of-the-art all-in-one image restoration methods.

**Validation**: Cross-validation on synthetic and real-world datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack, Hallucination
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
