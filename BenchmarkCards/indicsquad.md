# IndicSQuAD

## 📊 Benchmark Details

**Name**: IndicSQuAD

**Overview**: IndicSQuAD is a comprehensive multi-lingual extractive QA dataset covering nine major Indic languages, systematically derived from the SQuAD dataset, aimed to improve question-answering systems for low-resource Indic languages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- Bengali
- Marathi
- Telugu
- Tamil
- Gujarati
- Punjabi
- Kannada
- Odia
- Malayalam

**Similar Benchmarks**:
- MahaSQuAD
- TyDiQA
- XQuAD
- MLQA
- Indic QA Benchmark
- L3Cube-IndicQuest

**Resources**:
- [GitHub Repository](https://github.com/l3cube-pune/indic-nlp)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality findable question-answering dataset for Indic languages to facilitate the development of robust and inclusive NLP applications.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Language Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Systematically translated and adapted from the SQuAD dataset.

**Size**: 118,516 training samples, 11,873 validation samples, 11,803 test samples for each language.

**Format**: JSON

**Annotation**: Translated with linguistic fidelity and answer-span alignment techniques applied.

## 🔬 Methodology

**Methods**:
- Evaluation using baseline performance metrics on QA tasks
- Comparison of monolingual and multilingual models

**Metrics**:
- Exact Match (EM)
- F1 Score

**Calculation**: Performance metrics calculated based on the predictions of the models against the ground truth in the dataset.

**Interpretation**: Higher EM and F1 scores indicate better performance in extracting answer spans accurately.

**Baseline Results**: EM scores for models vary; for example, HindiRoBERTa achieved EM of 56.20%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
