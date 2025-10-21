# Mementos

## 📊 Benchmark Details

**Name**: Mementos

**Overview**: Mementos is a benchmark designed to assess Multimodal Large Language Models' (MLLMs) sequential image reasoning abilities through diverse image sequences and associated human-annotated descriptions.

**Data Type**: image sequences

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/umd-huang-lab/Mementos)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the capabilities of Multimodal Large Language Models (MLLMs) in dynamic reasoning across image sequences.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Captioning
- Visual Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Comprises images selected from Daily-life scenarios, Robotics tasks, and Comics, systematically extracted and annotated.

**Size**: 4,761 image sequences

**Format**: N/A

**Annotation**: Human-annotated descriptions capturing sequential events in the images.

## 🔬 Methodology

**Methods**:
- Human evaluation
- GPT-4 assisted metrics

**Metrics**:
- Recall
- Precision
- F1 Score

**Calculation**: Metrics are computed by matching AI-generated and human-annotated keywords.

**Interpretation**: Scores indicating effective recognition of objects and behaviors in images, with higher scores reflecting better reasoning capabilities.

**Baseline Results**: Performance of nine MLLMs evaluated on Mementos.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
