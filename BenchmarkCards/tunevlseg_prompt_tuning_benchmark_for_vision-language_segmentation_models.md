# TuneVLSeg (Prompt Tuning Benchmark for Vision-Language Segmentation Models)

## 📊 Benchmark Details

**Name**: TuneVLSeg (Prompt Tuning Benchmark for Vision-Language Segmentation Models)

**Overview**: This work presents an open-source benchmarking framework, TuneVLSeg, to integrate various unimodal and multimodal prompt tuning techniques into Vision-Language Segmentation Models (VLSMs), allowing the evaluation of prompt tuning for segmentation tasks across 8 diverse medical datasets and 2 natural-domain datasets.

**Data Type**: segmentation masks

**Domains**:
- Healthcare
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/naamiinepal/tunevlseg)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate various unimodal and multimodal prompt tuning strategies for VLSMs in segmentation tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Image Segmentation

**Limitations**: The study is limited to class-agnostic VLSMs which output binary segmentation masks as classes in downstream tasks may differ from those in the pretrained tasks.

## 💾 Data

**Source**: Includes 8 diverse medical datasets and 2 natural domain datasets.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Dice Score

**Calculation**: The performance of models is calculated using Dice Scores over provided datasets.

**Interpretation**: Higher Dice Scores indicate better segmentation performance.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
