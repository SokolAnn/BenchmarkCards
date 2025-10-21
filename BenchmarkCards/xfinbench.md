# XFINBENCH

## 📊 Benchmark Details

**Name**: XFINBENCH

**Overview**: XFINBENCH is a novel benchmark designed to evaluate the ability of Large Language Models (LLMs) in solving complex, knowledge-intensive financial problems across diverse topics and multi-modal contexts.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- BizBench
- FinEval
- FinanceMATH

**Resources**:
- [GitHub Repository](https://github.com/Zhihan72/XFinBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM’s ability to solve complex and knowledge-intensive financial problems with multi-modal context.

**Target Audience**:
- ML Researchers
- Finance Experts

**Tasks**:
- Statement Judging
- Multi-choice Question Answering
- Financial Calculation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from graduate-level finance textbooks.

**Size**: 4,235 examples

**Format**: N/A

**Annotation**: Manual annotation and automated annotation using GPT-4o.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the performance of LLMs on various tasks within the benchmark.

**Interpretation**: Good performance is indicated by high accuracy in solving complex financial problems.

**Baseline Results**: o1 is the best-performing text-only model with an overall accuracy of 67.3%.

**Validation**: XFINBENCH includes a validation set of 1,000 examples to support model development validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Improper usage']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is sourced from openly available textbooks while adhering to copyright regulations.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
