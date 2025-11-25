# TableBench

## 📊 Benchmark Details

**Name**: TableBench

**Overview**: TableBench is a comprehensive and complex benchmark covering 18 subcategories within four major categories of Table Question Answering (TableQA) abilities. It includes real-world challenges in tabular data interpretation and reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/TableBench/TableBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TableBench is to evaluate a broad spectrum of TableQA capabilities and bridge the gap between academic benchmarks and real-world applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fact Checking
- Numerical Reasoning
- Data Analysis
- Visualization

**Limitations**: The benchmark does not extensively explore the inherent complexities of the tables themselves.

## 💾 Data

**Source**: Raw tabular data was collected from existing datasets including WTQ, SQA, TabFact, FeTaQA, and FinQA.

**Size**: 886 samples

**Format**: N/A

**Annotation**: Manual construction and annotation of questions across different categories.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE-L

**Calculation**: Evaluation is based on measuring the n-gram overlap with reference answers.

**Interpretation**: Performance is assessed based on generation quality and capability to process tabular data.

**Baseline Results**: GPT-4 shows substantial performance, yet remains below human performance thresholds.

**Validation**: Extensive experiments were conducted to evaluate more than 30 LLMs across the reasoning methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
