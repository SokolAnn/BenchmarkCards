# MM-SAP (Self-Awareness in Perception for MLLMs)

## 📊 Benchmark Details

**Name**: MM-SAP (Self-Awareness in Perception for MLLMs)

**Overview**: The MM-SAP benchmark is designed to evaluate the self-awareness of Multimodal Large Language Models (MLLMs) in their capacity to recognize what they can and cannot perceive from images. It integrates a knowledge quadrant framework for a more comprehensive assessment of self-awareness in visual perception.

**Data Type**: visual question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VQAv2
- OKVQA
- A-OKVQA

**Resources**:
- [GitHub Repository](https://github.com/YHWmz/MM-SAP)

## 🎯 Purpose and Intended Users

**Goal**: To define and evaluate the self-awareness of MLLMs in perception, leading to improvements in their reliability and reducing hallucinations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: The benchmark focuses solely on multiple-choice questions, which may oversimplify the complexity of real-world applications involving open-ended questions.

## 💾 Data

**Source**: Compiled from VQAv2, COCO, and Visual Genome datasets, along with manually created questions.

**Size**: 1,200 questions

**Format**: JSON

**Annotation**: Crafted by experts and sourced from existing datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Self-awareness score
- Proportion of knowns answered correctly
- Proportion of unknowns refused

**Calculation**: Self-awareness is evaluated using scores based on answered knowns and properly refused unknowns.

**Interpretation**: A higher self-awareness score indicates better capability of the MLLM to recognize its knowledge limits.

**Validation**: Models were evaluated across different categories of self-awareness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
