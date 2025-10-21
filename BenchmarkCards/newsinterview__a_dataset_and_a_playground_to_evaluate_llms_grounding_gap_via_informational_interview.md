# NewsInterview: a Dataset and a Playground to Evaluate LLMs’ Grounding Gap via Informational Interviews

## 📊 Benchmark Details

**Name**: NewsInterview: a Dataset and a Playground to Evaluate LLMs’ Grounding Gap via Informational Interviews

**Overview**: We release a high-quality dataset of 40,000 two-person informational interviews from NPR and CNN, addressing the scarcity of large-scale dialogue data necessary for studying grounding communication.

**Data Type**: transcripts of informational interviews

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/alex2awesome/news-interview-question-generation)

## 🎯 Purpose and Intended Users

**Goal**: To study grounding communication in a naturalistic setting through a large dataset of journalistic interviews.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Limitations**: N/A

## 💾 Data

**Source**: Transcripts collected from NPR and CNN.

**Size**: 40,000 transcripts

**Format**: CSV, JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Qualitative analysis of dialogues

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on alignment of LLM-generated dialogues with human interactions and a discourse analysis framework.

**Interpretation**: Scores indicate the level of grounding communication in dialogues.

**Baseline Results**: N/A

**Validation**: Validation procedures involve manual classification of interview roles by professional journalists.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Societal Impact**: Impact on education: bypassing learning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used in this study are publicly available and do not contain personally identifiable information beyond what has been already made public by the news organizations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
