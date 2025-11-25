# PRISM Alignment Dataset

## 📊 Benchmark Details

**Name**: PRISM Alignment Dataset

**Overview**: The PRISM Alignment Dataset maps the sociodemographics and stated preferences of 1,500 diverse participants from 75 countries to their contextual preferences and fine-grained feedback in 8,011 live conversations with 21 large language models (LLMs). It aims to enable analyses of subjective and multicultural perspectives on controversial issues, targeting the diversity of human feedback for model alignment.

**Data Type**: dialogue interactions and feedback

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HuggingFace H4 Stack Exchange Preference Dataset
- Stanford Human Preferences Dataset

**Resources**:
- [GitHub Repository](https://github.com/HannahKirk/prism-alignment)
- [Resource](https://huggingface.co/datasets/HannahRoseKirk/prism-alignment)

## 🎯 Purpose and Intended Users

**Goal**: To understand the role and impact of diverse human feedback in aligning large language models (LLMs).

**Target Audience**:
- ML Researchers
- Social Scientists
- Policy Makers

**Tasks**:
- Dialogue Generation
- Human Feedback Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Participant surveys and live conversations with LLMs

**Size**: 8,011 conversations with feedback

**Format**: JSONL

**Annotation**: Pseudonymized participant profiles with sociodemographic data and feedback ratings.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Rating
- Mean Choice

**Calculation**: Mean ratings are calculated across individual participant's ratings and conversations.

**Interpretation**: Higher mean scores indicate better perceived model responses based on participant preferences.

**Validation**: Validation was through ethical approval and participant consent.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes a diverse range of participant demographics, allowing for analyses across different ethnic, gender, and geographic groups.

**Potential Harm**: ['Reinforcing biases from dominant cultural perspectives', 'Revealing personal and sensitive topics within AI interactions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes pseudonymization of participant data and informed consent was obtained. However, some privacy risks remain due to the sensitive nature of conversations.

**Data Licensing**: Creative Commons Attribution 4.0 International License (CC-BY-4.0) for human-written texts; Creative Commons Attribution-NonCommercial 4.0 International License (CC-BY-NC-4.0) for model responses.

**Consent Procedures**: Informed consent was gathered from all participants, detailing their rights and how their data would be used.

**Compliance With Regulations**: The dataset follows GDPR compliance guidelines.
