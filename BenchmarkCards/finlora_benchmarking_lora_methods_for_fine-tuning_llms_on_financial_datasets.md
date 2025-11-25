# FinLoRA (Benchmarking LoRA Methods for Fine-Tuning LLMs on Financial Datasets)

## 📊 Benchmark Details

**Name**: FinLoRA (Benchmarking LoRA Methods for Fine-Tuning LLMs on Financial Datasets)

**Overview**: FinLoRA is a comprehensive benchmark designed to assess LoRA variants across diverse financial scenarios, with an emphasis on professional XBRL applications. It evaluates the efficacy of LoRA methods on both general and specialized financial tasks using a curated dataset of 19 financial datasets.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- BloombergGPT
- FinGPT
- FinBen
- PIXIU

**Resources**:
- [GitHub Repository](https://github.com/Open-Finance-Lab/FinLoRA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of FinLoRA is to evaluate various LoRA methods on financial tasks, providing insights into their performance and scalability.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Sentiment Analysis
- Named Entity Recognition
- Financial Analysis
- XBRL Tagging
- Financial Reporting

**Limitations**: N/A

## 💾 Data

**Source**: Curated from diverse financial applications and includes four novel datasets derived from SEC filings in XBRL format.

**Size**: 19 datasets, including 122.9k training examples and 31.7k testing examples.

**Format**: N/A

**Annotation**: Manual annotation based on predefined criteria for financial tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BERTScore

**Calculation**: Metrics for all tasks are averaged across different financial tasks, with accuracy and F1 Score calculated per task.

**Interpretation**: Higher scores indicate better model performance on financial tasks, specifically tailored for XBRL applications.

**Baseline Results**: LoRA methods achieved an average performance improvement of 36% over baseline models.

**Validation**: 46 rounds of fine-tuning and 194 rounds of evaluations were conducted.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
