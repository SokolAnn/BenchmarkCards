# Video-MMLU (Video-Massive Multi-Discipline Lecture Understanding)

## 📊 Benchmark Details

**Name**: Video-MMLU (Video-Massive Multi-Discipline Lecture Understanding)

**Overview**: Video-MMLU is a large-scale benchmark designed to evaluate the comprehension abilities of Large Multimodal Models (LMMs) on multi-discipline lectures that require both visual perception and reasoning. It involves yielding detailed video captions and answering reasoning questions based on the lectures.

**Data Type**: video-caption pairs and question-answer pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2504.14693)

## 🎯 Purpose and Intended Users

**Goal**: To assess the reasoning and perception capabilities of large multimodal models when analyzing educational lecture videos across various disciplines.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Video Captioning
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from 10 YouTube channels focusing on multi-discipline lectures in mathematics, physics, and chemistry.

**Size**: 1,065 videos and 15,750 question-answering pairs

**Format**: Video with accompanying captions and questions

**Annotation**: Constructed using a multi-stage annotation pipeline integrating video captions and frame-level annotations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the performance of various LMMs across video captioning and question-answering tasks.

**Interpretation**: Higher scores indicate better model performance in understanding and reasoning over lecture videos.

**Baseline Results**: The best-performing model achieves a maximum accuracy ranging from 30% to 50% across evaluated tasks.

**Validation**: Extensive evaluation conducted using over 90 existing LLMs, benchmarked using standard educational metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
