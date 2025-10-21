# TB-Bench

## 📊 Benchmark Details

**Name**: TB-Bench

**Overview**: TB-Bench is a comprehensive benchmark designed to evaluate Multi-Modal Large Language Models (MLLMs) on understanding traffic behaviors across eight perception tasks from ego-centric views.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- KITTI
- ONCE
- Argoverse2

**Resources**:
- [GitHub Repository](https://github.com/TB-AD/TB-Bench-110k-250k)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TB-Bench is to rigorously assess MLLM performance across eight distinct perception tasks in the context of autonomous driving.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Spatial Reasoning
- Relative Distance
- Orientation Reasoning
- Other Lane to Ego-Vehicle
- Other Lane Changing
- Other Turning
- Ego Turning
- Ego Traverse Distance

**Limitations**: The study utilizes moderate large language models due to limited computational resources, which could be scaled up.

## 💾 Data

**Source**: The data is generated from existing datasets such as KITTI, ONCE, and Argoverse2, containing ego-centric views of traffic scenarios.

**Size**: 2,000 samples for benchmark; TB-100k has 110,000 samples; TB-250k has 250,000 samples.

**Format**: JSON

**Annotation**: Question-and-answer pairs are manually constructed and augmented using existing dataset samples.

## 🔬 Methodology

**Methods**:
- Rule-based evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the response accuracy of the models, using regular expressions for keyword matching.

**Interpretation**: An accuracy score of 1 indicates a correct prediction; otherwise, the score is 0.

**Baseline Results**: The proposed models achieve average accuracy up to 85% when fine-tuned with TB-100k.

**Validation**: Validation procedures include cross-validated performance metrics based on accuracy comparisons with existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
