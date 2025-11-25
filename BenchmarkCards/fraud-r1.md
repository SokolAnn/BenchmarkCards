# Fraud-R1

## 📊 Benchmark Details

**Name**: Fraud-R1

**Overview**: Fraud-R1 is a benchmark designed to evaluate LLMs’ ability to defend against internet fraud and phishing in dynamic, real-world scenarios, featuring a multi-round evaluation pipeline.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/kaustpradalab/Fraud-R1)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of Fraud-R1 is to assess the robustness of LLMs against fraud and phishing inducements, with a focus on real-world applications.

**Target Audience**:
- ML Researchers
- AI Developers
- Security Analysts

**Tasks**:
- Fraud Detection
- Risk Assessment

**Limitations**: N/A

## 💾 Data

**Source**: 8,564 fraud cases sourced from phishing scams, fake job postings, social media, and news, categorized into 5 major fraud types.

**Size**: 8,564 examples

**Format**: N/A

**Annotation**: Manually collected and categorized fraudulent cases.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Defense Success Rate (DSR)
- DSR @k
- Average conversation rounds

**Calculation**: DSR is calculated as the proportion of samples for which the model successfully identifies fraud in any of the conversation rounds.

**Interpretation**: Higher DSR indicates better model performance in identifying and resisting fraudulent or phishing attempts.

**Baseline Results**: N/A

**Validation**: All models evaluated under both Helpful Assistant and Role-play settings for a comprehensive assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Misuse**: Improper usage

**Demographic Analysis**: The benchmark evaluates performance across different language groups and identifies disparities in performance between English and Chinese.

**Potential Harm**: ['Risk of misclassifying legitimate communications as fraud due to biases in training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
