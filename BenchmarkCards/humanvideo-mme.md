# HumanVideo-MME

## 📊 Benchmark Details

**Name**: HumanVideo-MME

**Overview**: HumanVideo-MME is a rigorously curated benchmark designed to provide a more holistic evaluation of Multimodal Large Language Models (MLLMs) in human-centric video understanding, encompassing 13 tasks from basic attribute perception to advanced cognitive reasoning across diverse scenarios and video lengths.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HumanVBench
- OpenHumanVid

**Resources**:
- [GitHub Repository](https://github.com/Fantasyele/HumanVideo-MME)
- [Resource](https://fantasyele.github.io/projects/HumanVideo-MME/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate MLLMs on human-centric video understanding by leveraging a diverse range of cognitive tasks and evaluation paradigms.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Attribute Recognition
- Intention Inference
- Causal Reasoning
- Social Relationship Inference

**Limitations**: N/A

## 💾 Data

**Source**: Videos sourced from publicly available datasets including UltraVideo and OpenHumanVid, along with manual collection.

**Size**: 1,200 videos

**Format**: N/A

**Annotation**: Automated question-answer annotation combined with manual quality review.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on task-specific evaluation standards, including multiple-choice and fill-in-the-blank formats.

**Interpretation**: Higher scores indicate better model performance in understanding and reasoning across human-centric video tasks.

**Baseline Results**: Models show high performance in multiple-choice tasks but significantly drop in open-ended questions.

**Validation**: The benchmark validated through both automated filtering and multi-stage human review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
