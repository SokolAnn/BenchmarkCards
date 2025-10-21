# MoHoBench (Multimodal Honest Benchmark)

## 📊 Benchmark Details

**Name**: MoHoBench (Multimodal Honest Benchmark)

**Overview**: MoHoBench is a large-scale benchmark assessing honesty behaviors of Multimodal Large Language Models (MLLMs) through their responses to unanswerable visual questions, consisting of over 12,000 samples.

**Data Type**: visual question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DSTTSD/MoHoBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic assessment of honesty behaviors in MLLMs when faced with visually unanswerable questions.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated using images from COCO and HaloQuest.

**Size**: 12,158 questions

**Format**: JSON

**Annotation**: Questions are verified and filtered through multi-stage processes including human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Refusal Rate
- Refusal Rationality
- General Helpfulness

**Calculation**: Refusal Rate = (Number of refusals) / (Total questions)

**Interpretation**: Higher refusal rates indicate better honesty alignment among MLLMs when faced with unanswerable questions.

**Baseline Results**: Average refusal rate across evaluated models is 21.3%.

**Validation**: Human evaluation confirms model performance across multiple honesty dimensions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Images sourced from COCO and HaloQuest under appropriate licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
