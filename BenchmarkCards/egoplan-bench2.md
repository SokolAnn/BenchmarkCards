# EgoPlan-Bench2

## 📊 Benchmark Details

**Name**: EgoPlan-Bench2

**Overview**: EgoPlan-Bench2 is a benchmark designed to assess the planning capabilities of Multimodal Large Language Models (MLLMs) across a wide range of real-world scenarios, including everyday tasks spanning 4 major domains and 24 detailed scenarios.

**Data Type**: multiple-choice question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EgoPlan-Bench

**Resources**:
- [Resource](https://qiulu66.github.io/egoplanbench2/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the planning capabilities of MLLMs in real-world scenarios and to promote further enhancements in MLLM planning proficiency.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: Ego4D dataset consisting of 3,900 hours of egocentric videos.

**Size**: 1,321 multiple-choice QA pairs sourced from 1,113 videos

**Format**: multiple-choice

**Annotation**: Generated through a semi-automatic process utilizing GPT-4 for task goal extraction and multiple-choice QA generation, followed by manual verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Measurement of model performance based on the percentage of correctly predicted actions compared to the ground truth.

**Interpretation**: Performance is understood in terms of accuracy rates where 25% represents random guessing due to four options in each question.

**Baseline Results**: GPT-4V achieved an overall accuracy of 32.63%.

**Validation**: Model performance evaluated across various domains and scenarios featuring multiple-choice questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
