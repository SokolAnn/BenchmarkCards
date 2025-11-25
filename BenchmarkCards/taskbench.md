# TASKBENCH

## 📊 Benchmark Details

**Name**: TASKBENCH

**Overview**: TASKBENCH is a comprehensive framework to evaluate the capability of LLMs in task automation, specifically focusing on task decomposition, tool selection, and parameter prediction.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MetaTool
- ToolBench
- APIBench

**Resources**:
- [GitHub Repository](https://github.com/microsoft/JARVIS)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and standardized benchmark for evaluating LLMs in the field of task automation.

**Target Audience**:
- Research Community
- AI Practitioners

**Tasks**:
- Task Decomposition
- Tool Selection
- Parameter Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Generated through a comprehensive data generation process leveraging LLMs and a Tool Graph.

**Size**: 17,331 samples

**Format**: JSON

**Annotation**: Combination of automated generation and human verification methodologies.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Node F1
- Edge F1
- ROUGE-L

**Calculation**: Calculated based on the accuracy of tool predictions and their dependencies.

**Interpretation**: Higher F1 scores and ROUGE-L indicate better performance in task automation.

**Baseline Results**: Compared against traditional benchmarks such as APIBench, ToolBench, and MetaTool.

**Validation**: Results confirmed by correlation with human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
