# Open-Vocabulary Remote Sensing Image Semantic Segmentation (OVRSISS)

## 📊 Benchmark Details

**Name**: Open-Vocabulary Remote Sensing Image Semantic Segmentation (OVRSISS)

**Overview**: Open-Vocabulary Remote Sensing Image Semantic Segmentation (OVRSISS) aims to segment arbitrary semantic classes in remote sensing images. The work presents a comprehensive dataset named LandDiscover50K, consisting of 51,846 images across 40 diverse semantic classes.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- LoveDA
- iSAID
- FLAIR

**Resources**:
- [GitHub Repository](https://github.com/yecy749/GSNet)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to enable the segmentation of arbitrary semantic classes in remote sensing images without the need for predefined class sets.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Remote Sensing Experts

**Tasks**:
- Semantic Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: Images collected from established RSISS datasets providing pixel-wise annotations including Open Earth Map, LoveDA, Deep Globe Land Cover, SIOR, and SOTA.

**Size**: 51,846 images

**Format**: N/A

**Annotation**: Images are pixel-wise annotated across 40 diverse semantic classes.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Cross-dataset validation

**Metrics**:
- Mean Intersection-over-Union (mIoU)

**Calculation**: mIoU is calculated for pixel-wise segmented results against ground truth.

**Interpretation**: Higher mIoU scores indicate better model performance in semantic segmentation tasks.

**Baseline Results**: GSNet achieved an average mIoU of 31.25 across multiple datasets in comparison to existing methods.

**Validation**: Evaluation performed using multiple existing RSISS datasets to validate the performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
