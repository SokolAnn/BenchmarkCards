# AutoGeo-100k

## 📊 Benchmark Details

**Name**: AutoGeo-100k

**Overview**: AutoGeo-100k is a large-scale geometric dataset comprising 100,000 high-quality image-text pairs generated automatically for enhancing geometric understanding in multimodal large language models.

**Data Type**: geometry image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://autogeo-official.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale dataset for training and evaluating multimodal large language models in the domain of geometric reasoning.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Geometric Captioning
- Geometric Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated using AutoGeo framework that incorporates an augmented geometry clause system for automating the creation of geometric images.

**Size**: 100,000 examples

**Format**: N/A

**Annotation**: Automatically generated image descriptions using templates and fine-tuning with language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Fine-tuning of models

**Metrics**:
- Accuracy
- CIDEr
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on model output against ground truth descriptions for geometric images.

**Interpretation**: Higher scores in these metrics indicate better model performance in understanding and captioning geometric images.

**Baseline Results**: Models fine-tuned on AutoGeo-100k show significant improvements over zero-shot settings across multiple metrics.

**Validation**: Performance validated through experiments with well-defined training data volumes and difficulty levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
