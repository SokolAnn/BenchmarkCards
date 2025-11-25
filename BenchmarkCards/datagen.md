# DATAGEN

## 📊 Benchmark Details

**Name**: DATAGEN

**Overview**: DATAGEN is a unified framework for generating textual datasets via LLMs, focusing on enhancing diversity, truthfulness, and controllability in the dataset generation process. It aims to produce high-quality synthetic data efficiently and effectively.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MMLU
- TruthfulQA
- HellaSwag

**Resources**:
- [GitHub Repository](https://github.com/HowieHwong/DataGen)

## 🎯 Purpose and Intended Users

**Goal**: To create high-quality synthetic datasets through a user-controlled framework that ensures diverse, accurate, and adaptable data generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dataset Generation
- Benchmarking LLMs
- Data Augmentation

**Limitations**: N/A

## 💾 Data

**Source**: Generated via LLMs based on provided datasets and user-defined constraints.

**Size**: Variable depending on user specifications (e.g., 200 samples)

**Format**: JSON

**Annotation**: Automatically generated via LLMs with user-defined parameters.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on comparisons between generated data and original datasets.

**Interpretation**: Performance evaluated based on human feedback and automated assessments; higher scores indicate better generation capabilities.

**Validation**: Cross-validation with original datasets and performance benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
