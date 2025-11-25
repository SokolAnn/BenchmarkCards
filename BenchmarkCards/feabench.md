# FEABench

## 📊 Benchmark Details

**Name**: FEABench

**Overview**: FEABench is a benchmark to evaluate the ability of large language models (LLMs) and LLM agents to simulate and solve physics, mathematics, and engineering problems using finite element analysis (FEA).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Engineering

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/FEABench/gtb)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' ability to solve quantitative problems in physics and engineering using COMSOL Multiphysics through finite element analysis.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Problem Solving
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from tutorials in the COMSOL Multiphysics® Application Gallery and established validation problems.

**Size**: 15 problems for FEABench Gold; 200 algorithmically parsed tasks for FEABench Large.

**Format**: Java API commands for COMSOL Multiphysics®

**Annotation**: Manually verified for correctness and completeness.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Executability
- Model Tree Score
- Physics Metrics
- Target Value Metrics

**Calculation**: Metrics calculated based on the outcomes of executing the code with COMSOL Multiphysics API.

**Interpretation**: A correct solution indicates that the LLM successfully generated the code that solves the simulation problem according to the benchmarks defined in FEABench.

**Baseline Results**: Various LLMs tested with specific metrics reported, such as executability and physical reasoning scores across different tasks.

**Validation**: FEABench Gold problems are manually verified to ensure they yield correct outputs when solved.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
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
