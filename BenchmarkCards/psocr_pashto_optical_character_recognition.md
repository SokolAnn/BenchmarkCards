# PsOCR (Pashto Optical Character Recognition)

## 📊 Benchmark Details

**Name**: PsOCR (Pashto Optical Character Recognition)

**Overview**: This paper evaluates the performance of Large Multimodal Models (LMMs) on Optical Character Recognition (OCR) in the low-resource Pashto language by introducing a dataset comprising one million synthetic images annotated at various levels.

**Data Type**: image

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Pashto

**Resources**:
- [GitHub Repository](https://github.com/zirak-ai/PashtoOCR)
- [Resource](https://huggingface.co/datasets/zirak-ai/PashtoOCR)
- [Resource](https://www.kaggle.com/datasets/drijaz/PashtoOCR)

## 🎯 Purpose and Intended Users

**Goal**: To develop a comprehensive dataset for training and evaluating LMMs on Pashto OCR tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Optical Character Recognition

**Limitations**: The dataset consists solely of computer-generated text and does not include handwritten samples.

## 💾 Data

**Source**: Synthetic generation methods using a curated text corpus collected from various sources including Common Crawl, open-source websites, and previous studies.

**Size**: 1,000,000 images

**Format**: PNG

**Annotation**: Annotated at word, line, and document levels with bounding boxes.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation of models

**Metrics**:
- Character Accuracy
- Word Accuracy
- BLEU Score

**Calculation**: Metrics are calculated based on the character and word transformation needed to match predicted text with ground-truth.

**Interpretation**: Higher scores indicate better OCR performance on the synthetic images.

**Validation**: No pre-training or fine-tuning applied; models evaluated in their original form.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
