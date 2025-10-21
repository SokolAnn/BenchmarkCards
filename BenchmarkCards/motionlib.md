# MotionLib

## 📊 Benchmark Details

**Name**: MotionLib

**Overview**: MotionLib is the first million-level dataset for motion generation, comprising over 1.2 million motion sequences enriched with hierarchical text descriptions, designed to enhance the training of large motion models.

**Data Type**: motion sequences with hierarchical text annotations

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HumanML3D
- Motion-X

**Resources**:
- [Resource](https://beingbeyond.github.io/Being-M0/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale dataset for robust training and testing of motion generation models and to advance the understanding of human motion generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Motion Generation
- Text-to-Motion Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from over 20 million videos from open datasets and online platforms, with over 1.2 million motion sequences and detailed hierarchical annotations.

**Size**: 1.2 million motion sequences

**Format**: N/A

**Annotation**: Automated pseudo-labeling with fine-grained hierarchical text descriptions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- R-Precision
- Frechet Inception Distance (FID)
- Multimodal Distance (MMDist)

**Calculation**: Metrics calculated based on the quality and alignment of generated motions with input text descriptions.

**Interpretation**: Higher R-Precision indicates better alignment of generated motions with text prompts; lower FID scores indicate higher realism of generated motions.

**Baseline Results**: Comparison against state-of-the-art models such as MotionGPT and others.

**Validation**: Evaluated against several tasks including text-to-motion generation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All motion data comes from open-source and online videos with careful review to avoid potential ethical limitations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
