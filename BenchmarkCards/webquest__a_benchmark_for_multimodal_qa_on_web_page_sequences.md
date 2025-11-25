# WebQuest: A Benchmark for Multimodal QA on Web Page Sequences

## 📊 Benchmark Details

**Name**: WebQuest: A Benchmark for Multimodal QA on Web Page Sequences

**Overview**: WebQuest is a multi-page question-answering dataset that requires reasoning across multiple related web pages, evaluating information extraction, multimodal retrieval, and composition of information from many web pages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2409.13711)

## 🎯 Purpose and Intended Users

**Goal**: To assess information retrieval, reasoning, and navigation capabilities of multimodal models in a more realistic web usage scenario.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various popular websites focused on different functionalities.

**Size**: 1,146 examples

**Format**: N/A

**Annotation**: Questions created based on screenshots and reviewed for quality by human raters.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Relaxed Accuracy

**Calculation**: Allows a margin of ±0.05 for numerical answers and uses SQuAD pre-processing for string match.

**Interpretation**: Higher scores indicate better model performance, particularly in multi-screen reasoning.

**Baseline Results**: Various state-of-the-art multimodal models evaluated with Relaxed Accuracy, with GPT-4V achieving the highest score.

**Validation**: Data validation performed to ensure quality and to remove personally identifiable information.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Screens containing personally identifiable information were removed during data validation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
