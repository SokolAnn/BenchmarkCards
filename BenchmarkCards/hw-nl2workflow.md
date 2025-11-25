# HW-NL2Workflow

## 📊 Benchmark Details

**Name**: HW-NL2Workflow

**Overview**: The HW-NL2Workflow dataset includes 3,695 real-world business samples for training and evaluation, designed to enhance the automation of workflow construction from natural language instructions.

**Data Type**: workflow samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2503.22473)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for the NL2Workflow task to boost research and development in workflow automation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Workflow Generation

**Limitations**: N/A

## 💾 Data

**Source**: 3,695 workflows collected from an enterprise platform, each annotated by domain experts.

**Size**: 3,695 examples

**Format**: JSON

**Annotation**: Annotated by domain experts with natural language instructions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Exact Match Rate
- Arrangement Accuracy
- Parameter Accuracy

**Calculation**: Metrics are calculated based on the alignment of generated workflows with ground truth workflows.

**Interpretation**: Higher rates in Exact Match Rate, Arrangement Accuracy, and Parameter Accuracy indicate better model performance in workflow generation.

**Baseline Results**: Comparison against baseline models like GPT-4o, Qwen2.5-72B-Instruct, demonstrating superior performance with an EMR of 52.7%.

**Validation**: Extensive experiments conducted to evaluate the effectiveness of the WorkTeam framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
