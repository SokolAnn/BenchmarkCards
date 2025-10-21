# CARL-GT

## 📊 Benchmark Details

**Name**: CARL-GT

**Overview**: CARL-GT is a benchmark for evaluating Causal Reasoning capabilities of large Language Models using Graphs and Tabular data. It includes various tasks for causal graph reasoning, knowledge discovery, and decision-making.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/TURuibo/CauTabBench/tree/main/carl_gt)

## 🎯 Purpose and Intended Users

**Goal**: To measure the capabilities of large language models in causal reasoning through diverse tasks involving causal graph reasoning, knowledge discovery, and decision making.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Causal Graph Reasoning
- Knowledge Discovery
- Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: Generated causal graphs and corresponding tabular data based on structural causal models.

**Size**: 10 causal graphs, corresponding observational data

**Format**: Markdown

**Annotation**: Automatically generated based on defined causal relationships.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall
- Accuracy
- Mean Absolute Error (MAE)

**Calculation**: Metrics calculated based on the accuracy of predictions compared with ground-truth results for various causal reasoning tasks.

**Interpretation**: Higher scores indicate better performance in understanding and inferring causal relationships.

**Baseline Results**: Results from multiple LLMs evaluated across various tasks.

**Validation**: The benchmark tasks were validated to reflect real-world causal reasoning scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
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
