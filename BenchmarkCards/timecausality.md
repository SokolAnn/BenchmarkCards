# TimeCausality

## 📊 Benchmark Details

**Name**: TimeCausality

**Overview**: TimeCausality is a novel benchmark specifically designed to evaluate the causal reasoning ability of Vision-Language Models (VLMs) in the temporal dimension, focusing on real-world, irreversible transformations of objects governed by temporal causality.

**Data Type**: image pairs with reasoning rationales

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/InternLM/lmdeploy)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capacity of VLMs for temporal-causal reasoning using high-quality, human-verified image pairs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Causal Reasoning
- Visual Question Answering

**Limitations**: The scope of temporal causality is extensive; comprehensively covering all facets of causal relationships is inherently challenging.

## 💾 Data

**Source**: Image pairs generated from high-quality wild images sourced from the COCO 2017 validation split.

**Size**: 700 image pairs

**Format**: N/A

**Annotation**: Generated with high quality and human verification.

## 🔬 Methodology

**Methods**:
- Automated evaluation with LLMs
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy calculated for the determination of temporal order; F1 Score calculated for reasoning and inferring scores via free-text responses.

**Interpretation**: Higher scores indicate better performance in determining temporal causality and reasoning accuracy.

**Validation**: Rigorous manual verification process for the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis focused on the reasoning abilities across different Vision-Language Models.

**Potential Harm**: The benchmark aims to highlight the capability gaps in VLMs regarding temporal causal reasoning.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
