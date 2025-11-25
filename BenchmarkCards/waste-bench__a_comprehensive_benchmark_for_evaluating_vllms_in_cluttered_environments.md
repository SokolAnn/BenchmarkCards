# Waste-Bench: A Comprehensive Benchmark for Evaluating VLLMs in Cluttered Environments

## 📊 Benchmark Details

**Name**: Waste-Bench: A Comprehensive Benchmark for Evaluating VLLMs in Cluttered Environments

**Overview**: Waste-Bench is designed to evaluate the robustness and reasoning capabilities of Vision-Language Large Models (VLLMs) in waste classification, addressing the complexities of real-world applications involving cluttered scenes and deformed objects.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SEED-Bench
- MV-Bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of Waste-Bench is to rigorously test and evaluate the capabilities of VLLMs in handling waste classification tasks under challenging conditions.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Classification
- Counting
- Geometric Shape Analysis
- Color Recognition
- Complex and Cluttered Environment Reasoning

**Limitations**: The scope of evaluation is limited to a specific set of cluttered environments, which may not fully represent the variety of real-world scenarios.

## 💾 Data

**Source**: ZeroWaste dataset

**Size**: 952 images, 9,520 question-answer pairs

**Format**: JSON

**Annotation**: Human-in-the-loop filtering and review process ensuring quality and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Calculated based on the number of correct predictions over total predictions.

**Interpretation**: Accuracy reflects the model's ability to answer questions correctly based on the visual content.

**Validation**: Models evaluated under consistent conditions, ensuring uniformity across tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal identification details are included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
