# Open-Source Annotated Dataset

## 📊 Benchmark Details

**Name**: Open-Source Annotated Dataset

**Overview**: We collect a human-annotated dataset of thousands of captions and processed video frames from multiple person-centric sources.

**Data Type**: captioned image pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Enable non-rigid edits of human subject scenes, controllable by text, on in-the-wild data and public datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Editing

**Limitations**: The model often fails to preserve the identity of the person being edited.

## 💾 Data

**Source**: Collected from Kinetics, NTU-RGBD, Charades, and Fit3D datasets.

**Size**: 13,487 captioned pairs

**Format**: video frames with captions

**Annotation**: Human annotated captions and processed video frames.

## 🔬 Methodology

**Methods**:
- User study
- Quantitative performance evaluation using FID and PCKh

**Metrics**:
- FID
- PCKh

**Calculation**: Measured due to constraints in evaluating pose preservation and controllability.

**Interpretation**: Higher scores indicate better identity preservation and controllability.

**Baseline Results**: Image-only model results achieve the best FID but lowest identity preservation.

**Validation**: Validated through a user study with machine learning raters assessing multiple images.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for creating misleading content such as deepfakes.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
