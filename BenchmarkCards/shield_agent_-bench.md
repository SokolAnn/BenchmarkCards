# SHIELD AGENT -BENCH

## 📊 Benchmark Details

**Name**: SHIELD AGENT -BENCH

**Overview**: SHIELD AGENT -BENCH is the first comprehensive benchmark for evaluating guardrails for LLM-based autonomous agents, encompassing safe and risky trajectories across six diverse web environments.

**Data Type**: safety-related pairs of agent instructions and action trajectories

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ST-WebAgentBench
- VWA-Adv
- AgentHarm

**Resources**:
- [Resource](https://shieldagent-aiguard.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the effectiveness of guardrails for LLM-based autonomous agents.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners

**Tasks**:
- Safety Policy Compliance

**Limitations**: N/A

## 💾 Data

**Source**: Safety-related instructions and trajectories generated via attacks on LLM-based agents.

**Size**: 3,110 pairs

**Format**: N/A

**Annotation**: Manually annotated for safety compliance

## 🔬 Methodology

**Methods**:
- Automated metrics
- Experiments with existing benchmarks

**Metrics**:
- Accuracy
- False Positive Rate
- Rule Recall Rate

**Calculation**: Measured the effectiveness of guardrails using both accuracy and efficiency metrics.

**Interpretation**: Higher accuracy and lower false positive rates indicate more effective guardrail mechanisms.

**Baseline Results**: Compared against existing benchmarks such as ST-WebAgentBench, VWA-Adv, and AgentHarm.

**Validation**: Extensive experiments demonstrating performance across various risk scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack, Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to mitigate safety risks in LLM-based agents.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
