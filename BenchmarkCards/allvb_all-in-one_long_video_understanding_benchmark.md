# ALLVB (All-in-One Long Video Understanding Benchmark)

## 📊 Benchmark Details

**Name**: ALLVB (All-in-One Long Video Understanding Benchmark)

**Overview**: ALLVB is a long video understanding benchmark designed to assess the capabilities of Multi-modal LLMs (MLLMs) across 9 major video understanding tasks with 1,376 videos, each averaging nearly 2 hours, and a total of 252,420 Q&A pairs.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/ALLVB/ALLVB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and challenging benchmark for evaluating long video understanding capabilities of MLLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Classification
- Scene Recognition
- Object Detection and Tracking
- Action Recognition
- Temporal Action Localization
- Event Detection
- Video Captioning
- Video Emotion Recognition
- Needle-in-a-Haystack

**Limitations**: The benchmark currently includes only movie videos.

## 💾 Data

**Source**: 1,376 feature-length movies collected from open-source websites

**Size**: 1,376 movies, 2,628 hours total

**Format**: JSON

**Annotation**: Automated using GPT-4 with human quality control

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the number of correct answers identified by models against the total Q&As.

**Interpretation**: Higher accuracy indicates better understanding of long video content by the modeled LLM.

**Validation**: Validation through rigorous manual review and testing various MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark does not target specific demographic characteristics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-NC-SA-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
