# CityEQA-EC

## 📊 Benchmark Details

**Name**: CityEQA-EC

**Overview**: CityEQA-EC is the first benchmark dataset for Embodied Question Answering in urban environments, featuring 1,412 human-annotated tasks across six categories, grounded in a realistic 3D urban simulator.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- OpenEQA
- City-3DQA
- EarthVQA

**Resources**:
- [Resource](https://anonymous.4open.science/r/CityEQA-3027)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate embodied agents' performance on CityEQA tasks and promote advancements in urban spatial intelligence.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Embodied Question Answering
- Spatial Reasoning

**Limitations**: The benchmark primarily focuses on object-centric question-answering tasks and does not cover dynamic events or social interactions.

## 💾 Data

**Source**: Collected from the EmbodiedCity 3D urban simulator.

**Size**: 1,412 tasks

**Format**: N/A

**Annotation**: Annotated by five human annotators through observation of 3D simulated environments.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Question Answering Accuracy (QAA)
- Navigation Error (NE)
- Mean Time Steps (MTS)

**Calculation**: Metrics are calculated based on the correctness of answers, the distance to the target object, and the average time steps taken to complete tasks.

**Interpretation**: Higher QAA indicates better performance, lower NE denotes successful navigation, and reduced MTS reflects efficiency.

**Baseline Results**: PMA achieved 60.73% of human accuracy in answering questions.

**Validation**: Performance is assessed against five types of baselines, including human performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No identifiable information or private properties were included in the data collection process.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
