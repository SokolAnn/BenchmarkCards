# FinNLI (Financial Natural Language Inference)

## 📊 Benchmark Details

**Name**: FinNLI (Financial Natural Language Inference)

**Overview**: FinNLI is a benchmark dataset for Financial Natural Language Inference (NLI) that includes diverse premise-hypothesis pairs across various financial texts such as SEC Filings, Annual Reports, and Earnings Call transcripts. It aims to expose weaknesses in current large language models (LLMs) for financial reasoning.

**Data Type**: premise-hypothesis pairs

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- MedNLI
- FinCausal

**Resources**:
- [Resource](https://huggingface.co/datasets/finnli)

## 🎯 Purpose and Intended Users

**Goal**: The goal of FinNLI is to evaluate and improve NLI model performance in the financial domain, thus enhancing downstream applications of natural language processing in finance.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from real-world financial documents including Annual Reports, SEC Filings, and Earnings Calls.

**Size**: 21,304 pairs

**Format**: N/A

**Annotation**: Annotated by finance experts, the dataset includes a high-quality test set of 3,304 instances.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1 Score

**Calculation**: The Macro F1 Score is calculated as the average of F1 scores across all classes in the test set.

**Interpretation**: Higher Macro F1 Scores indicate better performance of the NLI models on the financial reasoning tasks.

**Baseline Results**: The highest Macro F1 scores observed were 74.57% for pre-trained language models and 78.62% for large language models.

**Validation**: The dataset was validated through expert annotation and pre-processing to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is constructed from publicly available financial documents and does not contain sensitive or personally identifiable information (PII).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
