# UVQA (Unanswerable Video Question Answering)

## 📊 Benchmark Details

**Name**: UVQA (Unanswerable Video Question Answering)

**Overview**: The UVQA dataset includes questions designed to extend beyond the content of the video, enabling Video Large Language Models to evaluate the relevance of user queries and refuse answering when the question exceeds the informational boundaries of the video.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ActivityNet QA
- MVSD-QA
- MSRVTT-QA

**Resources**:
- [GitHub Repository](https://github.com/EsYoon7/UVQA)

## 🎯 Purpose and Intended Users

**Goal**: To equip Video Large Language Models with the ability to reject unanswerable questions, thereby improving their performance in real-world QA scenarios.

**Target Audience**:
- AI Researchers
- Machine Learning Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: A key limitation of the approach is the increase in excessive refusal score observed after alignment for answerability, which may lead to undesired refusals for answerable questions.

## 💾 Data

**Source**: Generated using existing video-description paired datasets and perturbed to create unanswerable questions.

**Size**: 30,000 training samples, 300 evaluation samples

**Format**: JSON

**Annotation**: Automatically filtered with human review for evaluation samples.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Direct Preference Optimization

**Metrics**:
- Accuracy
- F1 Score
- Excessive Refusal Score
- Permissiveness Score
- Discretion Score

**Calculation**: Metrics assess model performance in terms of correct identification of answerable and unanswerable questions.

**Interpretation**: Higher scores indicate better performance in recognizing unanswerable questions without declining to answer valid ones.

**Validation**: The dataset was filtered and evaluated with human annotators to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
