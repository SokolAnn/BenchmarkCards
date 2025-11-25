# CO-Bench

## 📊 Benchmark Details

**Name**: CO-Bench

**Overview**: CO-Bench is a benchmark suite featuring 36 real-world combinatorial optimization problems drawn from various domains and complexity levels, designed to evaluate LLM agents in the context of efficient CO algorithm development.

**Data Type**: problem instances

**Domains**:
- Computer Science
- Operations Research

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/sunnweiwei/CO-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLM agents in combinatorial optimization through diverse and challenging problems.

**Target Audience**:
- ML Researchers
- Algorithm Developers
- Operations Researchers

**Tasks**:
- Algorithm Development
- Combinatorial Optimization

**Limitations**: N/A

## 💾 Data

**Source**: Real-world combinatorial optimization problems sourced from OR-Library.

**Size**: 6,482 instances

**Format**: N/A

**Annotation**: Manually annotated problem descriptions, data loading functions, and evaluation functions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Agentic frameworks evaluation

**Metrics**:
- Valid Solution
- Above Classical
- Survival Rate

**Calculation**: Scores are calculated based on the normalized score of the primal bound against a pre-computed optimal objective value.

**Interpretation**: Higher scores indicate better performance, with a score of 1 denoting performance identical to the optimal.

**Baseline Results**: Compared with classical solvers such as Gurobi and LKH.

**Validation**: N/A

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
