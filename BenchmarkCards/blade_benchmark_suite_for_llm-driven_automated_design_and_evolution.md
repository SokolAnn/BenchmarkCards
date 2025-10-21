# BLADE (Benchmark suite for LLM-driven Automated Design and Evolution)

## 📊 Benchmark Details

**Name**: BLADE (Benchmark suite for LLM-driven Automated Design and Evolution)

**Overview**: BLADE is a modular and extensible framework specifically designed for benchmarking LLM-driven Automated Algorithm Discovery methods in a continuous black-box optimisation context.

**Data Type**: benchmark problems for optimisation

**Domains**:
- Computer Science
- Optimization

**Languages**:
- English

**Similar Benchmarks**:
- BBOB
- SBOX-COST

**Resources**:
- [GitHub Repository](https://github.com/XAI-liacs/BLADE)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLM-driven Automated Algorithm Discovery methods for continuous black-box optimisation.

**Target Audience**:
- ML Researchers
- Algorithm Developers

**Tasks**:
- Automated Algorithm Design
- Performance Benchmarking

**Limitations**: N/A

## 💾 Data

**Source**: Several collections of single-objective continuous optimisation problems with instance generation mechanisms, including MA-BBOB and SBOX-COST.

**Size**: 1000 predefined instances

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Experimental setup
- Code Evolution Graph analysis
- Performance comparison against human-designed baselines

**Metrics**:
- Area Over the Convergence Curve (AOCC)
- ELO ratings

**Calculation**: AOCC is calculated based on the average performance of algorithms over multiple runs.

**Interpretation**: Higher AOCC and ELO ratings indicate more effective optimisation algorithms.

**Baseline Results**: Best-performing algorithms were compared against state-of-the-art human-designed algorithms like CMA-ES.

**Validation**: The benchmark was validated through use cases demonstrating its application in LLM-driven AAD methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
