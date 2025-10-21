# 3DBench: A Scalable 3D Benchmark and Instruction-Tuning Dataset

## 📊 Benchmark Details

**Name**: 3DBench: A Scalable 3D Benchmark and Instruction-Tuning Dataset

**Overview**: 3DBench is a scalable benchmark designed for evaluating 3D-LLMs covering ten diverse multi-modal tasks with three types of evaluation metrics.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To establish a scalable evaluation benchmark specifically designed for assessing 3D-LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Visual Grounding
- Detection
- Counting
- Room Detection
- Pose Relationship
- Object Relationship
- Navigation
- Question Answering
- Caption Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated using the Procthor simulation framework and includes data collected from 30,000 houses.

**Size**: over 0.23 million QA pairs

**Format**: N/A

**Annotation**: Ground-truth is incorporated into diverse dialogue templates.

## 🔬 Methodology

**Methods**:
- Quantitative evaluation
- Heuristic scoring with GPT
- Traditional evaluation metrics

**Metrics**:
- Accuracy
- Mean Average Precision (mAP)

**Calculation**: Metrics are calculated based on heuristics for text generation tasks and traditional metrics for detection and VG tasks.

**Interpretation**: Higher scores indicate better performance in spatial reasoning and dialog generation capabilities.

**Validation**: Extensive experiments evaluating trending MLLMs and comparisons against existing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
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
