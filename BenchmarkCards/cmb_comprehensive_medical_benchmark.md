# CMB (Comprehensive Medical Benchmark)

## 📊 Benchmark Details

**Name**: CMB (Comprehensive Medical Benchmark)

**Overview**: The CMB aims to evaluate the performance of large language models in the medical domain, especially focusing on Chinese language medical tasks. This benchmark showcases how dataset diversity and distribution in supervised fine-tuning can enhance model performance, indicating that models can achieve competitive results with smaller parameter sizes by leveraging a diverse dataset.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/CAS-SIAT-XinHai/CollectiveSFT)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of large language models in medical tasks through dataset diversity and supervised fine-tuning.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Named Entity Recognition

**Limitations**: While fine-tuned smaller models excel at answering multiple-choice questions accurately, they may struggle with maintaining engaging and coherent conversations.

## 💾 Data

**Source**: Publicly available medical datasets including PubMedQA, MedMCQA, and others, focused on fostering a diverse training environment.

**Size**: 4,745,140 examples

**Format**: Alpaca format

**Annotation**: Standardized annotation through data reconstruction from various sources.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the model's performance on various tasks demonstrated during testing.

**Interpretation**: Scores reflect model performance across diverse medical tasks, particularly evaluating how well they perform in specialized contexts.

**Validation**: Evaluation involved comparing model performance against established benchmarks in the medical domain.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark considers the diversity of datasets to mitigate biases in data sources.

**Potential Harm**: ['Inaccurate medical advice due to hallucination.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
