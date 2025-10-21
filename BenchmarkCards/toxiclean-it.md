# ToxiClean-IT

## 📊 Benchmark Details

**Name**: ToxiClean-IT

**Overview**: The ToxiClean-IT dataset is constructed for evaluating prompt-image safety in text-to-image generation and enables supervised fine-tuning of Vision-Language Models (VLMs) by providing both textual and visual safety signals.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/KEVIN04087/ToxiClean-IT)

## 🎯 Purpose and Intended Users

**Goal**: To construct a dataset that allows for the training of prompt refinement methods that improve safety in text-to-image (T2I) models while preserving user intent.

**Target Audience**:
- ML Researchers
- AI Developers
- Dataset Curators

**Tasks**:
- Text-to-Image Generation
- Prompt Optimization

**Limitations**: The iterative refinement process increases the computational cost of image generation.

## 💾 Data

**Source**: The ToxiClean-IT dataset is built using a multi-modal LLM to produce high-quality image-text pairs with safety evaluations.

**Size**: 3,390 pairs

**Format**: JSON

**Annotation**: Annotated using off-the-shelf multi-modal LLM.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Reinforcement Learning

**Metrics**:
- Inappropriate Probability (IP)
- Confidence Score (CS)

**Calculation**: Metrics are computed based on the probability of generated images being classified as inappropriate and the confidence scores from classifiers like Q16.

**Interpretation**: Lower inappropriate probability and higher confidence scores indicate better performance in terms of safety.

**Baseline Results**: Methods leveraging the ToxiClean-IT dataset show significant reductions in inappropriate generation compared to traditional methods.

**Validation**: Performance evaluated across multiple T2I models to ensure generalizability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Generation of inappropriate or harmful content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The ToxiClean-IT dataset is released under the Creative Commons Attribution 4.0 (CC BY 4.0) license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
