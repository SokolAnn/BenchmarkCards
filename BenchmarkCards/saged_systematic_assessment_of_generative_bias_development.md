# SAGED (Systematic Assessment of Generative Bias Development)

## 📊 Benchmark Details

**Name**: SAGED (Systematic Assessment of Generative Bias Development)

**Overview**: SAGED is a holistic benchmarking pipeline designed to evaluate biases in language models through a five-stage process, which includes scraping materials, assembling benchmarks, generating responses, extracting numeric features, and diagnosing with disparity metrics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/holistic-ai/SAGED-Bias)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SAGED is to provide a flexible framework for bias detection in language models, allowing for customizable fairness baselines and comprehensive evaluation metrics.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Ethicists

**Tasks**:
- Bias Detection
- Sentiment Analysis

**Limitations**: SAGED focuses on bias assessment for text-based LLMs and does not yet extend to multi-modal systems.

## 💾 Data

**Source**: Data is scraped from diverse sources, including Wikipedia, to create a comprehensive benchmark.

**Size**: 31,500 responses

**Format**: JSON

**Annotation**: Automatically generated through machine learning models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Max Z-score
- Impact Ratio
- Bias Concentration

**Calculation**: Metrics are calculated based on extracted numeric features using generated responses and baseline comparisons.

**Interpretation**: Lower values of metrics indicate less bias, while higher values suggest greater disparity among responses.

**Validation**: Validation is ensured through comprehensive statistical analysis of generated data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
