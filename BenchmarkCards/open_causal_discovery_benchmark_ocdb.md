# Open Causal Discovery Benchmark (OCDB)

## 📊 Benchmark Details

**Name**: Open Causal Discovery Benchmark (OCDB)

**Overview**: The OCDB is a comprehensive evaluation framework for causal discovery algorithms based on real datasets, designed to enhance interpretability and assess causal structures and effects effectively.

**Data Type**: causal graphs and data structures

**Domains**:
- Natural Language Processing
- Healthcare
- Finance
- Natural Sciences

**Languages**:
- English

**Similar Benchmarks**:
- CSuite
- CausalTime
- gCastle

**Resources**:
- [Resource](https://anonymous.4open.science/r/OCDB-6B6B)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized, open platform for the evaluation of causal discovery algorithms using real-world datasets.

**Target Audience**:
- ML Researchers
- Causal Discovery Practitioners
- Data Scientists

**Tasks**:
- Causal Discovery
- Causal Inference

**Limitations**: The computational complexity of CED is high, which may hinder its application on larger datasets.

## 💾 Data

**Source**: Real-world datasets covering various domains, curated for causal discovery tasks.

**Size**: 13 datasets of varying sizes

**Format**: CSV

**Annotation**: Data is curated from multiple sources and processed uniformly.

## 🔬 Methodology

**Methods**:
- Baseline Model Evaluation
- Causal Graph Analysis

**Metrics**:
- Causal Structure Distance (CSD)
- Causal Effect Distance (CED)
- Structural Hamming Distance (SHD-C)
- Structural Intervention Distance (SID)

**Calculation**: Metrics calculated based on the differences in causal structures and causal effects.

**Interpretation**: Lower values indicate better performance in discovering causal relationships.

**Baseline Results**: Detailed results provided for various causal discovery methods and datasets.

**Validation**: Experimental validation against baseline models and existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of variables and their interactions across different datasets included.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All datasets are publicly available for research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
