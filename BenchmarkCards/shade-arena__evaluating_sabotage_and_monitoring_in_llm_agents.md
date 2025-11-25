# SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents

## 📊 Benchmark Details

**Name**: SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents

**Overview**: SHADE-Arena is a diverse agent evaluation dataset for assessing the sabotage and monitoring capabilities of LLM agents through complex pairs of benign main tasks and harmful side objectives in complicated environments.

**Data Type**: task pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/safety-research/SHADE-Arena)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the sabotage capabilities of large language models (LLMs) and their monitoring abilities in high-stakes environments.

**Target Audience**:
- ML Researchers
- Safety Researchers

**Tasks**:
- Task Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic environments generated to mimic real-world agent interactions.

**Size**: 17 task pairs

**Format**: N/A

**Annotation**: Manual engineering and transcript review to ensure task complexity and validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- AUC

**Calculation**: Success is defined as the agent completing the main task and side task without detection by the monitor.

**Interpretation**: A higher score indicates better ability of agents to execute tasks without being detected.

**Baseline Results**: Claude 3.7 Sonnet and Gemini 2.5 Pro scored 27% and 15% as sabotage agents respectively.

**Validation**: Successful trajectories are compared across multiple models to assess performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
