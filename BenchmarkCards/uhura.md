# Uhura

## 📊 Benchmark Details

**Name**: Uhura

**Overview**: Uhura is a new benchmark designed to evaluate LMs’ scientific knowledge and truthfulness in six low-resource African languages, consisting of two tasks: Uhura-ARC-Easy (multiple-choice science questions) and Uhura-TruthfulQA (evaluating truthfulness on various topics).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Amharic
- Hausa
- Northern Sotho
- Swahili
- Yoruba
- Zulu

**Similar Benchmarks**:
- ARC (AI2 Reasoning Challenge)
- TruthfulQA

**Resources**:
- [Resource](https://www.huggingface.co/masakhane)
- [Resource](https://www.uhura.dev/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of language models on scientific knowledge and truthfulness in low-resource African languages.

**Target Audience**:
- ML Researchers
- Language Model Developers
- NLP Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was created via human translation of established benchmarks (ARC-Easy and TruthfulQA).

**Size**: Approximately 1,200 questions per language for ARC-Easy and up to 817 questions for TruthfulQA.

**Format**: N/A

**Annotation**: Translations were conducted by professional translators, with quality control by language coordinators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Zero-shot prompting
- Five-shot prompting

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly answered questions.

**Interpretation**: Higher accuracy indicates better performance of language models in understanding and responding to questions in low-resource African languages.

**Baseline Results**: Closed models consistently outperformed open models, with specific accuracies reported in the evaluation results.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal identifying information is included in the datasets.

**Data Licensing**: The Uhura benchmark datasets are released under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license.

**Consent Procedures**: All translators provided informed consent for their involvement.

**Compliance With Regulations**: Not Applicable
