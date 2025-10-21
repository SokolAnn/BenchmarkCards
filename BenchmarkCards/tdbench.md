# TDBench

## 📊 Benchmark Details

**Name**: TDBench

**Overview**: TDBench is a benchmark for evaluating Vision Language Models (VLMs) on top-down image understanding, containing 2,000 curated questions designed for assessing various capabilities in interpreting top-down images.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Columbia-ICSL/TDBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of VLMs focusing on top-down image understanding and incorporating reliability metrics for trustworthiness assessment.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification
- Object Localization
- Attribute Recognition
- Object Counting
- Scene Understanding
- Spatial Relationship Analysis
- Hallucination Detection
- Dynamic Temporal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Curated public datasets and synthetic images from the CARLA Simulator.

**Size**: 2,000 questions

**Format**: JSON

**Annotation**: Questions were manually annotated and curated by experts.

## 🔬 Methodology

**Methods**:
- RotationalEval (RE)
- Manual evaluation

**Metrics**:
- Adjusted Accuracy
- Accuracy

**Calculation**: Metrics are calculated based on the proportion of questions a model knows versus those it can guess.

**Interpretation**: Higher performance suggests better visual grounding and knowledge retention.

**Validation**: The benchmark was validated through human review and model filtering for ensuring question quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
