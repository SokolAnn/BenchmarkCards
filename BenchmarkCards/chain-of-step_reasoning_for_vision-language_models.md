# Chain-of-Step Reasoning for Vision-Language Models

## 📊 Benchmark Details

**Name**: Chain-of-Step Reasoning for Vision-Language Models

**Overview**: This paper introduces a framework for chain-of-step reasoning, enabling vision-language models to evaluate reasoning step quality accurately and apply effective reinforcement learning and inference-time scaling with fine-grained rewards.

**Data Type**: structured step-wise reasoning samples

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MathVista
- MMM
- M3CoT
- AI2D
- ChartQA

**Resources**:
- [GitHub Repository](https://github.com/baaivision/CoS)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the reasoning capabilities of vision-language models through structured chain-of-step reasoning and fine-grained evaluation methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multimodal Reasoning
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated using prompts to create structured reasoning data from various multimodal datasets.

**Size**: 300,000 samples

**Format**: N/A

**Annotation**: Automatically annotated using Monte Carlo estimation and LLM-as-Judge techniques.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Reinforcement Learning

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of reasoning steps and their alignment with correct answers.

**Interpretation**: Better performance is indicated by higher accuracy rates on reasoning tasks.

**Validation**: N/A

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

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
