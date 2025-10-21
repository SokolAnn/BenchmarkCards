# DCA-Bench (Dataset Curation Agents Benchmark)

## 📊 Benchmark Details

**Name**: DCA-Bench (Dataset Curation Agents Benchmark)

**Overview**: DCA-Bench aims to provide a comprehensive benchmark for evaluating LLM agents’ capability to discover data quality issues across online dataset platforms, highlighting the need for further exploration and research in autonomous dataset curation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/TRAIS-Lab/dca-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of LLM agents in discovering hidden data quality issues in datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dataset Curation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from real issues reported by users or maintainers of popular dataset platforms, including Hugging Face, Kaggle, and BIG-Bench.

**Size**: 221 test cases

**Format**: N/A

**Annotation**: Manually verified issues collected during the dataset curation process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics using LLMs

**Metrics**:
- Success Rate
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the outputs of the Curator agents compared to ground truth annotations.

**Interpretation**: The Curator's performance is classified into three levels: fail, success, and success+ based on the correctness of identified issues and provided contextual evidence.

**Baseline Results**: Top-performing models achieved about 29.86% success rate without hints and 78.28% with the most specific hints.

**Validation**: The reliability of the automatic evaluation scheme was validated through extensive comparisons with human annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is collected from platforms like Hugging Face, Kaggle, and GitHub, compliant with their respective terms.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
