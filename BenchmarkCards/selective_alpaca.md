# Selective Alpaca

## 📊 Benchmark Details

**Name**: Selective Alpaca

**Overview**: Selective Alpaca is a curated instruction tuning (IT) dataset created by applying a novel approach called SelectIT, which improves IT data selection by leveraging the intrinsic uncertainty of large language models (LLMs) without requiring additional resources.

**Data Type**: instruction-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Alpaca-GPT4
- LIMA
- Q2Q
- AlpaGasus

**Resources**:
- [GitHub Repository](https://github.com/Blue-Raincoat/SelectIT)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the performance of large language models by providing a dataset that consists of high-quality instruction data selected using uncertainty-aware methodologies.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Instruction Tuning
- Natural Language Understanding

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is created from the Alpaca-GPT4 dataset using the SelectIT method for high-quality instruction tuning data selection.

**Size**: 10,400 pairs

**Format**: N/A

**Annotation**: The data was selected based on improvement of performance metrics using inherent model uncertainty evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the model's performance on downstream tasks after applying instruction tuning with the dataset.

**Interpretation**: The performance is measured in relation to baseline models to assess improvements in instruction adherence and quality.

**Validation**: Results are validated through comprehensive empirical testing across multiple foundational models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
