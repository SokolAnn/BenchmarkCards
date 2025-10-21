# MetaWild: A Multimodal Dataset for Animal Re-Identification with Environmental Metadata

## 📊 Benchmark Details

**Name**: MetaWild: A Multimodal Dataset for Animal Re-Identification with Environmental Metadata

**Overview**: MetaWild is a multimodal dataset designed to enable systematic evaluation of metadata integration and multimodal learning in Animal ReID. It pairs images with environmental metadata to enhance animal re-identification performance.

**Data Type**: image with environmental metadata

**Domains**:
- Natural Language Processing
- Computer Vision
- Environmental Sciences

**Languages**:
- N/A

**Similar Benchmarks**:
- NZ-TrailCams

**Resources**:
- [Resource](https://jim-lyz1024.github.io/MetaWild/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the impact of environmental metadata on Animal ReID performance and facilitate the development of multimodal ReID methods based on Vision-Language Models.

**Target Audience**:
- ML Researchers
- Wildlife Conservationists
- Model Developers

**Tasks**:
- Animal Re-Identification

**Limitations**: N/A

## 💾 Data

**Source**: New Zealand Trail Camera dataset (NZ-TrailCams)

**Size**: 20,890 images

**Format**: JSON

**Annotation**: Identity annotations were independently verified by at least three annotators.

## 🔬 Methodology

**Methods**:
- Testing with and without environmental metadata
- Leave-one-domain-out evaluation

**Metrics**:
- Mean Average Precision (mAP)
- Cumulative Match Characteristic at rank 1 (CMC-1)

**Calculation**: Metrics are calculated using standard identity classification and triplet loss functions.

**Interpretation**: Higher mAP and CMC-1 scores indicate better performance in correctly re-identifying animals.

**Baseline Results**: N/A

**Validation**: Validation through comparison of models using visual data only versus combined visual and metadata.

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

**Data Licensing**: Community Data License Agreement – Permissive – Version 1.0. (CDLA-Permissive-1.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
