# OpenGVL - Benchmarking Visual Temporal Progress for Data Curation

## 📊 Benchmark Details

**Name**: OpenGVL - Benchmarking Visual Temporal Progress for Data Curation

**Overview**: OpenGVL is a comprehensive benchmark for estimating task progress across diverse challenging manipulation tasks involving both robotic and human embodiments, aimed at improving data curation in robotics through reliable temporal task completion predictions.

**Data Type**: temporal task progress prediction

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- Agibot-World
- OXE
- Droid

**Resources**:
- [Resource](https://huggingface.co/datasets/OpenGVL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized framework for benchmarking temporal progress prediction systems in robotics and serve as a tool for data curation.

**Target Audience**:
- ML Researchers
- Robotics Practitioners
- Data Scientists

**Tasks**:
- Temporal Task Progress Prediction
- Data Curation

**Limitations**: N/A

## 💾 Data

**Source**: Various robotics datasets including nyu door, berkeley mvp, cmu stretch, and nyu franka

**Size**: 50 episodes sampled from each dataset

**Format**: N/A

**Annotation**: Automatically generated using the Value-Order Correlation (VOC) metric

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Value-Order Correlation (VOC)

**Calculation**: VOC measures the rank correlation between predicted task completion percentages and the ground truth.

**Interpretation**: A higher VOC score indicates better alignment between predictions and actual task completion.

**Baseline Results**: Comparison to proprietary models shows open-source models achieve approximately 60-70% of the performance.

**Validation**: Benchmark validation through hidden datasets to prevent contamination.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
