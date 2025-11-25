# RedNote-Vibe

## 📊 Benchmark Details

**Name**: RedNote-Vibe

**Overview**: RedNote-Vibe is the first longitudinal dataset for social media AIGT analysis, sourced from the Xiaohongshu platform, containing user engagement metrics and timestamps spanning from the pre-LLM period to July 2025. It enables research into the temporal dynamics and user interaction patterns of AI-generated text (AIGT).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/testuser03158/RedNote-Vibe)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to facilitate the study of AI-generated text (AIGT) detection in dynamic social media contexts, particularly focusing on the relationship between linguistic features and user engagement.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- AIGT Classification
- AI Provider Identification
- Model Identification

**Limitations**: N/A

## 💾 Data

**Source**: Social media posts collected from the Xiaohongshu platform (RedNote) spanning from January 2020 to July 2025.

**Size**: 120,000 posts

**Format**: N/A

**Annotation**: The dataset contains user engagement metrics (likes, comments, collections) and timestamps, each post is evaluated to detect AI-generated and human-authored content.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall

**Calculation**: Metrics are calculated based on standard evaluation protocols for classification tasks, including binary and multi-class tasks.

**Interpretation**: Performance measures indicate the effectiveness of detecting AI-generated text across different tasks with varying degrees of granularity.

**Baseline Results**: Baseline models include classical statistics-based methods and model-based methods such as BERT, RoBERTa, and ALBERT.

**Validation**: The dataset was validated through experiments comparing performance across various classifiers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
