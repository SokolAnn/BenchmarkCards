# REFUTE (Refuting Erroneous Findings Using Targeted Examples)

## 📊 Benchmark Details

**Name**: REFUTE (Refuting Erroneous Findings Using Targeted Examples)

**Overview**: REFUTE is a dynamically updating benchmark designed to evaluate the counterexample generation capabilities of language models for incorrect algorithmic solutions. It consists of problems from programming contests along with their incorrect solutions, challenging models to identify inputs that cause these solutions to fail.

**Data Type**: algorithmic problem-solving tasks with incorrect code submissions

**Domains**:
- Computer Science

**Languages**:
- English
- C++
- Python

**Resources**:
- [GitHub Repository](https://github.com/falsifiers/refute-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the ability of language models to create counterexamples for incorrect algorithmic solutions, thereby improving model reasoning and reflection capabilities.

**Target Audience**:
- Machine Learning Researchers
- Algorithm Developers
- Software Engineers

**Tasks**:
- Counterexample Generation
- Algorithmic Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Incorrect submissions from recent programming contests hosted on Codeforces.

**Size**: 324 samples

**Format**: structured problem statements with incorrect code and correct solutions

**Annotation**: Each sample is annotated with metadata including problem constraints and correct solutions.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Model-based evaluation

**Metrics**:
- Counterexample success rate
- Accuracy of generated solutions

**Calculation**: Metrics are calculated based on the ability of models to produce valid counterexamples that identify failures in incorrect solutions.

**Interpretation**: Performance is interpreted based on the percentage of tasks for which models successfully generate counterexamples.

**Validation**: Counterexamples are validated automatically by comparing the outputs of the incorrect and correct solutions using an input validation script.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
