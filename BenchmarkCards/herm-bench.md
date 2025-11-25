# HERM-Bench

## 📊 Benchmark Details

**Name**: HERM-Bench

**Overview**: HERM-Bench is a benchmark for evaluating the human-centric understanding capabilities of Multimodal Large Language Models (MLLMs), spanning 8 evaluation dimensions including basic perception and complex understanding. It provides a comprehensive assessment of existing MLLMs' abilities in human-centric scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- COCO
- OKVQA
- GQA
- RefCOCO
- RefCOCO+
- RefCOCOg

**Resources**:
- [Resource](https://arxiv.org/abs/2410.06777)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the human-centric understanding capabilities of Multimodal Large Language Models (MLLMs) and identify limitations in their current training data.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: HERM-100K dataset constructed from diverse image sources with multi-level human-centric annotations.

**Size**: 100,000 annotations

**Format**: JSON

**Annotation**: Annotations generated using GPT-4V with diverse image sources.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on normal evaluation scores and IoU for grounding tasks.

**Interpretation**: Higher scores indicate better performance in evaluating human-centric understanding.

**Baseline Results**: Comparison of HERM-7B against various MLLMs on HERM-Bench shows it outperforms all others.

**Validation**: Evaluations were conducted across multiple existing MLLMs to ensure comprehensive assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Inadequate representation of diverse human scenarios due to suboptimal training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
