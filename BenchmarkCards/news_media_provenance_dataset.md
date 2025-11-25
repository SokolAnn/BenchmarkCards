# News Media Provenance Dataset

## 📊 Benchmark Details

**Name**: News Media Provenance Dataset

**Overview**: The dataset consists of news articles with provenance-tagged images, designed to assess the relevance of image origin in relation to news articles.

**Data Type**: news articles with provenance-tagged images

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/matybohacek/News-Media-Provenance-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset for evaluating provenance metadata associated with news articles in order to determine the relevance of images used.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Location of Origin Relevance
- Date and Time of Origin Relevance

**Limitations**: N/A

## 💾 Data

**Source**: News article URLs from the Webz.io News Dataset Repository.

**Size**: 637 articles

**Format**: N/A

**Annotation**: Annotated by four trained annotators to simulate provenance metadata.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy was calculated based on the correct identification of image relevance to articles.

**Interpretation**: Higher accuracy indicates better model performance at identifying relevance.

**Validation**: Results were validated across several large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential sensitivity of provenance metadata concerning location and identity of involved individuals.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Embedding provenance metadata may involve sensitive information; privacy measures should be considered.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
