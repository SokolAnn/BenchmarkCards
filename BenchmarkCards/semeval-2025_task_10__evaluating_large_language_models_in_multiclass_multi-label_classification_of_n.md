# SemEval-2025 Task 10: Evaluating Large Language Models in Multiclass Multi-label Classification of News Entity Framing

## 📊 Benchmark Details

**Name**: SemEval-2025 Task 10: Evaluating Large Language Models in Multiclass Multi-label Classification of News Entity Framing

**Overview**: This paper presents the QUST team's participation in subtask 1 of SemEval-2025 Task 10, which involves multiclass multi-label classification of news entity framing using large language models (LLMs) enhanced by instruction tuning and a voting mechanism to improve predictions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi
- Russian
- Portuguese
- Bulgarian

**Resources**:
- [GitHub Repository](https://github.com/warmth27/SemEval2025_Task10)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the performance of large language models for fine-grained role labeling in multilingual news articles.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Official development and test data from SemEval-2025 Task 10.

**Size**: Data sizes vary by language; specific numbers are provided for English, Hindi, Russian, Portuguese, and Bulgarian datasets.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Ensemble learning via voting

**Metrics**:
- Exact Match Ratio

**Calculation**: Exact match ratio is calculated based on the predictions of the ensemble of top-3 models.

**Interpretation**: Higher exact match ratio indicates better model performance in classifying roles in news articles.

**Baseline Results**: The best performance was achieved with a voting strategy of model combinations: Phi-3-small, Phi-3-medium, and Phi-4.

**Validation**: Results evaluated against the official test data of SemEval-2025 Task 10.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
