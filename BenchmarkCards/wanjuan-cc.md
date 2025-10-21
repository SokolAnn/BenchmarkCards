# WanJuan-CC

## 📊 Benchmark Details

**Name**: WanJuan-CC

**Overview**: WanJuan-CC is a safe and high-quality open-sourced English webtext dataset derived from Common Crawl data, addressing the challenges of constructing large-scale pre-training datasets for language models. It incorporates a comprehensive process for data extraction and quality filtering, yielding 1.0T Tokens of high-quality data.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RefinedWeb

**Resources**:
- [Resource](https://arxiv.org/abs/2402.19282)

## 🎯 Purpose and Intended Users

**Goal**: To provide a safe, high-quality, and open-source dataset for training large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification
- Language Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Common Crawl Data

**Size**: 1.0T Tokens (4.45TB)

**Format**: N/A

**Annotation**: Model-based quality filtering

## 🔬 Methodology

**Methods**:
- Human evaluation
- Quality signal evaluation
- Model evaluation

**Metrics**:
- Perplexity
- Accuracy

**Calculation**: Metrics are calculated using validation datasets and downstream task evaluations.

**Interpretation**: Lower perplexity indicates better data quality; accuracy metrics are used for model performance.

**Validation**: Validation through several metrics including effectiveness, completeness, fluency, and accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Quality

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potentially unsafe content such as toxicity and personally identifiable information (PII) has been filtered out.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data has been filtered to remove content containing personally identifiable information (PII).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
