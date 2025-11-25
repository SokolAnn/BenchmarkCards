# U-SAFEBENCH (User-Specific Safety Benchmark)

## 📊 Benchmark Details

**Name**: U-SAFEBENCH (User-Specific Safety Benchmark)

**Overview**: U-SAFEBENCH is the first benchmark designed to assess user-specific aspect of LLM safety by evaluating the responses of LLM agents when considering user-specific profiles.

**Data Type**: user instructions and profiles

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SafetyBench

**Resources**:
- [GitHub Repository](https://github.com/yeonjun-in/U-SafeBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the user-specific safety of LLM agents and assess their responses based on user profiles.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Safety Evaluators

**Tasks**:
- Question Answering
- Autonomous Agent Tasks

**Limitations**: The overall safety performance of most models remains inadequate for real-world deployment.

## 💾 Data

**Source**: The dataset includes over 150 user profiles and more than 1,900 real-world user instructions adapted for user-specific safety.

**Size**: 1,936 instruction-user profile pairs

**Format**: CSV

**Annotation**: Collection includes automated data generation and human annotation for user-specific safety classification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- User-Specific Safety Score
- User-Specific Helpfulness Score

**Calculation**: Safety score is calculated based on the rejection ratio of harmful instructions, while helpfulness score is the fulfillment ratio of benign instructions.

**Interpretation**: Higher safety scores indicate better compliance with user-specific safety standards; higher helpfulness scores indicate better assistance to benign requests.

**Baseline Results**: Average LLMs achieved a user-specific safety score of 18.6%; Claude-3.5-sonnet achieved a state-of-the-art score of 63.8%.

**Validation**: Models' responses evaluated using LLM-as-a-judge approach to determine refusal intent.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset may include sensitive content depending on user profiles; clear content warnings will be provided.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
