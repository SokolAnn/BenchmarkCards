# WIT (Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning)

## 📊 Benchmark Details

**Name**: WIT (Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning)

**Overview**: WIT is a curated dataset composed of 37.6 million image-text examples from 108 Wikipedia languages. It facilitates multimodal, multilingual learning and is used for pretraining multimodal models, particularly for tasks such as image-text retrieval.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- French
- Chinese
- Spanish
- German
- Russian
- Arabic
- Hindi
- Japanese
- Korean

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/wit)

## 🎯 Purpose and Intended Users

**Goal**: To provide the largest multimodal dataset for pretraining and evaluating models in the multilingual space.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Image-Text Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from Wikipedia articles and Wikimedia image links.

**Size**: 37.6 million image-text pairs

**Format**: JSON

**Annotation**: High-quality annotations verified through an extensive human-annotation process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall@K (R@1, R@5)

**Calculation**: Metrics are calculated based on the similarity between image-text pairs using cosine similarity.

**Interpretation**: Higher Recall@K values indicate better performance in retrieving relevant image-text pairs.

**Validation**: Human validation confirmed high-quality image-text associations with 98.5% favorable judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis across 100+ languages with 12K+ examples in each language.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Data extracted from publicly available Wikipedia articles.

**Compliance With Regulations**: Not Applicable
