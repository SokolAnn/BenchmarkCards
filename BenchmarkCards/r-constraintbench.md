# R-ConstraintBench

## 📊 Benchmark Details

**Name**: R-ConstraintBench

**Overview**: R-ConstraintBench is a scalable framework that evaluates models on Resource-Constrained Project Scheduling Problems (RCPSP), an NP-Complete feasibility class, while difficulty increases via linear growth in constraints.

**Data Type**: scheduling problems

**Domains**:
- Operations Research

**Languages**:
- English

**Similar Benchmarks**:
- OR-Instruct
- IndustryOR
- OptiMUS
- MAMO

**Resources**:
- [Resource](https://arxiv.org/abs/2508.15204)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the feasibility reasoning of leading LLMs under a variety of constraints present in RCPSP.

**Target Audience**:
- ML Researchers
- Operations Researchers
- Model Developers

**Tasks**:
- Scheduling
- Feasibility Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic RCPSP instances generated using a solver-driven pipeline.

**Size**: 6,000 instances

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated verification
- Feasibility checks

**Metrics**:
- Feasibility Rate
- Weighted Area Under the Curve (WAUC)
- Breakpoint Level (BP-Level)

**Calculation**: WAUC metrics are calculated by weighing feasibility rates at different levels of constraint density.

**Interpretation**: Higher WAUC values indicate better feasibility across increasing constraints.

**Baseline Results**: Top models demonstrate feasibility across various RCPSP configurations with failure rates analyzed.

**Validation**: Validation through automated verification of generated schedules against predefined constraints.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
