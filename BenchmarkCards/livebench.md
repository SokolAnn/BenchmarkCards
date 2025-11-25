# LIVEBENCH

## 📊 Benchmark Details

**Name**: LIVEBENCH

**Overview**: LiveBench is a new benchmark for LLMs designed to be resistant to both test set contamination and the pitfalls of LLM judging and human crowdsourcing. It contains frequently updated questions from recent information sources, scores answers automatically according to objective ground-truth values, and has a variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Big-Bench Hard
- AMPS
- IFEval

**Resources**:
- [Resource](https://livebench.ai)
- [GitHub Repository](https://github.com/livebench/livebench)

## 🎯 Purpose and Intended Users

**Goal**: To mitigate both test set contamination and the pitfalls of LLM judging and human crowdsourcing in LLM evaluation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Math
- Coding
- Reasoning
- Instruction Following
- Language Comprehension
- Data Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Questions drawn from recent math competitions, arXiv papers, news articles, and datasets.

**Size**: 1,000 questions

**Format**: N/A

**Annotation**: Automatically generated based on objective ground-truth values.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the proportion of correctly answered questions.

**Interpretation**: An accuracy score represents the percentage of correctly answered questions out of the total questions.

**Baseline Results**: N/A

**Validation**: LiveBench is validated through regular inspections of incorrect answers and adjustments to scoring functions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache License 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
