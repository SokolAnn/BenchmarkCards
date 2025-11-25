# Linguistic Understanding and Cognitive Inference Dataset (LUCID)

## 📊 Benchmark Details

**Name**: Linguistic Understanding and Cognitive Inference Dataset (LUCID)

**Overview**: LUCID is a dataset designed to evaluate language models on their understanding of linguistic nuances including negation, tense, voice, and modal variations, comprising carefully crafted sentence pairs in English and Bengali.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English
- Bengali

**Resources**:
- [GitHub Repository](https://github.com/Luciddataset/LUCID)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for language models to assess their ability to understand fine-grained linguistic features across languages.

**Target Audience**:
- ML Researchers
- Educational Technologists
- Language Model Developers

**Tasks**:
- Text Classification
- Linguistic Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Linguistic Understanding and Cognitive Inference Dataset (LUCID) is composed of sentence pairs designed to target linguistic aspects.

**Size**: N/A

**Format**: N/A

**Annotation**: Expertly crafted sentence pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pearson correlation
- Spearman correlation
- Mean Absolute Error (MAE)
- Human Calibration Envelope (HCE) accuracy

**Calculation**: The Human Calibration Envelope (HCE) accuracy is calculated by checking whether model predictions fall within one standard deviation of mean human ratings.

**Interpretation**: A higher HCE accuracy indicates better alignment with human cognitive tolerance and variability.

**Validation**: Evaluation across multiple linguistic phenomena.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Hallucination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
