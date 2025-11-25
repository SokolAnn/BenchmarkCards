# RoofNet: A Global Multimodal Dataset for Roof Material Classification

## 📊 Benchmark Details

**Name**: RoofNet: A Global Multimodal Dataset for Roof Material Classification

**Overview**: RoofNet is the largest and most geographically diverse novel multimodal dataset to date, comprising over 51,500 samples from 184 geographically diverse sites pairing high-resolution Earth Observation (EO) imagery with curated text annotations for global roof material classification.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [Resource](https://www.kaggle.com/datasets/noellelaw/roofnet)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for roof material classification that supports scalable, AI-driven risk assessment and infrastructure policy planning.

**Target Audience**:
- Researchers
- Policymakers
- Insurance providers
- Urban resilience planners

**Tasks**:
- Classification

**Limitations**: Class imbalance with materials like metal and concrete significantly outnumbering rarer classes such as thatch and polycarbonate.

## 💾 Data

**Source**: Geographically diverse satellite imagery with curated text annotations from various sources including OpenStreetMap.

**Size**: 51,503 samples

**Format**: N/A

**Annotation**: Annotated in collaboration with domain experts.

## 🔬 Methodology

**Methods**:
- Model fine-tuning
- Human-in-the-loop validation

**Metrics**:
- Top-1 accuracy

**Calculation**: Evaluation of models based on classification accuracy across various roof material categories.

**Interpretation**: A higher Top-1 accuracy indicates better performance in correctly classifying roof materials.

**Baseline Results**: Significant accuracy improvements: +39.84% for CLIP ViT-L/14 and +37.95% for RemoteCLIP ViT-L/14.

**Validation**: Held-out test set of 635 unseen images for accuracy evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released for non-commercial research use under the CC BY-NC 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
