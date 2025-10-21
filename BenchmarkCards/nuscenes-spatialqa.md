# NuScenes-SpatialQA

## 📊 Benchmark Details

**Name**: NuScenes-SpatialQA

**Overview**: NuScenes-SpatialQA is the first large-scale ground-truth-based Question-Answer (QA) benchmark specifically designed to evaluate the spatial understanding and reasoning capabilities of Vision-Language Models (VLMs) in autonomous driving. It systematically evaluates VLMs’ performance in both spatial understanding and reasoning across multiple dimensions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- NuScenes-MQA
- NuScenes-QA
- DriveLM

**Resources**:
- [Resource](https://taco-group.github.io/NuScenes-SpatialQA/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the spatial understanding and reasoning capabilities of Vision-Language Models (VLMs) in autonomous driving.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Spatial Question Answering

**Limitations**: While NuScenes-SpatialQA provides a systematic evaluation of spatial reasoning in VLMs, it has certain limitations. It is constructed from the NuScenes dataset, which is limited to urban driving scenarios and does not cover all possible driving conditions.

## 💾 Data

**Source**: Constructed from the NuScenes dataset, which offers extensive real-world driving scenarios with multi-modal sensor data.

**Size**: 150 scenes, each with 40 key frames, totaling approximately 3.5 million QA pairs

**Format**: N/A

**Annotation**: Automatically generated through 3D scene graph generation and QA generation pipelines.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- Tolerance-based Accuracy
- Mean Absolute Error (MAE)

**Calculation**: Quantitative QA tasks utilize tolerance-based accuracy and mean absolute error to assess performance.

**Interpretation**: The capacity to achieve high accuracy in qualitative tasks versus challenges faced in quantitative assessments indicates varying levels of spatial reasoning capacity among VLMs.

**Baseline Results**: Performance comparisons of various VLMs benchmarked, such as LLaVA and Qwen, across qualitative and quantitative spatial QA tasks.

**Validation**: Conducted through extensive experimental evaluations on diverse VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark is built on publicly available data while ensuring privacy and unbiased evaluation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
