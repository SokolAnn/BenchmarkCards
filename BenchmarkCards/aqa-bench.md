# AQA-Bench

## 📊 Benchmark Details

**Name**: AQA-Bench

**Overview**: AQA-Bench is a novel benchmark to assess the sequential reasoning capabilities of large language models (LLMs) in algorithmic contexts, including binary search, depth-first search, and breadth-first search.

**Data Type**: interactive Q&A pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/UCSC-VLAA/AQA-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively assess LLMs' proficiency in executing predefined algorithmic procedures and evaluate their sequential reasoning ability.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Sequential Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Dynamically generated environments based on predefined parameters.

**Size**: 400 test cases for each base environment under EASY mode, 1500 for HARD mode.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Goal metric
- Policy metric

**Calculation**: Metrics are calculated based on model outputs relative to ground truth and the efficiency of the model's policy.

**Interpretation**: Lower scores in goal metrics indicate better performance; the goal metric is prioritized over the policy metric.

**Baseline Results**: N/A

**Validation**: Evaluations run with multiple models across various environments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
