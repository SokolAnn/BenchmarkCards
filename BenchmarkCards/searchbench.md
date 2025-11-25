# SearchBench

## 📊 Benchmark Details

**Name**: SearchBench

**Overview**: SearchBench is a benchmark designed to evaluate large language models' ability to solve combinatorial search problems that require backtracking and consideration of multiple action sequences.

**Data Type**: combinatorial search problems

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- PuzzleBench

**Resources**:
- [Resource](https://arxiv.org/abs/2406.12172)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capabilities of LLMs on combinatorial search problems through a comprehensive analysis.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Pathfinding
- Puzzle Solving
- Subset Sum Problems
- Sorting Problems
- Under-determined Systems

**Limitations**: N/A

## 💾 Data

**Source**: Automated generation pipelines creating instances of combinatorial problems.

**Size**: 1,107 fixed instances

**Format**: N/A

**Annotation**: Automatically generated with strict adherence to problem rules.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Feasibility
- Correctness
- Optimality

**Calculation**: Metrics are computed through an automated evaluation pipeline that assesses LLM-generated solutions.

**Interpretation**: A solution is valid if it meets the goals of feasibility, correctness, and optimality.

**Validation**: Validation of model performances against defined benchmarks and human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons (CC BY-SA)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
