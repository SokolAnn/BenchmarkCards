# O-Bench

## 📊 Benchmark Details

**Name**: O-Bench

**Overview**: O-Bench is the first visual question answering (VQA) benchmark specifically designed for occlusion perception, containing 4,588 question-answer pairs across five tailored tasks, based on 1,365 images featuring semantically coherent occlusion scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the occlusion perception capabilities of multimodal large language models (MLLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Occlusion Identification
- Binary Relationship Identification
- Gestalt Description
- Gestalt Reasoning
- Occlusion Rate Estimation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed based on the SA-1B dataset.

**Size**: 1,365 images and 4,588 question-answer pairs

**Format**: N/A

**Annotation**: Annotated through a reliable, semi-automatic workflow with five expert annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Measured as the arithmetic mean of individual accuracies across the five tasks.

**Interpretation**: The overall performance indicates how well MLLMs can perceive and reason about occlusion scenarios.

**Baseline Results**: Human performance baseline averaged to 84.8%

**Validation**: Validated by extensive evaluation against human performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
