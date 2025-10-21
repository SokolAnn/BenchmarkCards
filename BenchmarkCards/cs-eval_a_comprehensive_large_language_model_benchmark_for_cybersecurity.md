# CS-Eval (A Comprehensive Large Language Model Benchmark for CyberSecurity)

## 📊 Benchmark Details

**Name**: CS-Eval (A Comprehensive Large Language Model Benchmark for CyberSecurity)

**Overview**: CS-Eval is a publicly accessible, comprehensive and bilingual benchmark specifically designed for evaluating the performance of large language models (LLMs) in cybersecurity across 42 categories organized into knowledge, ability, and application levels.

**Data Type**: question-answering pairs

**Domains**:
- Cybersecurity

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/CS-EV AL/CS-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for assessing the cybersecurity capabilities of large language models (LLMs).

**Target Audience**:
- ML Researchers
- Cybersecurity Professionals
- Model Developers

**Tasks**:
- Vulnerability Management
- Threat Detection
- Data Security

**Limitations**: The reliance on manual data collection and the need to develop automated methods for future enhancement.

## 💾 Data

**Source**: Curated questions generated from expert knowledge, validated and dynamically updated for accuracy.

**Size**: 4,369 questions

**Format**: JSON

**Annotation**: Manually crafted and validated by a team of experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Evaluate the primary metric based on exact answer matches for multiple-choice questions and binary correctness for open-ended questions.

**Interpretation**: Scores are averaged to evaluate model performance across different fields.

**Baseline Results**: Average scores across models vary widely based on capabilities in specific cybersecurity tasks.

**Validation**: Cross-validation of questions to ensure consistency and correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
