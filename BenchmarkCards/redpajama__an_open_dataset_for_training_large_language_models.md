# RedPajama: an Open Dataset for Training Large Language Models

## 📊 Benchmark Details

**Name**: RedPajama: an Open Dataset for Training Large Language Models

**Overview**: The RedPajama datasets, which include RedPajama-V1 and RedPajama-V2, consist of over 100 trillion tokens and address data-related challenges in the development of open-source language models, providing transparency and mechanisms for dataset curation and analysis.

**Data Type**: raw text data

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- French
- Spanish
- Italian

**Similar Benchmarks**:
- C4
- RefinedWeb
- The Pile

**Resources**:
- [Resource](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)
- [Resource](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-V2)

## 🎯 Purpose and Intended Users

**Goal**: To provide training data for large language models and foster research in dataset curation and analysis.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Common Crawl, Wikipedia, Books, arXiv, Stack Exchange

**Size**: 100 trillion tokens

**Format**: JSON Lines

**Annotation**: Various quality signals measured for web data

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of models trained on the RedPajama datasets.

**Interpretation**: Higher quality signals correlate with better model performance across tasks.

**Validation**: Validation procedures included ablation studies showcasing the impact of quality signals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: ODC-By-1.0 and licenses that may apply to constituent parts.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
