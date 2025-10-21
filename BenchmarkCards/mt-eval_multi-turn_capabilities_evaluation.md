# MT-Eval (Multi-Turn Capabilities Evaluation)

## 📊 Benchmark Details

**Name**: MT-Eval (Multi-Turn Capabilities Evaluation)

**Overview**: MT-Eval is a comprehensive benchmark designed to evaluate multi-turn conversational abilities in large language models, measuring their coherence and adaptability in real-world dialogue scenarios.

**Data Type**: multi-turn queries

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MT-Bench

**Resources**:
- [GitHub Repository](https://github.com/KwanWaiChung/MT-Eval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to systematically evaluate and understand large language models' capabilities in multi-turn conversations across diverse applications.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-Turn Dialogue Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing datasets and augmented with GPT-4 generated queries and dialogues.

**Size**: 1,170 turns across 168 dialogue sessions.

**Format**: JSON

**Annotation**: Manually reviewed and revised for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- GPT-4 evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Scores are derived from user interactions and evaluations conducted through human raters and automated assessments using GPT-4.

**Interpretation**: Higher scores indicate better performance in multi-turn dialogue capabilities.

**Baseline Results**: GPT-4 scored highest among models evaluated.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
