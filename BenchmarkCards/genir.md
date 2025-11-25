# GenIR

## 📊 Benchmark Details

**Name**: GenIR

**Overview**: GenIR is a privacy-safe automated data curation pipeline for image restoration, yielding a dataset of one million high-quality images, serving as a robust training resource for image restoration models.

**Data Type**: high-quality images

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- DIV2K
- Flickr2K
- SUPIR

**Resources**:
- [GitHub Repository](https://github.com/shallowdream204/DreamClear)

## 🎯 Purpose and Intended Users

**Goal**: To generate a large-scale dataset of high-quality images for training robust real-world image restoration models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Restoration

**Limitations**: In situations of severe image degradation, the synthesized texture details may not exist in the ground-truth image.

## 💾 Data

**Source**: Generated using a dual-prompt learning strategy in the GenIR pipeline, repurposing generative priors in pretrained text-to-image models.

**Size**: 1,000,000 images

**Format**: High-resolution images

**Annotation**: Generated with text prompts ensuring no identifiable individuals are included.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- PSNR
- SSIM
- LPIPS
- DISTS
- FID
- NIQE
- MANIQA
- MUSIQ
- CLIPIQA

**Calculation**: Metrics are calculated based on the generated images compared to ground-truth images using reference and no-reference approaches.

**Interpretation**: High values of PSNR, SSIM, NIQE, MANIQA, and MUSIQ indicate better restoration quality, while lower values of LPIPS, DISTS, and FID signify improved performance.

**Baseline Results**: DreamClear outperforms existing image restoration methods across various benchmarks, reflecting significant advancements in real-world image restoration.

**Validation**: Validated through extensive experiments on multiple benchmarks, including both real-world and synthetic datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential risks include privacy information leakage from photographs used in model training.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Implemented measures to ensure no identifiable individuals are included in the generated dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
