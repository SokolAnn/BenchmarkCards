# Beyond Metrics: Evaluating LLMs’ Effectiveness in Culturally Nuanced, Low-Resource Real-World Scenarios

## 📊 Benchmark Details

**Name**: Beyond Metrics: Evaluating LLMs’ Effectiveness in Culturally Nuanced, Low-Resource Real-World Scenarios

**Overview**: This paper evaluates the performance of seven leading LLMs in sentiment analysis on a novel dataset derived from multilingual and code-mixed WhatsApp chats, focusing on cultural nuances and decision-making transparency.

**Data Type**: sentiment analysis messages

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Swahili
- Sheng

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess the effectiveness of LLMs in sentiment analysis within culturally nuanced, low-resource environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Sentiment Analysis

**Limitations**: This study primarily examines texts in Swahili, English, Sheng, and their code-mixed variants, overlooking the vast array of global languages. The focus on seven specific LLMs provides insights but excludes other emerging LLMs.

## 💾 Data

**Source**: The dataset was derived from multilingual exchanges in WhatsApp groups among young people living with HIV in Nairobi, Kenya.

**Size**: 3,719 messages

**Format**: N/A

**Annotation**: The data is annotated with sentiment and word-level language identification.

## 🔬 Methodology

**Methods**:
- Quantitative analysis using F1 score
- Qualitative analysis of model explanations

**Metrics**:
- F1 Score

**Calculation**: The weighted F1 score is used to evaluate performance due to the skew in the dataset.

**Interpretation**: F1 score indicates model performance in accurately detecting sentiment, especially in heavily imbalanced datasets.

**Validation**: Models were prompted with structured instructions for sentiment classification and justification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The analysis includes demographic considerations on the impact of language and cultural nuances in sentiment detection.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data was anonymized to protect participant privacy and ethical guidelines were strictly followed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants signed consent forms outlining study procedures and data anonymization measures.

**Compliance With Regulations**: The study adhered to ethical guidelines for research involving human subjects.
