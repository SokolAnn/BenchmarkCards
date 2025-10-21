# REALM (Real-world Applications of Large Language Models)

## 📊 Benchmark Details

**Name**: REALM (Real-world Applications of Large Language Models)

**Overview**: REALM is a dataset of over 94,000 LLM use cases collected from Reddit and news articles that captures diverse applications of LLMs and the demographics of their users. It provides insights into LLM adoption across different domains.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Social Science
- Human-Computer Interaction

**Languages**:
- English

**Resources**:
- [Resource](https://realm-e7682.web.app/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive understanding of real-world LLM applications and their societal impacts.

**Target Audience**:
- Researchers
- Policy makers
- Industry professionals

**Tasks**:
- Use case analysis
- Trend analysis
- Impact assessment

**Limitations**: The dataset is exclusively derived from Reddit and news articles, excluding other significant platforms such as Twitter and Facebook.

## 💾 Data

**Source**: Collected from Reddit and news articles via NewsAPI and Academic Torrents.

**Size**: 94,000 examples

**Format**: JSON

**Annotation**: Annotated using a systematic pipeline involving expert and automated methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Expert annotation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on the performance of the classification and annotation pipelines.

**Interpretation**: A high recall indicates good identification of use cases despite the low prior prevalence.

**Validation**: Validated through expert annotations achieving high inter-annotator agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: The dataset includes demographic breakdowns based on the professions of users.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data is anonymized to protect personal information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
