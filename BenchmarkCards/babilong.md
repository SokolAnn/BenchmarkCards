# BABILong

## 📊 Benchmark Details

**Name**: BABILong

**Overview**: BABILong is a novel generative benchmark designed to evaluate the performance of NLP models in processing arbitrarily long documents with distributed facts, specifically addressing the challenge of extracting and processing these facts within extensive texts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- bAbI
- LongBench

**Resources**:
- [GitHub Repository](https://github.com/booydar/babilong)

## 🎯 Purpose and Intended Users

**Goal**: To assess model capabilities in extracting and processing distributed facts within extremely long documents.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark uses background texts to hide facts, and the chosen background sources may affect results.

## 💾 Data

**Source**: Randomly distributed facts inside book corpus using the PG19 dataset.

**Size**: 11,000,000 tokens

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Evaluation is based on the performance of models on tasks involving question-answering with hidden facts in long texts.

**Interpretation**: Performance assessed based on how well models can identify and answer questions from distributed facts within extensive context.

**Baseline Results**: Evaluated against GPT-4 and RAG models.

**Validation**: Benchmarked across various models, showing performance degradation with increasing context length.

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
