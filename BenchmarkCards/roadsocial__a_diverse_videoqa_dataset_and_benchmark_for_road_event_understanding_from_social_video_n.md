# RoadSocial: A Diverse VideoQA Dataset and Benchmark for Road Event Understanding from Social Video Narratives

## 📊 Benchmark Details

**Name**: RoadSocial: A Diverse VideoQA Dataset and Benchmark for Road Event Understanding from Social Video Narratives

**Overview**: RoadSocial is a large-scale, diverse VideoQA dataset tailored for generic road event understanding from social media narratives, addressing existing datasets' regional and viewpoint biases.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Lingo-QA
- SUTD-TrafficQA
- DRAMA

**Resources**:
- [Resource](https://roadsocial.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rich benchmark for the evaluation of Video LLMs in understanding road events through videos and social media narratives.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Road Safety Advocates

**Tasks**:
- Video Question Answering
- Road Event Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Social media videos from Twitter capturing road events and accompanying narratives.

**Size**: 13.2K videos, 260K QA pairs, 414K social comments

**Format**: JSON

**Annotation**: Semi-automatic framework using Text and Video LLMs with expert verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- GPT-3.5 Score
- Mean Average Precision (mAP)

**Calculation**: Scores are derived from the semantic alignment between model-generated and ground truth answers.

**Interpretation**: Higher scores indicate better alignment with ground truth answers, suggesting improved comprehension of road events.

**Validation**: Dataset validated through human expert annotations and performance metrics across various Video LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Our data collection adheres to ethical guidelines and uses only publicly available content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
