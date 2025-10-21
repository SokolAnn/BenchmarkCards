# CSVQA (Chinese STEM Visual Question Answering)

## 📊 Benchmark Details

**Name**: CSVQA (Chinese STEM Visual Question Answering)

**Overview**: CSVQA is a diagnostic multimodal benchmark specifically designed for evaluating scientific reasoning through domain-grounded visual question answering, featuring 1,378 carefully constructed question-answer pairs across diverse STEM disciplines.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Chinese

**Similar Benchmarks**:
- ScienceQA
- MathVista
- MMMU

**Resources**:
- [Resource](https://huggingface.co/datasets/Skywork/CSVQA)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the scientific reasoning capabilities of vision-language models (VLMs) in interpreting STEM content.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: The benchmark currently focuses on high school-level content, which may not fully capture the depth and complexity of advanced scientific reasoning.

## 💾 Data

**Source**: Publicly available Chinese high school textbooks and examination papers across STEM disciplines.

**Size**: 1,378 questions

**Format**: CSV

**Annotation**: Expert-annotated questions, with about 81% paired with detailed explanations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Evaluation of model responses based on correctness and reasoning consistency.

**Interpretation**: A valid response is one that is logically consistent with provided explanations.

**Baseline Results**: Top model achieved 49.6% accuracy.

**Validation**: Validated through expert reviews and quality control pipelines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All content used in the dataset is sourced from publicly available materials, ensuring no private information is included.

**Data Licensing**: Content sourced with explicit permission for use and redistribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Developed in accordance with established ethical standards.
