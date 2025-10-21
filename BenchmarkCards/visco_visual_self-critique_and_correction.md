# VISCO (Visual Self-Critique and Correction)

## 📊 Benchmark Details

**Name**: VISCO (Visual Self-Critique and Correction)

**Overview**: VISCO is the first benchmark that evaluates the fine-grained critique and correction capabilities of large vision-language models (LVLMs), focusing on their ability to self-improve through critique.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://visco-benchmark.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To analyze and improve the self-improvement capabilities of LVLMs through critique and correction.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Critique Generation
- Answer Correction

**Limitations**: N/A

## 💾 Data

**Source**: Curated from 18 datasets across 8 tasks involving reasoning and perception.

**Size**: 1,645 question-answering pairs with 5,604 annotations

**Format**: JSON

**Annotation**: Dense annotations performed by expert human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- VISCore
- F1 Score

**Calculation**: VISCore is calculated as the geometric mean of F1 scores for answer, step, and explanation critiques.

**Interpretation**: Higher VISCore indicates better performance in critique and correction capabilities.

**Baseline Results**: N/A

**Validation**: Models evaluated on a variety of tasks with metric correlation against human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
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
