# OS-H ARM

## 📊 Benchmark Details

**Name**: OS-H ARM

**Overview**: OS-H ARM is a benchmark for measuring the safety of computer use agents, focusing on assessing the risks posed by deliberate user misuse, prompt injection attacks, and model misbehavior across various operating system applications.

**Data Type**: task-based interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/tml-epfl/os-harm)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively measure the safety risks associated with computer use agents and ensure their alignment with acceptable usage policies.

**Target Audience**:
- ML Researchers
- Safety Researchers
- Model Developers

**Tasks**:
- Deliberate User Misuse
- Prompt Injection
- Model Misbehavior

**Limitations**: N/A

## 💾 Data

**Source**: OSWorld environment

**Size**: 150 tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation

**Metrics**:
- F1 Score
- Task Completion Rate

**Calculation**: F1 score computed on the evaluation outputs comparing automated scoring and human annotations.

**Interpretation**: A higher F1 score indicates better agreement between model evaluations and safety expectations.

**Baseline Results**: The average unsafe execution rates across models are reported, with varying performance on task completion.

**Validation**: Evaluated against a variety of frontier agent models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Security

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
