# XLRS-Bench (Extreme Large Ultra-High-Resolution Remote Sensing Benchmark)

## 📊 Benchmark Details

**Name**: XLRS-Bench (Extreme Large Ultra-High-Resolution Remote Sensing Benchmark)

**Overview**: XLRS-Bench is a comprehensive benchmark for evaluating the perception and reasoning capabilities of multimodal large language models (MLLMs) in ultra-high-resolution remote sensing (RS) scenarios, integrating 16 sub-tasks across various perceptual and reasoning dimensions.

**Data Type**: ultra-high-resolution remote sensing images with annotations

**Domains**:
- Remote Sensing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- VRS-Bench
- LHRS-Bench

**Resources**:
- [Resource](https://xlrs-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively assess the capabilities of MLLMs in complex remote sensing imagery, highlighting their limitations and indicating future research directions.

**Target Audience**:
- ML Researchers
- Remote Sensing Experts
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Captioning
- Visual Grounding
- Counting
- Scene Classification
- Object Detection
- Anomaly Detection
- Route Planning

**Limitations**: N/A

## 💾 Data

**Source**: 1,400 ultra-high-resolution remote sensing images sourced from detection and segmentation datasets with extensive annotations.

**Size**: 1,400 images (840 at 10,000 x 10,000 resolution)

**Format**: Images in standard visual formats with human-verified annotations.

**Annotation**: Manual annotation with cross-verification by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- F1 Score

**Calculation**: Metrics are computed based on the accuracy of answers in the evaluation tasks, focusing on both perception and reasoning capabilities.

**Interpretation**: Higher scores indicate better performance in perception tasks and reasoning capabilities in the context of remote sensing.

**Baseline Results**: N/A

**Validation**: Cross-validation processes were employed involving multiple human reviewers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
