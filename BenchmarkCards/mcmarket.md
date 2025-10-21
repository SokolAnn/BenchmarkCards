# McMarket

## 📊 Benchmark Details

**Name**: McMarket

**Overview**: McMarket is a large-scale dataset for the task of Multilingual Cross-market Product-based Question Answering (MCPQA), comprising over 7 million questions from 17 marketplaces across 11 languages, designed to enhance question answering in resource-scarce marketplaces by leveraging information from resource-rich auxiliary marketplaces.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- E-commerce

**Languages**:
- English
- Portuguese
- Chinese
- French
- Japanese
- Spanish
- German
- Italian
- Russian
- Arabic
- Hindi

**Similar Benchmarks**:
- xPQA
- AmazonQA
- ReviewRC

**Resources**:
- [GitHub Repository](https://github.com/yfyuan01/MCPQA)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in Multilingual Cross-market Product-based Question Answering by providing a diverse and extensive dataset that supports the exploration of answer generation and question ranking across different marketplaces.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Review-Based Answer Generation
- Product-Related Question Ranking

**Limitations**: The dataset may contain biased or inaccurate information due to user-generated content.

## 💾 Data

**Source**: Amazon product dataset (XMarket) and user-generated reviews from various marketplaces.

**Size**: 7,268,393 questions and 52,469,322 reviews

**Format**: JSON

**Annotation**: Initial labeling is enhanced with auto-labeling using GPT-4, followed by human assessment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- Mean Reciprocal Rank (MRR)
- Precision@3

**Calculation**: Metrics are calculated by comparing model-generated answers with ground truth answers using standard evaluation practices.

**Interpretation**: Higher scores in these metrics indicate better performance of the models on the task.

**Baseline Results**: Models ranging from BM25 to LLaMA-2, showing cross-market methods outperform single-market counterparts.

**Validation**: Benchmarked through experiments comparing performance across different models and settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes diverse demographic factors due to its multilingual and multi-market nature.

**Potential Harm**: The dataset aims to prevent harm related to misinformation in product-related question answering.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information is included in the dataset as it is derived from publicly available data.

**Data Licensing**: Data licensed under CC0 1.0 DEED.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
