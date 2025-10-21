# REXTIME: A Benchmark Suite for Reasoning-Across-Time in Videos

## 📊 Benchmark Details

**Name**: REXTIME: A Benchmark Suite for Reasoning-Across-Time in Videos

**Overview**: REXTIME is a benchmark designed to rigorously test AI models’ ability to perform temporal reasoning within video events, focusing on human-like understanding when the question and its corresponding answer occur in different video segments.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://rextime.github.io/)
- [Resource](https://huggingface.co/datasets/ReXTime/ReXTime)
- [GitHub Repository](https://github.com/ReXTime/ReXTime)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively assess the reasoning-across-time capabilities of multimodal AI models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Visual Question Answering
- Temporal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: ActivityNet and QVHighlights datasets

**Size**: 9,695 training samples, 921 validation samples, 2,143 test samples

**Format**: JSON

**Annotation**: Manually curated for accuracy and relevance

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- mIoU
- Recall@1

**Calculation**: Accuracy for multiple-choice VQA and moment retrieval metrics

**Interpretation**: Models are evaluated on their accuracy in answering questions and localizing answer events.

**Baseline Results**: Human accuracy: 87.98%; GPT-4o accuracy: 73.67%

**Validation**: Rigorous human curation and automated question-answer generation

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information in curated data.

**Data Licensing**: Released under CC BY-NC-SA 4.0 license for data; MIT license for code.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
