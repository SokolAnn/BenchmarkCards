# Finance Agent Benchmark

## 📊 Benchmark Details

**Name**: Finance Agent Benchmark

**Overview**: The Finance Agent Benchmark presents challenging and diverse real-world finance research problems that require LLMs to perform complex analysis using recent SEC filings. It provides a comprehensive testbed for measuring the progress of LLM-driven finance agents, featuring 537 expert-authored questions across nine financial task categories.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinQA
- TAT-QA

**Resources**:
- [Resource](https://doi.org/10.57967/hf/5514)
- [Resource](https://doi.org/10.5281/zenodo.15428823)
- [GitHub Repository](https://github.com/vals-ai/finance-agent)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate AI agents on real-world financial analysis tasks.

**Target Audience**:
- ML Researchers
- Finance Professionals
- Model Developers

**Tasks**:
- Information Retrieval
- Complex Financial Modeling
- Market Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Expert-generated dataset using real-world SEC filings and financial documents.

**Size**: 537 questions

**Format**: CSV

**Annotation**: Expert-reviewed for accuracy and relevance.

## 🔬 Methodology

**Methods**:
- LLM-as-judge evaluation
- Rubric-based assessment
- Contradiction detection

**Metrics**:
- Accuracy

**Calculation**: Class-balanced accuracy calculated for each category of questions, along with naive accuracy.

**Interpretation**: Higher accuracy indicates better performance of LLMs in responding to financial queries accurately.

**Baseline Results**: The best-performing model achieved 46.8% accuracy.

**Validation**: Dataset split into public, private validation, and test sets for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 for the dataset and MIT License for the code.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
