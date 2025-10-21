# CoIN (Continual Instruction tuning)

## 📊 Benchmark Details

**Name**: CoIN (Continual Instruction tuning)

**Overview**: CoIN is a comprehensive benchmark tailored for assessing the behavior of existing Multimodal Large Language Models (MLLMs) under continual instruction tuning. It comprises 10 meticulously crafted datasets spanning 8 tasks, ensuring diversity and serving as a robust evaluation framework to assess crucial aspects of continual instruction tuning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zackschen/CoIN)
- [Resource](https://huggingface.co/datasets/Zacks-Chen/CoIN)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively investigate the behavior of MLLMs in continual instruction tuning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering
- Image Classification
- Grounding

**Limitations**: N/A

## 💾 Data

**Source**: Diverse publicly available vision-language datasets like VQAv2, ScienceQA, and ImageNet.

**Size**: 10 datasets spanning 8 tasks

**Format**: JSON

**Annotation**: Automatically generated using scripts for instruction tuning.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Mean Average Accuracy (MAA)
- Backward Transfer (BWT)

**Calculation**: Metrics are calculated based on the outputs of MLLMs in comparison to ground truths and also evaluated for reasoning capabilities.

**Interpretation**: High MAA indicates consistent performance, while lower BWT reflects catastrophic forgetting.

**Validation**: Continual evaluation of MLLMs through diverse tasks and structured instructions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
