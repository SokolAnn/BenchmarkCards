# SynthScars

## 📊 Benchmark Details

**Name**: SynthScars

**Overview**: SynthScars is a high-quality and diverse dataset consisting of 12,236 fully synthetic images with human-expert annotations. It features 4 distinct image content types, 3 categories of artifacts, and fine-grained annotations covering pixel-level segmentation, detailed textual explanations, and artifact category labels.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [Resource](https://opendatalab.github.io/LEGION)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for synthetic image detection that supports fine-grained artifact analysis.

**Target Audience**:
- ML Researchers
- Image Forensics Practitioners

**Tasks**:
- Image Forgery Detection
- Artifical Localization
- Image Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: Aggregated synthetic image samples from multiple datasets including RichHF-18K, Chameleon, and FFAA.

**Size**: 12,236 images

**Format**: N/A

**Annotation**: Human-expert annotations with irregular polygon masks, detailed artifact explanations.

## 🔬 Methodology

**Methods**:
- Image Forgery Analysis
- Multimodal Language Model Integration

**Metrics**:
- Mean Intersection over Union (mIoU)
- F1 Score

**Calculation**: Metrics calculated based on the segmentation performance of artifact localization tasks.

**Interpretation**: Higher mIoU and F1 score indicates better artifact localization accuracy in synthetic images.

**Baseline Results**: LEGION outperforms the strongest expert model, PAL4VST, by 10.65 points in F1 score for Object category on SynthScars.

**Validation**: Extensive experiments conducted across multiple benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
