# TheBlueScrubs-v1

## 📊 Benchmark Details

**Name**: TheBlueScrubs-v1

**Overview**: TheBlueScrubs-v1 is a curated medical dataset derived from the internet, containing over 25 billion medical tokens and designed to train clinical large language models (cLLMs). It addresses the limitations of existing medical datasets by providing a broader range of medical discourse, including both formal and informal content.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- PubMed
- Common Crawl
- UMLS

**Resources**:
- [Resource](https://huggingface.co/datasets/TheBlueScrubs/TheBlueScrubs-v1)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, diverse dataset for training clinical large language models, enabling improved accuracy in biomedical AI applications.

**Target Audience**:
- Medical Researchers
- AI Researchers
- Model Developers

**Tasks**:
- Text Classification
- Synthetic Data Generation
- Misinformation Detection
- Safety Testing

**Limitations**: The dataset may still contain biases or misinformation despite filtering efforts.

## 💾 Data

**Source**: Dataset constructed from SlimPajama, a 627-billion-token deduplicated version of RedPajama, which includes data from Common Crawl, C4, GitHub, books, arXiv, Wikipedia, and Stack Exchange.

**Size**: 25.1 billion tokens

**Format**: Sharded format with text and associated metadata.

**Annotation**: Annotated with medical relevance scores, factual precision scores, safety scores, and cancer-specific labels.

## 🔬 Methodology

**Methods**:
- Logistic Regression for filtering
- LLM-based scoring using Llama 3.1 for quality assessment

**Metrics**:
- AUC
- Medical Probability Score

**Calculation**: Performance assessed via AUC with thresholds set at ≥0.8 for filtering quality.

**Interpretation**: Higher scores indicate greater medical relevance, precision, and safety of the texts.

**Baseline Results**: AUC of approximately 0.95 for classifier performance on external validation.

**Validation**: Validated through comparison with clinical reviews and external benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Ethical Quality

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset emphasizes medical content, particularly focusing on oncology but does not provide detailed demographic breakdowns.

**Potential Harm**: ['Misinformation exposure', 'Bias propagation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All original data sources comply with GDPR and local data protection regulations.

**Data Licensing**: Licensed under the Apache License, Version 2.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
