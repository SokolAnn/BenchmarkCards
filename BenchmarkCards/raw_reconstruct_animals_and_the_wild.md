# RAW (Reconstruct Animals and the Wild)

## 📊 Benchmark Details

**Name**: RAW (Reconstruct Animals and the Wild)

**Overview**: RAW is a synthetic dataset comprising one million images designed for the task of reconstructing natural scenes containing animals and their environments from single images, facilitating research in computational ethology.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [Resource](https://raw.is.tue.mpg.de/)

## 🎯 Purpose and Intended Users

**Goal**: To enable the reconstruction of natural scenes that include both animals and their environmental context.

**Target Audience**:
- ML Researchers
- Computer Vision Experts
- Ecologists

**Tasks**:
- 3D Reconstruction

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using the Infinigen project tools to create realistic 3D scenes of natural environments.

**Size**: 1,000,000 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Auto-regressive generation with LLM
- Tensor representations for images
- Training with synthetic data

**Metrics**:
- LPIPS
- Cosine Similarity

**Calculation**: Metrics calculated based on perceptual similarity between rendered reconstructions and source images.

**Interpretation**: Lower LPIPS scores indicate better perceptual similarity between generated images and original scenes.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinterpretation of animal behavior due to inaccuracies in data representation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
