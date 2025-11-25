# MultiMM (Multicultural Multimodal Metaphor dataset)

## 📊 Benchmark Details

**Name**: MultiMM (Multicultural Multimodal Metaphor dataset)

**Overview**: MultiMM is a dataset designed for cross-cultural studies of metaphor in Chinese and English, consisting of 8,461 text-image advertisement pairs with fine-grained annotations.

**Data Type**: text-image advertisement pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MultiMET

**Resources**:
- [GitHub Repository](https://github.com/DUTIR-YSQ/MultiMM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for automated multimodal metaphor comprehension across different cultural contexts.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Cultural Studies Scholars

**Tasks**:
- Metaphor Detection
- Sentiment Analysis

**Limitations**: The dataset is currently limited to advertising, which may restrict its applicability to other genres.

## 💾 Data

**Source**: Data collected from commercial and public service advertisements incorporating textual and visual elements.

**Size**: 8,461 pairs

**Format**: CSV

**Annotation**: Expert annotation with multiple raters to identify metaphorical vs. literal, target and source domains and sentiment categories.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Macro Precision
- Macro F1 Score

**Calculation**: Metrics are calculated using standard evaluation techniques for classification tasks.

**Interpretation**: Higher scores indicate better performance in detecting metaphors and sentiment across cultural contexts.

**Baseline Results**: The proposed SEMD model achieves the highest F1 score of 80.16% for metaphor detection and 77.79% for sentiment analysis.

**Validation**: The dataset was validated through strict annotation standards and expert consensus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The dataset includes samples from both Eastern and Western cultures to analyze cultural bias.

**Potential Harm**: The dataset aims to highlight cultural bias in NLP and promote the development of more inclusive language models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
