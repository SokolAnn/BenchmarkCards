# LinguaSafe: A Comprehensive Multilingual Safety Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: LinguaSafe: A Comprehensive Multilingual Safety Benchmark for Large Language Models

**Overview**: LinguaSafe is a comprehensive multilingual safety benchmark crafted with meticulous attention to linguistic authenticity, comprising 45k entries across 12 languages. It addresses the critical need for multilingual safety evaluations of LLMs, filling the void in safety assessment across diverse under-represented languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hungarian
- Malay
- Russian
- Chinese
- Vietnamese
- Arabic
- Korean
- Serbian
- Thai
- Bengali

**Resources**:
- [Resource](https://huggingface.co/datasets/telegraphpolehead/linguasafe)
- [GitHub Repository](https://github.com/telegraph-pole-head/LinguaSafeDatasetsMultilingual)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive suite of metrics for in-depth safety evaluation of multilingual LLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- Ethicists

**Tasks**:
- Safety Evaluation

**Limitations**: The dataset covers 12 languages which is relatively limited compared to other multilingual benchmarks.

## 💾 Data

**Source**: Curated from a mix of translated, transcreated, and natively-sourced data across various online platforms including forums and social media.

**Size**: 45,000 examples

**Format**: N/A

**Annotation**: Annotated by a combination of human annotators and AI with a multi-stage evaluation process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Severity-Weighted Confusion Matrix
- Unsafe Rate
- Oversensitivity Rate

**Calculation**: Metrics are calculated based on collected responses from the models evaluated on safety recognition tasks and oversensitivity scenarios.

**Interpretation**: Results help in assessing the safety alignment of LLMs across different languages and domains.

**Validation**: Validation against existing multilingual safety benchmarks and inter-annotator agreement measures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data processing involves ethical guidelines; potential sources of sensitive content are screened and reviewed.

**Data Licensing**: Released under CC BY-NC-SA 4.0 License (non-commercial, research-only).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
