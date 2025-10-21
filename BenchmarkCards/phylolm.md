# PHYLOLM

## 📊 Benchmark Details

**Name**: PHYLOLM

**Overview**: PhyloLM is a method that adapts phylogenetic algorithms to Large Language Models (LLMs) to explore their relationships and predict performance characteristics in benchmarks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- ARC
- HellaSwag
- TruthfulQA
- Winogrande
- GSM8k

**Resources**:
- [GitHub Repository](https://github.com/hrl-team/PhyloLM)
- [Resource](https://colab.research.google.com/drive/1agNE52eUevgdJ3KL3ytv5Y9JBbfJRYqd?usp=copy)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PHYLOLM is to provide a tool that evaluates LLM development, relationships, and capabilities through a phylogenetic lens.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Performance Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Benchmarks include outputs from diverse queries on a selection of LLMs, including both open-source and proprietary models.

**Size**: 156 models evaluated

**Format**: N/A

**Annotation**: Not applicable as the method relies on model outputs rather than annotated data.

## 🔬 Methodology

**Methods**:
- Phylogenetic analysis
- Logistic regression for performance prediction

**Metrics**:
- Pearson correlation coefficient

**Calculation**: Phylogenetic distance is computed based on the similarity of LLM outputs, and benchmark performance is predicted through logistic regression based on these distances.

**Interpretation**: The results demonstrate that phylogenetic distance is significantly correlated with true performance scores across various benchmarks.

**Baseline Results**: N/A

**Validation**: Validated through comparison with ground truth relationships and performance metrics in benchmark tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
