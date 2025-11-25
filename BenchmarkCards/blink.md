# Blink

## 📊 Benchmark Details

**Name**: Blink

**Overview**: Blink is a new benchmark for multimodal language models (LLMs) that focuses on core visual perception abilities not found in other evaluations. It consists of 14 visual perception tasks recast into multiple-choice questions for LLMs, challenging their capabilities in interpreting visual data.

**Data Type**: multiple-choice questions with images

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMBench
- MMVU
- MM-Vet

**Resources**:
- [Resource](https://zeyofu.github.io/blink/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the visual perception capabilities of existing multimodal LLMs and highlight the gap between human and machine visual perception.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Visual Question Answering
- Image Classification
- Spatial Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various image datasets and created new questions around 14 visual perception tasks.

**Size**: 3,807 questions, 7,358 images

**Format**: multiple-choice questions

**Annotation**: Questions were derived from human annotations and curated from existing datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the number of correct answers given by the models compared to human performance.

**Interpretation**: A higher accuracy indicates better visual perception capabilities of the evaluated multimodal LLMs.

**Baseline Results**: GPT-4V achieved 51.26% in accuracy; human performance was 95.70%.

**Validation**: Each task is validated through human evaluation with an average agreement score of 80-99%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
