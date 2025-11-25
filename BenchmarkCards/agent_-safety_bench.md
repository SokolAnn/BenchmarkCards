# AGENT -SAFETY BENCH

## 📊 Benchmark Details

**Name**: AGENT -SAFETY BENCH

**Overview**: AGENT -SAFETY BENCH is a comprehensive benchmark designed to evaluate the safety of LLM agents, encompassing 349 interaction environments and 2,000 test cases, evaluating 8 categories of safety risks and covering 10 common failure modes frequently encountered in unsafe interactions.

**Data Type**: test cases

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- R-Judge
- AgentDojo
- GuardAgent
- ToolEmu
- ToolSword
- InjecAgent

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/Agent-SafetyBench/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate further research in agent safety evaluation and improvement.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Safety Evaluation

**Limitations**: Most test cases rely on commonsense reasoning; advanced domain-specific knowledge testing is left for future work.

## 💾 Data

**Source**: Generated from interaction scenarios and existing benchmarks.

**Size**: 2,000 test cases

**Format**: JSON

**Annotation**: Manually annotated with potential risks and failure modes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Safety Score

**Calculation**: Total safety scores are computed based on the ratio of safe to unsafe cases from the 2,000 test cases.

**Interpretation**: Higher scores indicate better safety performance, with scores below 60% highlighting significant safety challenges.

**Validation**: Cross-validation and manual reviews conducted on test cases and safety annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack, Extraction attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential for malicious use of benchmark test cases by adversarial attackers.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark does not contain any actual personal or sensitive information.

**Data Licensing**: Distributed under the MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
