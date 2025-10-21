# HumanSense

## 📊 Benchmark Details

**Name**: HumanSense

**Overview**: HumanSense is a comprehensive benchmark designed to evaluate the human-centered perception and interaction capabilities of Multimodal Large Language Models (MLLMs), focusing on understanding complex human intentions and providing empathetic, context-aware responses.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HumanOmniV2

**Resources**:
- [GitHub Repository](https://github.com/antgroup/HumanSense)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess human-centered capabilities of MLLMs through the HumanSense framework.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Multi-modal Perception
- Contextual Understanding
- Response Strategy

**Limitations**: N/A

## 💾 Data

**Source**: The data is sourced from existing open-source datasets and YouTube videos, including 3,291 video-based questions and 591 audio-based questions.

**Size**: 3,882 questions

**Format**: N/A

**Annotation**: Question-Answer pairs are generated using templates and leveraging annotations and built-in labels from existing datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the model's performance against human baseline responses.

**Interpretation**: Higher scores indicate better performance in understanding and responding to human-centered tasks.

**Baseline Results**: Human evaluators achieve an average accuracy of 87.5% on the benchmark, significantly outperforming current MLLMs.

**Validation**: Validation of QA pairs through manual inspection for correctness and appropriateness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
