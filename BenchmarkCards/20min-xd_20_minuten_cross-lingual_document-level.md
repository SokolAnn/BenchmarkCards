# 20min-XD (20 Minuten Cross-lingual Document-level)

## 📊 Benchmark Details

**Name**: 20min-XD (20 Minuten Cross-lingual Document-level)

**Overview**: 20min-XD is a French-German, document-level comparable corpus of news articles, sourced from the Swiss online news outlet 20 Minuten /20 minutes. The dataset comprises around 15,000 article pairs spanning 2015 to 2024, automatically aligned based on semantic similarity.

**Data Type**: article pairs

**Domains**:
- Natural Language Processing

**Languages**:
- German
- French

**Resources**:
- [Resource](https://huggingface.co/datasets/ZurichNLP/20min-XD)
- [GitHub Repository](https://github.com/ZurichNLP/20min-XD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a cross-lingual document-level dataset for various NLP applications and linguistically motivated studies.

**Target Audience**:
- NLP Researchers
- Linguists

**Tasks**:
- Bitext Mining
- Machine Translation
- Cross-lingual Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: News articles collected from the Swiss news outlet 20 Minuten /20 minutes.

**Size**: 15,000 article pairs

**Format**: JSON

**Annotation**: Automatically aligned based on semantic similarity.

## 🔬 Methodology

**Methods**:
- Automatic article alignment using multilingual embedding models

**Metrics**:
- F1 Score

**Calculation**: F1 Score is calculated based on precision and recall using the alignment of predicted pairs against gold standard pairs.

**Interpretation**: Higher F1 Score indicates better alignment quality between document pairs.

**Validation**: Validated with a manually curated set of article pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is released exclusively for non-commercial scientific research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
