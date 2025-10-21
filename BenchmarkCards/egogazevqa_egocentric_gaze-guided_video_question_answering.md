# EgoGazeVQA (Egocentric Gaze-Guided Video Question Answering)

## 📊 Benchmark Details

**Name**: EgoGazeVQA (Egocentric Gaze-Guided Video Question Answering)

**Overview**: EgoGazeVQA is an egocentric gaze-guided video question answering benchmark designed to evaluate the ability of existing MLLMs to interpret user intentions from first-person videos by leveraging gaze information.

**Data Type**: gaze-based question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- QaEgo4D
- EgoThink
- EgoSchema

**Resources**:
- [GitHub Repository](https://github.com/anonyupload/EgoGazeVQA)
- [Resource](https://huggingface.co/datasets/anonupload/EgoGazeVQA-91-nips25)

## 🎯 Purpose and Intended Users

**Goal**: To assess whether MLLMs can utilize egocentric gaze signals for analyzing daily-routine videos.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from egocentric video clips sourced from Ego4D, EgoExo4D, and EGTEA Gaze+ with gaze tracking data.

**Size**: 913 videos with 1757 QA pairs

**Format**: JSON

**Annotation**: Generated using MLLMs and refined by human annotators for relevance, answerability, fluency, accuracy, conciseness, and difficulty.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The performance is assessed by comparing model predictions to ground truth labels.

**Interpretation**: A higher accuracy percentage indicates better performance in understanding user intentions.

**Baseline Results**: Baseline performance of various MLLMs on EgoGazeVQA includes a maximum accuracy of 60.5% for Qwen2.5-VL-72B.

**Validation**: Models were evaluated on their ability to leverage gaze information in question-answering tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
