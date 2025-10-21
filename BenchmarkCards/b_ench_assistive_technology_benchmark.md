# @B ENCH (Assistive Technology Benchmark)

## 📊 Benchmark Details

**Name**: @B ENCH (Assistive Technology Benchmark)

**Overview**: @B ENCH is a pioneering multi-modal benchmark tailored specifically for the domain of Assistive Technology (AT), designed to evaluate Vision-Language Models (VLMs) based on user-defined tasks important for People with Visual Impairments (PVIs). It includes five vital tasks: Panoptic Segmentation, Depth Estimation, Optical Character Recognition (OCR), Image Captioning, and Visual Question Answering (VQA).

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2409.14215)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and standardized evaluation platform for vision-language models in assisting People with Visual Impairments.

**Target Audience**:
- ML Researchers
- Assistive Technology Developers

**Tasks**:
- Panoptic Segmentation
- Depth Estimation
- Optical Character Recognition
- Image Captioning
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: User-centered study involving Participants who are blind or have low vision for task selection based on needs.

**Size**: 15,989,114 samples in total across designated tasks

**Format**: Various, including datasets from Vision Language tasks.

**Annotation**: Data collected and curated based on qualitative feedback from participants.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Panoptic Quality (PQ)
- Root Mean Square Error (RMSE)
- BLEU-1 Score
- CIDEr

**Calculation**: Metrics calculated based on standard evaluation of VLM tasks as defined in benchmark tasks.

**Interpretation**: Higher scores in metrics indicate better performance, with PQ specifically measuring segmentation quality.

**Baseline Results**: Competitive results against state-of-the-art methods as per task benchmarks.

**Validation**: Evaluation of models on curated tasks across multiple real-world datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: Ongoing analysis based on feedback from participants to ensure inclusivity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User anonymity ensured during studies.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all participants.

**Compliance With Regulations**: Not Applicable
