# YinYangAlign

## 📊 Benchmark Details

**Name**: YinYangAlign

**Overview**: YinYangAlign is a novel benchmark for evaluating Text-to-Image (T2I) systems across six contradictory alignment objectives, which include balancing adherence to user prompts with artistic freedom and other fundamental tensions in image generation.

**Data Type**: image-caption pairs

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2502.03512)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for T2I systems that balances contradictory objectives.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Text-to-Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: A combination of diverse datasets including MS COCO, Conceptual Captions, FACTIFY 3M, and others tailored for the contradictory alignment objectives.

**Size**: 40,000 high-quality images

**Format**: image files

**Annotation**: Hybrid annotation using Vision-Language Models for automated processes followed by human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Faithfulness Score
- Emotional Impact Score
- Style Difference
- Content Abstraction
- Content Difference
- Cultural Sensitivity Score
- Verifiability Score

**Calculation**: Metrics are calculated based on both automated assessments from Vision-Language Models and manual review by human annotators.

**Interpretation**: High values in various scores indicate strong alignment with the objectives, while lower scores suggest misalignment or insufficient adherence.

**Baseline Results**: N/A

**Validation**: Validation was performed using inter-annotator agreement metrics during the human evaluation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Cultural Sensitivity
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
