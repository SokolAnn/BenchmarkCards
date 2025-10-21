# IFEval-FC

## 📊 Benchmark Details

**Name**: IFEval-FC

**Overview**: IFEval-FC assesses precise instruction following in function calling, focusing on evaluating LLMs’ ability to follow verifiable format instructions embedded within JSON schema parameter descriptions.

**Data Type**: function call examples with embedded format requirements

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BFCL
- ACEBench

**Resources**:
- [GitHub Repository](https://github.com/Skripkon/IFEval-FC)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' ability to follow formatting instructions in function calling scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Function Calling Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Real-world function schemas enhanced with verifiable instruction constraints, generated using GPT-5.

**Size**: 750 test cases

**Format**: JSON

**Annotation**: Function schemas enhanced with instructions and user queries generated via AI.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Score is defined as 1 if the instruction is followed, 0 otherwise.

**Interpretation**: Higher scores indicate better adherence to format constraints.

**Baseline Results**: Models evaluated include GPT-5 and Claude Opus 4.1 with no model achieving above 80% accuracy.

**Validation**: Validation procedures ensured tasks were appropriately challenging and suitable for LLM evaluations.

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
