# GLBench

## 📊 Benchmark Details

**Name**: GLBench

**Overview**: GLBench is the first comprehensive benchmark for evaluating GraphLLM methods in both supervised and zero-shot scenarios, enabling fair comparisons among different categories of GraphLLM methods and traditional graph neural networks.

**Data Type**: node classification tasks with text attributes

**Domains**:
- Natural Language Processing
- Social Networks

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/NineAbyss/GLBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified evaluation framework for GraphLLM methods and support comparative analysis across different methods and datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Node Classification

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available datasets covering text-attributed graphs across multiple domains.

**Size**: 7 datasets

**Format**: PT format using PyTorch

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Supervised learning evaluation
- Zero-shot learning evaluation

**Metrics**:
- Accuracy
- Macro-F1 score

**Calculation**: Metrics are calculated based on model predictions against ground truth labels for various classification tasks.

**Interpretation**: Higher accuracy and Macro-F1 scores indicate better performance in predicting node classifications.

**Baseline Results**: N/A

**Validation**: Consistency in data processing and experimental settings across multiple datasets for fair evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Datasets are under the MIT License unless otherwise specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
