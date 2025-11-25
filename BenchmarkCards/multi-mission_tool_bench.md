# Multi-Mission Tool Bench

## 📊 Benchmark Details

**Name**: Multi-Mission Tool Bench

**Overview**: The Multi-Mission Tool Bench evaluates agent robustness in related and dynamic multi-mission scenarios, designed to mirror real-world complexity by requiring agents to adapt to evolving demands across multiple interrelated missions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BFCL V3
- WorfBench
- TaskBench

**Resources**:
- [GitHub Repository](https://github.com/yupeijei1997/MMTB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that assesses the robustness of LLM-based agents in dynamic, multi-mission settings.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Agent decision-making evaluation

**Limitations**: The test data comprises only up to four missions due to the exponential growth of the mission switching space with more missions.

## 💾 Data

**Source**: Constructed using a controllable data generation framework simulating interactions among multiple agents.

**Size**: 1,024 test entries

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Dynamic decision tree evaluation

**Metrics**:
- Success rate
- Optimality rate

**Calculation**: Metrics calculated based on the paths taken during agent decision-making and their validity against the decision tree.

**Interpretation**: Higher success rates indicate better agent robustness and efficiency in decision-making.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
