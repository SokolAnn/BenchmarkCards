# SARLANG-1M (Synthetic Aperture Radar Language Modeling in SAR Image Understanding)

## 📊 Benchmark Details

**Name**: SARLANG-1M (Synthetic Aperture Radar Language Modeling in SAR Image Understanding)

**Overview**: SARLANG-1M is a large-scale benchmark designed for multimodal SAR image understanding, comprising over 1 million high-quality SAR image-text pairs, featuring two key components: SARLANG-1M-Cap for image captioning and SARLANG-1M-VQA for visual question answering, supporting seven key remote sensing applications.

**Data Type**: image-text pairs

**Domains**:
- Remote Sensing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Jimmyxichen/SARLANG-1M)

## 🎯 Purpose and Intended Users

**Goal**: To advance multimodal understanding of SAR images and facilitate the training and evaluation of VLMs on SAR-specific tasks.

**Target Audience**:
- AI Researchers
- Remote Sensing Experts
- Model Developers

**Tasks**:
- Image Captioning
- Visual Question Answering
- Object Identification
- Object Classification
- Instance Counting
- Region Referring
- Object Positioning

**Limitations**: N/A

## 💾 Data

**Source**: Collected from over 59 cities worldwide, integrating images from various public SAR datasets.

**Size**: 1,126,277 samples

**Format**: N/A

**Annotation**: Generated using high-quality text descriptions from SAR experts and automatic processes.

## 🔬 Methodology

**Methods**:
- Fine-tuning of Vision-Language Models
- Manual Review for Annotation Quality

**Metrics**:
- Accuracy
- BLEU Score
- CIDEr
- ROUGE-L

**Calculation**: Metrics are calculated based on the performance of models fine-tuned on the SARLANG-1M benchmark compared against human expert evaluations.

**Interpretation**: Higher scores in metrics indicate better performance of models in interpreting and understanding SAR images.

**Baseline Results**: N/A

**Validation**: Extensive evaluation using mainstream VLMs compared against human expert performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
