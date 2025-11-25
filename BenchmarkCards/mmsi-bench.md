# MMSI-Bench

## 📊 Benchmark Details

**Name**: MMSI-Bench

**Overview**: MMSI-Bench is a Visual Question Answering benchmark dedicated to multi-image spatial intelligence, designed to rigorously evaluate the spatial reasoning capabilities of multimodal large language models (MLLMs) through challenging, human-annotated questions based on diverse real-world images.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VSI-Bench
- MuriBench
- UniQA-3D

**Resources**:
- [Resource](https://runsenxu.com/projects/MMSI_Bench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the multi-image spatial reasoning capabilities of multimodal large language models and provide insights for advancing spatial intelligence.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated from multiple real-world datasets including ScanNet, Matterport3D, nuScenes, Ego4D, and others.

**Size**: 1,000 questions

**Format**: JSON

**Annotation**: Human-annotated by experts after extensive review for quality and clarity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the percentage of correct answers derived from exact matches between model outputs and ground-truth answers.

**Interpretation**: Higher accuracy indicates better spatial reasoning ability across multiple images.

**Baseline Results**: Human accuracy is approximately 97%, while top models score between 30-42%.

**Validation**: Extensive evaluation across 37 models was conducted to establish performance benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License (CC BY 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
