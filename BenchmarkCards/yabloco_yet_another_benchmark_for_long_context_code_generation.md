# YABLoCo (Yet Another Benchmark for Long Context Code Generation)

## 📊 Benchmark Details

**Name**: YABLoCo (Yet Another Benchmark for Long Context Code Generation)

**Overview**: The benchmark contributes a test set of 215 functions selected from four large repositories, focusing on function body generation in large C and C++ repositories, capturing relevant context in large repositories and generating runnable code.

**Data Type**: function examples with metadata, docstrings, and function bodies

**Domains**:
- Software Engineering

**Languages**:
- C
- C++

**Similar Benchmarks**:
- HumanEval
- MBPP
- CoderEval

**Resources**:
- [GitHub Repository](https://github.com/yabloco-codegen/yabloco-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating code generation models in large C/C++ repositories, addressing the challenges posed by long contexts in code generation.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Code Generation

**Limitations**: The benchmark is limited to C/C++ languages and is based on only four selected repositories.

## 💾 Data

**Source**: Data is collected from four large open-source repositories: llvm-project, bullet3, openssl, and redis.

**Size**: 215 function examples

**Format**: N/A

**Annotation**: Function context and other metadata analyzed and extracted using a clang-based tool.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Qualitative evaluation

**Metrics**:
- Pass@k
- Exact Match (EM)
- Edit Similarity (ES)

**Calculation**: Metrics are calculated by evaluating generated functions against tests from the original repositories.

**Interpretation**: Higher scores indicate better performance for code generation models, with pass@k measuring the functional correctness of the generated code.

**Baseline Results**: Results from baseline models CodeLlama, DeepSeekCoder, and GPT-4 were evaluated on the benchmark.

**Validation**: The pipeline includes a rigorous environment setup including building Docker images for each repository and running test suites.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
