# CoCo-CoLa (Correct Concept - Correct Language)

## 📊 Benchmark Details

**Name**: CoCo-CoLa (Correct Concept - Correct Language)

**Overview**: CoCo-CoLa is a novel metric designed to evaluate language adherence in multilingual LLMs, specifically measuring the ability of models to generate responses in the intended input language.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- French
- German
- Hindi
- Italian
- Portuguese
- Spanish

**Resources**:
- [GitHub Repository](https://github.com/elnazrahmati/CoCo-CoLa)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve language adherence in multilingual Large Language Models (LLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Closed-Book Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Mintaka CBQA dataset, a multilingual dataset providing identical question-answer pairs in multiple languages.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Fine-tuning experiments
- Metric evaluation

**Metrics**:
- CoCo-CoLa ratio
- Cumulative accuracy

**Calculation**: The CoCo-CoLa ratio is calculated based on the model's adherence to generating responses in the input language compared to generating in English.

**Interpretation**: Higher ratios indicate better adherence to the input language. Results are interpreted based on comparative performance across languages.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The research addresses linguistic biases which may affect underrepresented languages.

**Potential Harm**: The metric aims to reduce biases favoring high-resource languages, contributing to a more equitable language model adaptation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
