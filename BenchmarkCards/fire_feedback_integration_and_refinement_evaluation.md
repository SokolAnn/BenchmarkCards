# FIRE (Feedback Integration and Refinement Evaluation)

## 📊 Benchmark Details

**Name**: FIRE (Feedback Integration and Refinement Evaluation)

**Overview**: FIRE is a feedback-refinement dataset consisting of 1.1M multi-turn conversations derived from 27 source datasets, empowering Vision Language Models (VLMs) to refine their responses based on user feedback across diverse tasks.

**Data Type**: multi-turn conversations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DRESS

**Resources**:
- [Resource](https://mm-fire.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of FIRE is to evaluate the feedback-refining capability of VLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Captioning
- Document Understanding
- Math Reasoning
- OCR Reasoning
- Chart Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Derived from 27 diverse source datasets including public datasets.

**Size**: 1.1M conversations

**Format**: N/A

**Annotation**: Generated via simulations between student and teacher models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- CIDEr
- Mean Absolute Error (MAE)

**Calculation**: Metrics are calculated by comparing the refined responses with ground truth answers using established text evaluation techniques.

**Interpretation**: Higher scores indicate better alignment with ground truth and higher quality feedback.

**Baseline Results**: N/A

**Validation**: Evaluated through human and automated assessments on various settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: bypassing learning, Impact on human agency
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
