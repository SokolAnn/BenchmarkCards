# SpatialScore (Spatial Understanding Benchmark)

## 📊 Benchmark Details

**Name**: SpatialScore (Spatial Understanding Benchmark)

**Overview**: SpatialScore is the most comprehensive multimodal spatial understanding benchmark, integrating VGBench with data from 11 existing datasets to assess MLLMs' abilities in 3D spatial reasoning through 28K samples across various tasks and modalities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VGBench
- MMVP
- RealWorldQA
- VSR
- SpatialSense
- SpatialBench

**Resources**:
- [Resource](https://haoningwu3639.github.io/SpatialScore)

## 🎯 Purpose and Intended Users

**Goal**: To investigate and evaluate the spatial understanding capabilities of existing multimodal large language models (MLLMs) and to provide a rigorous testing framework for future research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- 3D Spatial Reasoning
- Distance Estimation
- Object Localization
- Positional Relations

**Limitations**: N/A

## 💾 Data

**Source**: Integrated data from 12 spatial understanding datasets including VGBench and various existing benchmarks.

**Size**: 28,000 samples

**Format**: question-answering pairs

**Annotation**: Data is extracted and curated from multiple existing datasets, ensuring diversity in spatial understanding tasks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on correct answers provided by models against the ground truth.

**Interpretation**: Higher accuracy indicates better spatial understanding abilities in MLLMs.

**Baseline Results**: Performance of current MLLMs on SpatialScore evaluated across various model parameters.

**Validation**: All results are validated through extensive evaluations and comparisons with existing MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Transparency
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
