# Rinas

## 📊 Benchmark Details

**Name**: Rinas

**Overview**: Rinas is a data loading framework designed to efficiently load large shuffled datasets for model training, enhancing overall training throughput without compromising accuracy.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To increase the training efficiency of models on large shuffled datasets through a novel data loading framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Model Training

**Limitations**: N/A

## 💾 Data

**Source**: Various large datasets including ImageNet, C4, RedPajama, and more.

**Size**: From 140 GB to 10 TB depending on dataset.

**Format**: Varied, including structured and unstructured data formats.

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Baseline comparisons against existing data loading frameworks
- Performance benchmarking during model training

**Metrics**:
- Throughput

**Calculation**: Throughput calculated by dividing the total number of samples processed by the total time taken.

**Interpretation**: Higher throughput indicates better performance and efficiency of the data loading process.

**Baseline Results**: Training throughput improved by up to 89% for vision models and 59% for language models compared to existing frameworks.

**Validation**: Evaluations conducted on multiple standard datasets across different model training scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
