# HOAXPEDIA

## 📊 Benchmark Details

**Name**: HOAXPEDIA

**Overview**: HOAXPEDIA is a collection of 311 hoax articles alongside semantically similar legitimate articles, aimed at fostering research in automated hoax detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Wiki-Reliability

**Resources**:
- [Resource](https://huggingface.co/datasets/hsuvaskakoty/hoaxpedia)
- [GitHub Repository](https://github.com/hsuvas/hoaxpedia_dataset.git)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for the binary classification task of detecting hoax articles in Wikipedia.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: The dataset is small, with only 311 hoax examples, which limits robust training scenarios.

## 💾 Data

**Source**: HOAXPEDIA dataset is constructed from existing literature and official Wikipedia lists of hoaxes.

**Size**: 311 hoax articles and 30,000 legitimate articles

**Format**: JSON

**Annotation**: Manually verified hoax articles using accompanying deletion discussion and reasons.

## 🔬 Methodology

**Methods**:
- Binary classification
- Language model evaluation

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated on the positive class (hoax).

**Interpretation**: Higher F1 Score indicates better performance in classifying hoaxes.

**Baseline Results**: F1 scores range from 0.58 to 0.88 for various models.

**Validation**: Experimentation on various language models to establish baseline results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
