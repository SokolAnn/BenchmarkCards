# NPHardEval

## 📊 Benchmark Details

**Name**: NPHardEval

**Overview**: NPHardEval is a benchmark designed to evaluate the reasoning abilities of Large Language Models (LLMs) across a broad spectrum of 900 algorithmic questions extending up to the NP-Hard complexity class. The benchmark aims to provide a rigorous and quantitative assessment of LLMs' logical reasoning capabilities, and includes a dynamic updating mechanism to mitigate overfitting.

**Data Type**: algorithmic questions

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GAOKAO
- HellaSwag

**Resources**:
- [GitHub Repository](https://github.com/casmlab/NPHardEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous assessment of the reasoning capabilities of LLMs across complex algorithmic questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Complex Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Dynamic generation of algorithmic reasoning problems categorized by complexity classes.

**Size**: 900 questions

**Format**: JSON

**Annotation**: Automatically generated with verification by established algorithms.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Weighted Accuracy
- Failure Rate

**Calculation**: Weighted Accuracy calculated based on the accuracy at different difficulty levels, each weighted to reflect its importance.

**Interpretation**: Higher performance indicates better reasoning capabilities in complex problem solving.

**Baseline Results**: Performance compared across 12 LLMs on various reasoning tasks.

**Validation**: Frequent updates to the benchmark every month to prevent overfitting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
