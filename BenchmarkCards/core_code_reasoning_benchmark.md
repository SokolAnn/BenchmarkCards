# CORE (Code Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: CORE (Code Reasoning Benchmark)

**Overview**: CORE is a high-quality, human-verified benchmark designed to evaluate LLMs on fundamental static analysis tasks including data dependency, control dependency, and information flow across programs written in C/C++, Java, and Python, containing 12,553 task instances.

**Data Type**: program analysis tasks

**Domains**:
- Software Engineering

**Languages**:
- C
- C++
- Java
- Python

**Similar Benchmarks**:
- SWE-Bench
- SWE-Lancer

**Resources**:
- [Resource](https://corebench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a fine-grained evaluation of LLMs’ code semantic reasoning ability by assessing core program analysis skills.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Data Dependency
- Control Dependency
- Information Flow

**Limitations**: Focuses on relatively short functions (within 100 LoC) to manage annotation complexity.

## 💾 Data

**Source**: Drawn from CodeNet and Google Code Jam datasets.

**Size**: 12,553 task instances

**Format**: N/A

**Annotation**: Semi-automated with substantial human effort ensuring soundness and completeness.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics computed as averages across evaluated models on dependency classification, trace generation, and dependency source enumeration.

**Interpretation**: Higher scores indicate better model performance in recognizing dependencies and generating accurate traces.

**Baseline Results**: Empirical evaluation reveals significant performance variance among LLMs, with reasoning models generally outperforming non-reasoning models.

**Validation**: Tested for reliability with human verification of task instances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
