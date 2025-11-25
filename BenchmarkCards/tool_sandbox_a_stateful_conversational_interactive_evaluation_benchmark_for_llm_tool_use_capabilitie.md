# TOOL SANDBOX (A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities)

## 📊 Benchmark Details

**Name**: TOOL SANDBOX (A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities)

**Overview**: TOOL SANDBOX is a stateful, conversational and interactive evaluation benchmark for LLM tool-use capabilities, showcasing significant performance gaps between models across complex task scenarios such as State Dependency, Canonicalization, and Insufficient Information.

**Data Type**: test scenarios with stateful tool interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BFCL
- ToolEval
- API-Bank
- ToolTalk
- τ-bench

**Resources**:
- [GitHub Repository](https://github.com/apple/ToolSandbox)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for LLMs' tool-use capabilities in a conversational interactive setting, illuminating challenges faced by state-of-the-art models.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Tool Use
- State Dependency Handling
- Conversational Interaction

**Limitations**: Requires deep knowledge of tool capacities for milestone and minefield authoring and is subject to non-negligible hallucination from the user simulator.

## 💾 Data

**Source**: Generated synthetic data from simulated interactions within the benchmark framework.

**Size**: 1,032 test scenarios

**Format**: Python scripts

**Annotation**: Manually authored and calibrated by internal domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- On-policy conversational evaluation

**Metrics**:
- Average similarity score
- Turn efficiency

**Calculation**: Metrics are calculated based on milestones and minefields defined for each test scenario and evaluated through a trajectory's conformity to these defined steps.

**Interpretation**: Higher similarity scores indicate better alignment with the defined milestones and overall completion of tasks; lower turn counts suggest improved efficiency.

**Validation**: Multiple rounds of tests against several LLM models were conducted to ensure validity and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
