# Robustness Benchmark for Reference-Free Dialogue Evaluation

## 📊 Benchmark Details

**Name**: Robustness Benchmark for Reference-Free Dialogue Evaluation

**Overview**: This benchmark evaluates the robustness of reference-free dialogue metrics against four categories of adversarial attacks: speaker tag prefixes, static responses, ungrammatical responses, and repeated conversational context.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DialogRPT
- UniEval

**Resources**:
- [GitHub Repository](https://github.com/JVasselli/dialogue-metric-robustness)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the robustness of dialogue evaluation metrics and provide a nuanced evaluation framework for assessing dialogue systems.

**Target Audience**:
- ML Researchers
- Dialogue System Developers
- NLP Practitioners

**Tasks**:
- Dialogue Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: DailyDialog and Topical-Chat datasets

**Size**: 160 dialogues (100 from DailyDialog, 60 from Topical-Chat)

**Format**: JSON

**Annotation**: Annotated with human ratings for content, grammaticality, relevance, and overall quality.

## 🔬 Methodology

**Methods**:
- Correlation with human judgment
- Adversarial testing

**Metrics**:
- Kendall's tau

**Calculation**: The success rate quantifies how often metrics rank adversarial responses lower than reference responses.

**Interpretation**: A higher success rate indicates greater robustness against adversarial attacks.

**Baseline Results**: N/A

**Validation**: Metrics performance is validated against human annotations across multiple dialogue aspects.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Extraction attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
