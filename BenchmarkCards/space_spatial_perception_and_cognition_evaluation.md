# SPACE (Spatial Perception And Cognition Evaluation)

## 📊 Benchmark Details

**Name**: SPACE (Spatial Perception And Cognition Evaluation)

**Overview**: SPACE is a benchmark that systematically evaluates spatial cognition in frontier models, based on tasks of cognitive science. It comprises large-scale and small-scale spatial cognition tasks to assess mapping abilities, reasoning about object shapes, and cognitive infrastructure like spatial attention and memory.

**Data Type**: text, image

**Domains**:
- Natural Language Processing
- Cognitive Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/apple/ml-space-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the spatial cognition capabilities of frontier models using a comprehensive suite of tasks designed from cognitive science research.

**Target Audience**:
- ML Researchers
- Cognitive Scientists
- Model Developers

**Tasks**:
- Spatial Reasoning
- Spatial Navigation
- Object Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Tasks derived from cognitive science literature, including video walk-throughs and static images.

**Size**: Approximately 1,600 total tasks across various formats.

**Format**: Visual and Text

**Annotation**: Tasks developed based on established psychological tests.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Each task's performance is measured based on the percentage of correctly answered questions for both human and model responses.

**Interpretation**: Performance is interpreted based on comparison to human accuracy, with benchmarks defined for each task.

**Baseline Results**: Human performance averages around 80%+ across tasks, with specific model performances detailed in the paper.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['Lack of spatial cognition could hinder advancements in AI alignment with human cognitive processes.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
