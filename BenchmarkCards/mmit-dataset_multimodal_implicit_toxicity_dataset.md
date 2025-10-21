# MMIT-Dataset (Multimodal Implicit Toxicity Dataset)

## 📊 Benchmark Details

**Name**: MMIT-Dataset (Multimodal Implicit Toxicity Dataset)

**Overview**: The MMIT-Dataset comprises 2,100 multimodal statements and prompts across 7 risk categories and 31 sub-categories to advance the detection of multimodal implicit toxicity.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that facilitates the study and detection of multimodal implicit toxicity in text-image content.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Toxicity Detection

**Limitations**: N/A

## 💾 Data

**Source**: Constructed through collaboration with LVLMs, diffusion models, and human involvement.

**Size**: 2,100 instances

**Format**: N/A

**Annotation**: Manual review by professional annotators, with some automated checks performed using LVLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the predictions made by ShieldVLM and compared to ground truth labels.

**Interpretation**: A safety prediction is considered correct if its predicted label aligns with the ground-truth safety label.

**Baseline Results**: Compared with industry-standard models including OpenAI Multimodal Content Moderation.

**Validation**: Validated using a combination of manual and automatic checks to ensure alignment with safety guidelines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
