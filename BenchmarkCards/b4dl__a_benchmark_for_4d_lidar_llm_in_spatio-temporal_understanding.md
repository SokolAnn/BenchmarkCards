# B4DL: A Benchmark for 4D LiDAR LLM in Spatio-Temporal Understanding

## 📊 Benchmark Details

**Name**: B4DL: A Benchmark for 4D LiDAR LLM in Spatio-Temporal Understanding

**Overview**: We introduce B4DL, a benchmark designed for MLLMs to understand spatio-temporal dynamics in 4D LiDAR data, with a suite of tasks that evaluate both simple and complex understanding of outdoor scenes.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- nuScenes
- LiDAR-LLM

**Resources**:
- [Resource](https://mmb4dl.github.io/mmb4dl/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the understanding of spatio-temporal dynamics inherent in 4D LiDAR data by MLLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Existence
- Binary QA
- Time Grounding
- Description
- Temporal Understanding
- Comprehensive Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated dataset based on 4D LiDAR point clouds sourced from the nuScenes dataset.

**Size**: 178,416 question-answer pairs

**Format**: JSON

**Annotation**: Generated through a novel data generation pipeline incorporating both automated methods and human annotations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- mIoU
- BLEU-4
- ROUGE-L
- METEOR
- BERTScore

**Calculation**: Metrics are calculated based on specific evaluation criteria defined for each task.

**Interpretation**: Higher scores indicate better understanding and reasoning capability of MLLMs over 4D LiDAR data.

**Baseline Results**: N/A

**Validation**: Evaluations are performed on a separate test set of 150 scenes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
