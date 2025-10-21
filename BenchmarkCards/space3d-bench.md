# Space3D-Bench

## 📊 Benchmark Details

**Name**: Space3D-Bench

**Overview**: Space3D-Bench is a dataset composed of 1000 spatial questions and answers related to scenes of the Replica dataset, aimed at evaluating 3D question answering systems with a variety of data modalities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- 3DMV-VQA
- M3DBench
- ScanQA

**Resources**:
- [Resource](https://space3d-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate spatial question answering systems using diverse, human-formulated questions based on 3D environments.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Replica dataset, consisting of various indoor scenes.

**Size**: 1000 questions

**Format**: N/A

**Annotation**: Manually constructed by researchers to limit ambiguities and ensure suitability.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Calculated based on the comparison of system answers with a ground-truth assessment.

**Interpretation**: An accuracy of 67% indicates a moderate level of performance by the answering system.

**Baseline Results**: The baseline system, RAG3D-Chat, achieved 67% accuracy.

**Validation**: Extensive user study confirmed the reliability of the assessment protocol with 97.5% agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
