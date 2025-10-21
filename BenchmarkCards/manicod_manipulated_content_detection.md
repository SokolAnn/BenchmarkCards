# MANICOD (Manipulated Content Detection)

## 📊 Benchmark Details

**Name**: MANICOD (Manipulated Content Detection)

**Overview**: MANICOD is designed for detecting zero-day manipulated content using a dataset of 4,270 pieces of manipulated fake news derived from 2,500 recent real-world news headlines.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cyberooo/manicod)

## 🎯 Purpose and Intended Users

**Goal**: To provide an explainable detector for manipulated content that employs real-time contextual information for accurate classification.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Dataset created from crawling RSS feeds from reputable news sources over 20 days.

**Size**: 4,270 examples

**Format**: N/A

**Annotation**: Manual alteration and review with bias considerations for ensuring the authenticity of manipulated content.

## 🔬 Methodology

**Methods**:
- Knowledge retrieval from online sources
- LLM-based inference

**Metrics**:
- F1 Score

**Calculation**: The F1 score was calculated as 0.856 based on precision and recall measures.

**Interpretation**: Scores above 0.85 indicate strong performance in detecting manipulated content.

**Baseline Results**: Comparison against existing benchmarks shows an up to 1.9x improvement in F1 score.

**Validation**: MANICOD has been validated with a dataset specifically created for evaluating its performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
