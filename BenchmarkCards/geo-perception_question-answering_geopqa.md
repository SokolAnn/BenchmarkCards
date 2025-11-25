# Geo-Perception Question-Answering (GeoPQA)

## 📊 Benchmark Details

**Name**: Geo-Perception Question-Answering (GeoPQA)

**Overview**: GeoPQA is designed to evaluate the geometric reasoning capabilities of multimodal large language models (MLLMs) by targeting basic geometric concepts and spatial relationships.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DAMO-NLP-SG/GeoPQA)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the perceptual limitations in multimodal language models' geometric reasoning abilities and to establish a benchmark for improving visual perception in geometric contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Geometric Reasoning
- Visual Question Answering

**Limitations**: The accuracy of stage 1 training relies on an LLM judge (GPT-4o-mini) to parse free-form answers, introducing extra cost and time.

## 💾 Data

**Source**: Curated from real and synthetic geometric diagrams.

**Size**: 659 test samples and 5420 training samples

**Format**: JSON

**Annotation**: Generated and filtered using LLMs with a quality verification process.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Question-Answering Evaluation

**Metrics**:
- Accuracy

**Calculation**: The accuracy reward is given only if all perception questions for a given input are correctly answered.

**Interpretation**: Higher accuracy indicates better visual perception and reasoning capabilities in models.

**Validation**: Empirical tests conducted on GeoPQA's dataset reveal significant shortcomings of MLLMs in visual perception.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt leaking

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
