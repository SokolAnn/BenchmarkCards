# Semantic-CC: Boosting Remote Sensing Image Change Captioning via Foundational Knowledge and Semantic Guidance

## 📊 Benchmark Details

**Name**: Semantic-CC: Boosting Remote Sensing Image Change Captioning via Foundational Knowledge and Semantic Guidance

**Overview**: Semantic-CC is a novel change captioning method that integrates foundational knowledge and semantic guidance to enhance the description of changes in remote sensing images. It utilizes bi-temporal image analysis and a multi-task learning framework to produce more accurate and granular change descriptions.

**Data Type**: text

**Domains**:
- Remote Sensing
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LEVIR-CC
- LEVIR-CD

**Resources**:
- [Resource](https://arxiv.org/abs/2407.14032)

## 🎯 Purpose and Intended Users

**Goal**: Enhance the performance of remote sensing image change captioning by utilizing foundational knowledge and semantic guidance.

**Target Audience**:
- Researchers in Remote Sensing
- Natural Language Processing Practitioners

**Tasks**:
- Change Captioning
- Change Detection

**Limitations**: N/A

## 💾 Data

**Source**: LEVIR-CC and LEVIR-CD datasets utilized for training and evaluation.

**Size**: 10,077 image pairs in LEVIR-CC; 637 pairs in LEVIR-CD

**Format**: Image pairs and annotations

**Annotation**: Annotations made by multiple annotators for change descriptions.

## 🔬 Methodology

**Methods**:
- Multi-task learning
- Feature extraction using bi-temporal SAM-based encoder
- Vision-language foundation model for text generation

**Metrics**:
- BLEU Score
- METEOR
- ROUGE-L
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the similarity between generated sentences and reference sentences for caption and based on pixel-level comparisons for change detection.

**Interpretation**: Higher BLEU, METEOR, and ROUGE-L scores indicate better performance in generating accurate and comprehensive change descriptions.

**Validation**: Validated through experiments on LEVIR-C datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
