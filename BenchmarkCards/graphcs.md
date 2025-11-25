# GraphCS

## 📊 Benchmark Details

**Name**: GraphCS

**Overview**: GraphCS is a comprehensive benchmark designed to evaluate the performance of large language models (LLMs) in community search tasks, addressing the challenges of output bias and the limitations of LLMs in discerning community structures within graphs.

**Data Type**: graph

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MAGMA

**Resources**:
- [Resource](https://arxiv.org/abs/2508.09549)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the GraphCS benchmark is to evaluate the capabilities of LLMs in community search problems in graph analysis.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Community Search

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark includes two algorithmically generated datasets (PSG and LFR) for community search tasks.

**Size**: 12,400 graphs

**Format**: N/A

**Annotation**: Automated generation via graph generating algorithms.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated by comparing the predicted community vertices against ground-truth labels.

**Interpretation**: An F1 Score close to 1 indicates better performance in identifying true community members while avoiding irrelevant vertices.

**Baseline Results**: N/A

**Validation**: The framework employs a dual-agent collaborative model, CS-Agent, which refines outputs through dialogues.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
