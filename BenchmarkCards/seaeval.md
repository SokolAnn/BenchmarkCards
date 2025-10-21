# SeaEval

## 📊 Benchmark Details

**Name**: SeaEval

**Overview**: SeaEval is a benchmark for multilingual foundation models, focusing on their understanding and reasoning capabilities in natural language and cultural practices. It assesses classic NLP tasks, complex reasoning, and cross-lingual knowledge transfer.

**Data Type**: multilingual datasets

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Indonesian
- Spanish
- Vietnamese
- Malay
- Filipino

**Similar Benchmarks**:
- MMLU
- GLUE

**Resources**:
- [GitHub Repository](https://github.com/SeaEval/SeaEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of multilingual foundation models across various tasks and cultural understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification
- Complex Reasoning
- Cultural Understanding

**Limitations**: N/A

## 💾 Data

**Source**: 29 datasets including 7 new datasets constructed for cultural reasoning and cross-lingual consistency assessments.

**Size**: 13,263 samples

**Format**: CSV

**Annotation**: Expert annotations and translations by native speakers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L

**Calculation**: Standard evaluation metrics including accuracy for multiple-choice questions and BLEU/ROUGE for generative tasks.

**Interpretation**: Higher scores indicate better performance in multilingual capabilities and reasoning.

**Baseline Results**: Results from multiple large language models are reported against benchmark tasks.

**Validation**: Tests include cross-lingual consistency and evaluation against human-curated datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Misuse**: Non-disclosure

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
