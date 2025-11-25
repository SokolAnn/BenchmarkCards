# Qiskit HumanEval (QHE)

## 📊 Benchmark Details

**Name**: Qiskit HumanEval (QHE)

**Overview**: The Qiskit HumanEval dataset is a hand-curated collection of tasks designed to benchmark the ability of Large Language Models (LLMs) to produce quantum code using Qiskit, consisting of more than 100 quantum computing tasks.

**Data Type**: quantum programming tasks

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP

**Resources**:
- [GitHub Repository](https://github.com/Qiskit/qiskit)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the performance of code generation models (LLMs) in producing executable quantum code for a variety of quantum tasks.

**Target Audience**:
- ML Researchers
- Quantum Computing Practitioners
- Model Developers

**Tasks**:
- Quantum Circuit Generation
- Simulation and Execution
- State Preparation and Analysis
- Algorithm Implementation
- Gate Operations and Manipulation
- Visualization and Post-Processing
- Advanced Circuit Manipulation
- Quantum Circuit Serialization

**Limitations**: N/A

## 💾 Data

**Source**: Hand-curated collection created by experts in quantum computing and Qiskit.

**Size**: 101 tasks

**Format**: JSON

**Annotation**: Tasks were manually created and peer-reviewed by a panel of experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass Rate

**Calculation**: The percentage of tasks that the model completed successfully based on the test cases provided.

**Interpretation**: A high pass rate indicates that the model is proficient in generating quantum code that meets the requirements of the tasks.

**Validation**: Tasks were evaluated by running the generated code against pre-defined unit tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All tasks are original and do not contain proprietary information.

**Data Licensing**: All data used is publicly available under permissible licenses such as Apache 2.0, MIT.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
