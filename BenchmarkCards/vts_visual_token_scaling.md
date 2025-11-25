# VTS (Visual Token Scaling)

## 📊 Benchmark Details

**Name**: VTS (Visual Token Scaling)

**Overview**: VTS (Visual Token Scaling) is a new dataset that facilitates supervised reasoning trajectories (VTS-SFT) and preference-labeled reasoning comparisons (VTS-DPO) for visual reasoning tasks in multi-modal large language models (MLLMs), enabling dynamic and iterative visual inference.

**Data Type**: supervised reasoning trajectories

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Open-DataFlow/vts-v)

## 🎯 Purpose and Intended Users

**Goal**: To enhance multi-step visual reasoning by enabling models to iteratively select visual actions and verify their utility at each step.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Visual Question Answering
- Image-Grounded Dialogue
- Fine-Grained Visual Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated from visual reasoning examples in the LLaVA-OneVision dataset.

**Size**: 315,000 examples

**Format**: JSON

**Annotation**: Automatically generated visual reasoning trajectories with filtering for correctness using LLM-based verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the correctness of generated reasoning trajectories against ground-truth labels.

**Interpretation**: Higher accuracy indicates better performance and reasoning capability of MLLMs.

**Baseline Results**: Results from models using static visual token representation were significantly lower compared to those using VTS.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Negative impacts on model output fairness due to biased reasoning trajectories.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used was filtered to ensure no personal identifiable information was included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data was sourced from publicly available datasets and verified for correctness.

**Compliance With Regulations**: Not Applicable
