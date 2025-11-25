# AgentSeer

## 📊 Benchmark Details

**Name**: AgentSeer

**Overview**: AgentSeer is an observability-based evaluation framework that decomposes agentic executions into granular action and component graphs, enabling systematic agentic-situational assessment for large language models.

**Data Type**: action and component graphs

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HarmBench
- AgentBench

**Resources**:
- [Resource](https://mlflow.org/docs/latest/genai/tracing/)
- [Resource](https://langchain-ai.github.io/langgraph/)

## 🎯 Purpose and Intended Users

**Goal**: To establish a systematic method for evaluating safety in agentic AI systems and expose agentic vulnerabilities.

**Target Audience**:
- AI Researchers
- Model Developers
- Safety Engineers

**Tasks**:
- Security Assessment
- Vulnerability Evaluation

**Limitations**: The evaluation focuses on one agentic use case and a specific technology stack, which may limit generalizability.

## 💾 Data

**Source**: HarmBench evaluations on agentic-level vulnerabilities.

**Size**: 50 harmful objectives evaluated

**Format**: N/A

**Annotation**: Evaluation conducted through comparative model validation.

## 🔬 Methodology

**Methods**:
- Model-level iterative attacks
- Agentic-level direct attacks
- Context-aware iterative attacks

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: Calculated as the ratio of successful attacks to total objectives.

**Interpretation**: Higher ASR indicates greater vulnerability and lower effectiveness of safety guardrails.

**Baseline Results**: GPT-OSS-20B: 39.47% ASR; Gemini-2.0-flash: 50.00% ASR.

**Validation**: Cross-model validation on GPT-OSS-20B and Gemini-2.0-flash.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack, Data poisoning
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Identifying agent-specific vulnerabilities that traditional evaluations miss.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
