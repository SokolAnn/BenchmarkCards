# InPlan3D

## 📊 Benchmark Details

**Name**: InPlan3D

**Overview**: InPlan3D is a comprehensive benchmark for 3D task planning, consisting of 3,174 long-term planning tasks across 636 indoor scenes.

**Data Type**: task planning tasks

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- SQA3D
- ScanRefer
- Multi3DRefer

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capability of Multimodal Large Language Models (MLLMs) in the context of 3D task planning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: Curated 3D indoor scenes and constructed planning tasks from the perspective of an indoor service robot.

**Size**: 3,174 tasks across 636 scenes

**Format**: N/A

**Annotation**: Tasks are described with high-level instructions followed by detailed step-by-step actions.

## 🔬 Methodology

**Methods**:
- Benchmark evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Step-level accuracy
- Task-level accuracy

**Calculation**: Metrics are calculated based on the correctness of the generated plans against ground truth.

**Interpretation**: Higher metrics indicate better reasoning and planning capabilities in 3D environments.

**Baseline Results**: State-of-the-art performance achieved with Text-Scene.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
