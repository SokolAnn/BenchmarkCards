# AgentBackdoorEval

## 📊 Benchmark Details

**Name**: AgentBackdoorEval

**Overview**: AgentBackdoorEval is a dataset designed for the comprehensive evaluation of agent backdoor attacks, covering five real-world scenarios where agents may be deployed, including Banking Finance, E-commerce, Medical, Social Media, and Weather Query.

**Data Type**: task simulation scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentInstruct
- ToolBench

**Resources**:
- [GitHub Repository](https://github.com/whfeLingYu/DemonAgent)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the resilience of LLM-based agents against sophisticated backdoor attacks.

**Target Audience**:
- ML Researchers
- Security Practitioners

**Tasks**:
- Task Simulation

**Limitations**: N/A

## 💾 Data

**Source**: Generated using automated prompts to simulate attack scenarios and tool functions.

**Size**: N/A

**Format**: Structured format

**Annotation**: Automatically generated from prompts.

## 🔬 Methodology

**Methods**:
- Evaluation against multiple datasets

**Metrics**:
- Attack Success Rate (ASR)
- Detection Rate (DR)
- Normal Task Completion Performance (NP)

**Calculation**: Metrics are calculated as ratios of successful attacks and detected anomalies.

**Interpretation**: Lower DR and higher ASR indicate better attack effectiveness and stealthiness.

**Baseline Results**: N/A

**Validation**: Performance evaluated across multiple agent benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
