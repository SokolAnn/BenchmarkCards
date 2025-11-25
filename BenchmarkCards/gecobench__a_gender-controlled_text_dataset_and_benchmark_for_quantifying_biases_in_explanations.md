# GECOBench: A Gender-Controlled Text Dataset and Benchmark for Quantifying Biases in Explanations

## 📊 Benchmark Details

**Name**: GECOBench: A Gender-Controlled Text Dataset and Benchmark for Quantifying Biases in Explanations

**Overview**: GECO is a gender-controlled text dataset designed for the development and evaluation of XAI methods. GECOBench is a quantitative benchmarking framework to assess the correctness of machine learning world explanations for language models on gender classification tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/braindatalab/gecobench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous open framework for benchmarking the correctness of explanations of pre-trained language models and aspects of fairness.

**Target Audience**:
- ML Researchers
- XAI Method Developers

**Tasks**:
- Gender Classification

**Limitations**: The benchmark does not consider non-linear feature interactions present in many real-world applications.

## 💾 Data

**Source**: Sentences sourced from Wikipedia pages of popular books with gender manipulation to create male and female sentence variants.

**Size**: 3,220 sentences

**Format**: JSONL

**Annotation**: Manual labeling of gender for subjects and other protagonist words in sentences.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mass Accuracy

**Calculation**: Mass Accuracy is calculated by determining the correctness of explanations against ground truth based on token importance.

**Interpretation**: A perfect Mass Accuracy score indicates that only ground truth tokens are recognized as important.

**Validation**: Validations were conducted by manual checking of explanations against ground truth data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Uncertain data provenance

**Demographic Analysis**: Yes, the dataset was created to be gender-balanced.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
