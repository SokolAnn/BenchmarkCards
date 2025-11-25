# HiCUPID (Conversations with User Personal Information Dataset)

## 📊 Benchmark Details

**Name**: HiCUPID (Conversations with User Personal Information Dataset)

**Overview**: HiCUPID is a new benchmark for training and evaluating LLMs as personalized assistants, incorporating multi-faceted challenges of personalized AI assistants and providing an automated evaluation model.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/12kimih/HiCUPID)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate future efforts toward building LLM-powered personalized assistants and to evaluate their customization and personalization abilities.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Personalized Assistant Development
- Quality Assessment of AI Responses

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using GPT-4o from PersonaHub profiles.

**Size**: 1,500 users, 40,000 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated using GPT-4o

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics based on Llama-3.2

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics calculated using human preference evaluations compared with metrics like BLEU and ROUGE-L.

**Interpretation**: Scores are interpreted based on how well model responses align with predefined human preferences for personalization.

**Validation**: Internal validation through comparison of multiple models and evaluation settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Potential for over-reliance on personalized assistants leading to diminished critical thinking.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: HiCUPID uses synthetic data with no real user information, minimizing privacy risks.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
