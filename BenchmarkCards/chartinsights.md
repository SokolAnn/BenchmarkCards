# ChartInsights

## 📊 Benchmark Details

**Name**: ChartInsights

**Overview**: ChartInsights is a newly curated dataset specifically designed for evaluating low-level Chart Question Answering (ChartQA) tasks, consisting of 22,347 samples covering 10 data analysis tasks across 7 chart types.

**Data Type**: chart-query-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA
- DVQA
- MixFigureQA
- ChartBench

**Resources**:
- [Resource](https://chartinsight.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of Multimodal Large Language Models (MLLMs) on low-level chart question answering tasks.

**Target Audience**:
- ML Researchers
- Data Scientists
- Model Developers

**Tasks**:
- Data Retrieval
- Reasoning
- Filter
- Determine Range
- Cluster
- Find Extreme
- Correlation
- Find Anomaly
- Order
- Distribution

**Limitations**: Limited to specific chart types and low-level tasks.

## 💾 Data

**Source**: Curated from existing datasets like nvBench and ChartQA.

**Size**: 22,347 samples

**Format**: N/A

**Annotation**: Automated generation and manual review of task-query pairs.

## 🔬 Methodology

**Methods**:
- Systematic evaluation of MLLMs
- Textual and visual prompts
- Quantitative analysis of model performance

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the ratio of correct answers to total questions.

**Interpretation**: Accuracy rates indicate the strength of MLLMs in processing low-level ChartQA tasks.

**Baseline Results**: Average accuracy of tested models ranges from 39.8% to 84.32%.

**Validation**: Validation conducted through testing a random 20% of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misunderstanding of chart data due to hallucinations in MLLMs.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
