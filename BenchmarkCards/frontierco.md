# FrontierCO

## 📊 Benchmark Details

**Name**: FrontierCO

**Overview**: FrontierCO is a comprehensive benchmark that covers eight canonical combinatorial optimization problem types and evaluates 16 representative ML-based solvers, providing realistic problem difficulty and abundant training data.

**Data Type**: combinatorial optimization problem instances

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/CO-Bench/FrontierCO)

## 🎯 Purpose and Intended Users

**Goal**: To enable meaningful and comprehensive evaluation of contemporary ML-based combinatorial optimization solvers and provide insights for future research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Combinatorial Optimization

**Limitations**: N/A

## 💾 Data

**Source**: Benchmarks from established repositories and competitions, training data generated using various problem-specific instance generators.

**Size**: Data includes a variety of instances across eight combinatorial optimization problems.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Comparative Evaluation of ML-based CO Solvers

**Metrics**:
- Primal Gap

**Calculation**: Primal gap is computed relative to the best known solution (BKS).

**Interpretation**: Lower primal gap indicates better solver performance.

**Baseline Results**: Human-designed SOTA solvers serve as baselines across different problem types.

**Validation**: Evaluation includes both easy and hard test sets for comprehensive assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
