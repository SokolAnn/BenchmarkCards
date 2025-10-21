# CodeMixBench

## 📊 Benchmark Details

**Name**: CodeMixBench

**Overview**: CodeMixBench provides a comprehensive evaluation benchmark for assessing the code-mixing capabilities of large language models across 18 languages and eight tasks, including knowledge reasoning, mathematical reasoning, and traditional NLP tasks.

**Data Type**: question-answering pairs, sentiment analysis pairs, language identification pairs, named entity recognition pairs, part-of-speech tagging pairs, machine translation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Chinese
- Hindi
- Bengali
- Arabic
- Marathi
- Tamil
- Malayalam
- Dutch
- German
- Frisian
- Hokkien
- Guarani
- N/A
- N/A

**Similar Benchmarks**:
- LinCE
- GLUECoS

**Resources**:
- [GitHub Repository](https://github.com/Jeromeyluck/CodeMixBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models on multilingual code-mixing tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Knowledge Reasoning
- Mathematical Reasoning
- Truthfulness
- Language Identification
- Part of Speech Tagging
- Named Entity Recognition
- Sentiment Analysis
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic datasets generated from parallel corpora and existing multilingual datasets.

**Size**: 22 datasets across various tasks

**Format**: N/A

**Annotation**: Synthetic generated with filtering for quality and linguistic coherence.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score

**Calculation**: Metrics calculated based on the model's performance on various code-mixing tasks.

**Interpretation**: Higher scores indicate better performance in understanding and processing code-mixed language.

**Validation**: Extensive filtering and evaluation processes implemented to ensure data quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
