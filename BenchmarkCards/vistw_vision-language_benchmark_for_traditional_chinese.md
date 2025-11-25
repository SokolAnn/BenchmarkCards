# VisTW (Vision-Language Benchmark for Traditional Chinese)

## 📊 Benchmark Details

**Name**: VisTW (Vision-Language Benchmark for Traditional Chinese)

**Overview**: VisTW is a comprehensive evaluation benchmark for Vision-Language Models in Traditional Chinese, consisting of two components: VisTW-MCQ, a collection of multiple-choice questions from 21 subjects, and VisTW-Dialogue, focusing on open dialogue in Taiwanese cultural contexts.

**Data Type**: question-answering pairs, image-question pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Education

**Languages**:
- Traditional Chinese

**Similar Benchmarks**:
- TMMLU (Traditional Chinese Massive Multitask Language Understanding)
- CMMU (Chinese Multi-modal Multi-type Understanding)
- MMMU (Massive Multidiscipline Multimodal Understanding)

**Resources**:
- [GitHub Repository](https://github.com/TMMMU-Benchmark/evaluation)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of Vision-Language Models in understanding and generating Traditional Chinese in the context of Taiwanese culture.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Visual Question Answering
- Open-Ended Dialog Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various Taiwanese educational assessments and manually curated image-question pairs from real-life scenarios.

**Size**: 3,795 questions and 131 image-question pairs

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Spearman correlation

**Calculation**: Metrics are calculated based on accuracy of responses and correlation between model scores and human evaluations.

**Interpretation**: Higher scores indicate better performance in understanding and reasoning about Traditional Chinese cultural contexts.

**Baseline Results**: N/A

**Validation**: Model performance is validated against human scores through multiple evaluation frameworks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark includes diverse geographic sampling across Taiwan.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Images were collected with consent and no personally identifiable information was included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Contributors explicitly waived ownership rights for the images used in the benchmark.

**Compliance With Regulations**: Not Applicable
