# VaLLu (Visual Language Learning Universal)

## 📊 Benchmark Details

**Name**: VaLLu (Visual Language Learning Universal)

**Overview**: VaLLu is a meticulously curated benchmark designed to evaluate the cognitive capabilities of large vision-language models (LVLMs). It aims to provide comprehensive evaluation across various types of cognitive tasks, including reasoning and visual-context understanding.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMMU
- MathVista
- Oven
- HallusionBench

**Resources**:
- [Resource](https://sreyan88.github.io/VDGD/)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate the cognitive abilities of LVLMs, focusing on their capacities in reasoning and visual interpretation.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Visual Reasoning
- Information Extraction
- Cognitive Task Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from Oven, MMMU, MMC, MathVista, HallusionBench, MATH-Vision, and MME.

**Size**: 1,500 examples

**Format**: JSONL

**Annotation**: Manually filtered for noisy examples and annotated with expert-provided responses.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation using GPT-4

**Metrics**:
- Helpfulness
- Clarity
- Correctness
- Depth
- Engagement

**Calculation**: Metrics calculated by averaging scores across multiple evaluations.

**Interpretation**: Higher scores indicate better performance across various evaluation criteria.

**Baseline Results**: Performance compared against VCD, OPERA, Woodpecker, among others.

**Validation**: Metrics validated through manual review and statistical analysis of outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under the licenses of original benchmarks sourced.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
