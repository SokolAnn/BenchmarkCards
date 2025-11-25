# Comprehensive Benchmark for Radiology Report Generation

## 📊 Benchmark Details

**Name**: Comprehensive Benchmark for Radiology Report Generation

**Overview**: This study presents a comprehensive benchmark to evaluate the performance of instruction-tuned Vision-Language Models (VLMs) in the specialized task of radiology report generation across three low-resource languages: Italian, German, and Spanish.

**Data Type**: radiology report pairs

**Domains**:
- Healthcare

**Languages**:
- Italian
- German
- Spanish

**Resources**:
- [Resource](https://arxiv.org/abs/2505.01096)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the performance of instruction-tuned Vision-Language Models (VLMs) in generating radiology reports in low-resource languages and to determine the effectiveness of language-specific and domain-specific adaptations.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Radiology Report Generation

**Limitations**: The study's scope was limited to a single dataset and three non-English languages, potentially limiting the generalizability of findings.

## 💾 Data

**Source**: IU-Xray dataset consisting of 7,470 chest X-ray images paired with 3,955 radiological reports.

**Size**: 7,470 images and 3,955 reports

**Format**: N/A

**Annotation**: Reports translated from English into Italian, German, and Spanish.

## 🔬 Methodology

**Methods**:
- Systematic evaluation of model performance
- Comparative analysis of models

**Metrics**:
- BLEU-1
- BLEU-2
- BLEU-3
- BLEU-4
- ROUGE-N
- ROUGE-L
- METEOR

**Calculation**: Metrics calculated based on comparisons of generated reports to reference reports to evaluate quality.

**Interpretation**: Higher scores in BLEU and ROUGE metrics indicate better lexical and semantic alignment with reference reports.

**Baseline Results**: N/A

**Validation**: Standard dataset split of 70% for training, 10% for validation, and 20% for testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
