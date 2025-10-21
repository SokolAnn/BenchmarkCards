# Reducing Large Language Model Bias with Emphasis on “Restricted Industries”: Automated Dataset Augmentation and Prejudice Quantification

## 📊 Benchmark Details

**Name**: Reducing Large Language Model Bias with Emphasis on “Restricted Industries”: Automated Dataset Augmentation and Prejudice Quantification

**Overview**: This paper proposes a novel, automated mechanism for debiasing large language models through specified dataset augmentation and introduces two new metrics, the mb-index and db-index, to quantify bias specifically within 'restricted industries' where data is limited.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2403.13925)

## 🎯 Purpose and Intended Users

**Goal**: To reduce bias in large language models through automated dataset augmentation and to offer quantitative measures for bias in datasets and models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Bias Measurement
- Dataset Augmentation

**Limitations**: The datasets used to calculate db-index are limited in size and it would be beneficial to test on larger datasets.

## 💾 Data

**Source**: Government reports related to military and classified content.

**Size**: 17,500 entries

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated dataset augmentation
- Quantitative bias measurement

**Metrics**:
- mb-index
- db-index

**Calculation**: The mb-index is calculated as the perplexity multiplied by the stereotype score divided by the number of data entries. The db-index is obtained by calculating cosine similarity between dataset entries and a comparison dataset containing biased and abusive language.

**Interpretation**: A lower mb-index and db-index indicate less bias in the model and dataset respectively.

**Validation**: The methodology is validated through experimental comparison of LLM performance on original vs. augmented datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
