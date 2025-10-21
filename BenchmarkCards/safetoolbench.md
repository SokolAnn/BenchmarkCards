# SafeToolBench

## 📊 Benchmark Details

**Name**: SafeToolBench

**Overview**: SafeToolBench is the first benchmark to comprehensively assess tool utilization security in a prospective manner, encompassing malicious user instructions and diverse practical toolsets across 16 real-world domains.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Finance
- Social Media

**Languages**:
- English

**Similar Benchmarks**:
- ToolEmu
- AgentSafetyBench

**Resources**:
- [GitHub Repository](https://github.com/BITHLP/SafeToolBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the safety of tool utilization in LLMs before executing potentially harmful actions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Risk Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Generated using GPT-4o based on real-world scenarios.

**Size**: 1,200 examples

**Format**: JSON

**Annotation**: Manually reviewed and rated by experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Scores are computed based on user instructions, tool characteristics, and their interactions, with predefined thresholds.

**Interpretation**: Higher scores indicate higher risks associated with tool utilization.

**Baseline Results**: N/A

**Validation**: Data validated through expert review and scoring protocols.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data generated ensures no real personal or sensitive information is used.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
