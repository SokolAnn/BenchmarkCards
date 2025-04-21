# R-Judge

## 📊 Benchmark Details

**Name**: R-Judge

**Overview**: A benchmark crafted to evaluate the proficiency of LLMs in judging and identifying safety risks given agent interaction records.

**Data Type**: text

**Domains**:
- programming
- internet of things (IoT)
- software
- web
- finance

**Resources**:
- [GitHub Repository](https://github.com/Lordog/R-Judge)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the risk awareness of large language models (LLMs) in interactive environments, specifically in judging safety risks during agent interactions.

**Target Audience**:
- Researchers
- Practitioners
- LLM Engineers

**Tasks**:
- Judging safety risks
- Identifying unsafe actions from agent interactions
- Enhancing LLM safety awareness

**Limitations**: None

## 💾 Data

**Source**: Curated from diverse agent interaction scenarios and annotated by human experts.

**Size**: 569 records

**Format**: text

**Annotation**: High-quality curation with annotated safety labels and risk descriptions.

## 🔬 Methodology

**Methods**:
- Human annotation
- Evaluation on 11 LLMs
- Fine-tuning experiments

**Metrics**:
- F1 score
- Recall
- Specificity
- Effectiveness

**Calculation**: F1 = 2 * (Recall * Precision) / (Recall + Precision)

**Interpretation**: The model's ability to accurately identify whether agent actions are safe or unsafe.

**Baseline Results**: Random scores indicate a baseline performance, where models generally score lower than random in safety judgment tests.

**Validation**: GPT-4 as an automatic scorer to validate model-generated analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety Judgment
- Risk Identification

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Societal Impact**: Impact on Jobs
- **Misuse**: Non-disclosure
- **Governance**: Lack of system transparency

**Demographic Analysis**: N/A

**Potential Harm**: Ensure data safety and minimize risks associated with agent actions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset includes records of potentially sensitive information; handling must comply with privacy regulations.

**Data Licensing**: Data is curated from various sources and must comply with respective licensing agreements.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Need to ensure models comply with data protection laws and ethical guidelines.
