# MangaZero

## 📊 Benchmark Details

**Name**: MangaZero

**Overview**: MangaZero is a large-scale dataset specifically designed for multi-character, multi-state manga generation, addressing a significant gap in story visualization training data. It contains 43,264 manga pages and 427,147 annotated panels, supporting the visualization of varied character interactions and movements across sequential frames.

**Data Type**: manga panels with annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Japanese

**Similar Benchmarks**:
- Manga109

**Resources**:
- [Resource](https://jianzongwu.github.io/projects/diffsensei/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for customized manga generation, enabling detailed control over character appearances and interactions in manga narratives.

**Target Audience**:
- AI Researchers
- ML Researchers
- Creative Artists

**Tasks**:
- Customized Manga Generation

**Limitations**: N/A

## 💾 Data

**Source**: Downloaded manga pages from online manga websites (MangaDex), annotated with character IDs and other features.

**Size**: 43,264 pages

**Format**: Various image formats

**Annotation**: Annotated with panel bounding boxes, character IDs, and dialog bounding boxes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Fréchet Inception Distance (FID)
- CLIP image-text similarity
- DINO image similarity
- Dialog bounding box F1 score

**Calculation**: Metrics are calculated using standard evaluation methods in generative modeling.

**Interpretation**: Lower FID and higher CLIP scores indicate better image quality and alignment between generated images and text.

**Baseline Results**: Compared against baseline models such as StoryDiffusion, MS-Diffusion, and others.

**Validation**: Model validation supported by human preference studies and automated evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
