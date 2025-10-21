# MCTB ENCH : M ULTIMODAL COGNITION TOWARDS TEXT-RICH VISUAL SCENES BENCHMARK

## 📊 Benchmark Details

**Name**: MCTB ENCH : M ULTIMODAL COGNITION TOWARDS TEXT-RICH VISUAL SCENES BENCHMARK

**Overview**: MCTBench is introduced to evaluate the cognitive capabilities of Multimodal Large Language Models (MLLMs) through visual reasoning and content-creation tasks in text-rich visual scenes.

**Data Type**: text-rich image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2410.11538)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cognitive capabilities of MLLMs in text-rich visual scenes.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Perception
- Reasoning
- Content Creation

**Limitations**: The dataset primarily focuses on English, limiting generalization to multilingual scenes.

## 💾 Data

**Source**: Approximately 5.2k text-rich images collected from various public datasets and 8.5k rigorously annotated question-answer pairs.

**Size**: 5.2k images and 8.5k question-answer pairs

**Format**: N/A

**Annotation**: Annotations were manually reviewed with guidelines and generated through GPT assistance.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation
- Model-based evaluation

**Metrics**:
- Mean accuracy
- GSB (Good, Same, Bad) metric

**Calculation**: Mean accuracy is calculated for perception and reasoning tasks. GSB metric based on a comparison between model outputs and provided references.

**Interpretation**: Higher mean accuracy indicates better performance in understanding and reasoning tasks.

**Baseline Results**: Various MLLMs, such as GPT-4V and Gemini-Pro, were assessed against MCTBench.

**Validation**: Evaluations included automated checks as well as human validation processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
