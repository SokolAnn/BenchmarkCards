# RoTBench

## 📊 Benchmark Details

**Name**: RoTBench

**Overview**: RoTBench is a multi-level benchmark for evaluating the robustness of Large Language Models in tool learning, introducing five external environments with varying noise levels to analyze model resilience across critical phases.

**Data Type**: task scenarios with noise

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Junjie-Ye/RoTBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of Large Language Models in tool learning across different noise environments.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Tool Selection
- Parameter Identification
- Content Filling

**Limitations**: N/A

## 💾 Data

**Source**: Diverse real-world application scenarios defined through the ToolEyes evaluation system.

**Size**: 105 test cases per environment

**Format**: N/A

**Annotation**: Manually labeled paths for evaluation.

## 🔬 Methodology

**Methods**:
- Task-based evaluation metrics

**Metrics**:
- Tool Selection Score (sTS)
- Parameter Identification Score (sPI)
- Content Filling Score (sCF)

**Calculation**: Scores are computed based on the successful selection and identification of tools and parameters according to specific metrics.

**Interpretation**: Scores reflect the robustness of LLMs in adapting to noise during tool learning processes.

**Baseline Results**: N/A

**Validation**: Experimental evaluation across five noise levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
