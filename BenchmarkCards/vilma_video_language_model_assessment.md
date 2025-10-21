# VILMA (Video Language Model Assessment)

## 📊 Benchmark Details

**Name**: VILMA (Video Language Model Assessment)

**Overview**: VILMA is a task-agnostic benchmark designed to evaluate the video-language models (VidLMs) based on their fine-grained visuo-linguistic capabilities and temporal reasoning. It includes proficiency tests that assess basic competencies necessary for solving more complex tasks. VILMA aims to provide a thorough assessment of VidLMs and identify areas for improvement.

**Data Type**: video-caption pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://cyberiada.github.io/ViLMA)

## 🎯 Purpose and Intended Users

**Goal**: To develop a robust zero-shot benchmark for evaluating the linguistic and temporal grounding capabilities of video-language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Temporal Reasoning
- Action Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Curated from various video-language datasets including Something-Something V2, YouCook2, COIN, and RareAct

**Size**: 8,460 instances

**Format**: N/A

**Annotation**: Manual and automatic validation of video-caption pairs, with human assessment for quality control.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pairwise ranking accuracy

**Calculation**: Proportion of samples where video-caption matching score surpasses video-foil matching score.

**Interpretation**: Higher scores indicate better performance in distinguishing between correct captions and foils.

**Baseline Results**: The performance comparison includes results against a random baseline.

**Validation**: Human validation processes involved multiple annotators scoring captions against video content.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
