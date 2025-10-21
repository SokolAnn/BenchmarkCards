# OmniEAR

## 📊 Benchmark Details

**Name**: OmniEAR

**Overview**: OmniEAR is a comprehensive framework for evaluating how language models reason about physical interactions, tool usage, and multi-agent coordination in embodied tasks, utilizing 1,500 scenarios across household and industrial domains.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- ALFRED
- BEHAVIOR-1K
- PARTNR
- TDW-MAT

**Resources**:
- [GitHub Repository](https://github.com/ZJU-REAL/OmniEmbodied)
- [Resource](https://zju-real.github.io/OmniEmbodied)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate embodied reasoning in embodied AI systems through scenarios requiring the understanding of physical properties and dynamic capability acquisition.

**Target Audience**:
- ML Researchers
- Robotics Engineers
- AI Developers

**Tasks**:
- Dynamic Capability Acquisition
- Tool Usage Reasoning
- Multi-Agent Coordination

**Limitations**: N/A

## 💾 Data

**Source**: Generated through automated pipelines producing various scenarios reflecting rich physical environments.

**Size**: 1,500 scenarios

**Format**: JSON

**Annotation**: Automatically validated through a pipeline combining neural generation and rule-based checks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Success Rate (SR)
- Execution Steps

**Calculation**: Success rate calculated based on task completion percentage across various tasks.

**Interpretation**: Higher success rates indicate better alignment with task requirements and improved embodied reasoning abilities.

**Baseline Results**: Current models show performance degradation from 85% success with explicit instructions to below 65% in constraint-based reasoning tasks.

**Validation**: Each scenario underwent multi-tier validation involving automated and human evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Data poisoning
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Exposing personal information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
