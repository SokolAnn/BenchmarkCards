# Design2Code

## 📊 Benchmark Details

**Name**: Design2Code

**Overview**: Design2Code is the first real-world benchmark for multimodal code generation from visual designs, containing 484 diverse real-world webpages as test cases and automatic evaluation metrics to assess model performance.

**Data Type**: HTML/CSS code generation from visual design inputs

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- WebSight

**Resources**:
- [Resource](https://arxiv.org/abs/2403.03163)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the capabilities of multimodal large language models in generating functional code from visual webpage designs.

**Target Audience**:
- ML Researchers
- Web Developers
- AI Model Developers

**Tasks**:
- Code Generation
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Real-world webpages curated from the C4 validation set

**Size**: 484 webpages

**Format**: HTML files

**Annotation**: Manually curated and filtered for quality

## 🔬 Methodology

**Methods**:
- Automated Metrics
- Human Evaluation

**Metrics**:
- Block Match
- Text Similarity
- Position Similarity
- Color Similarity
- CLIP Similarity

**Calculation**: Metrics are calculated based on visual similarity and element matching between generated and reference webpages.

**Interpretation**: Higher scores indicate better alignment to the reference webpages in terms of layout and visual fidelity.

**Baseline Results**: Various state-of-the-art models including GPT-4o and Claude 3 for comparison.

**Validation**: Human evaluations confirmed the effectiveness of automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Filtered out webpages containing private or sensitive information during curation.

**Data Licensing**: Dataset is released under ODC-By license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
