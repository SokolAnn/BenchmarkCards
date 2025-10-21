# ClassEval-T: Evaluating Large Language Models in Class-Level Code Translation

## 📊 Benchmark Details

**Name**: ClassEval-T: Evaluating Large Language Models in Class-Level Code Translation

**Overview**: ClassEval-T is a class-level code translation benchmark designed to assess the performance of large language models (LLMs) on translating complex class structures in code across multiple programming languages such as Python, Java, and C++. It provides a more accurate evaluation of LLM capabilities in real-world software development tasks compared to previous benchmarks focused on statement or method-level translations.

**Data Type**: class-level code samples

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- C++

**Similar Benchmarks**:
- ClassEval

**Resources**:
- [GitHub Repository](https://github.com/wLinHoo/ClassEval-T)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the performance of large language models in translating complex, class-level coding tasks.

**Target Audience**:
- ML Researchers
- Software Developers
- Data Scientists

**Tasks**:
- Code Translation

**Limitations**: N/A

## 💾 Data

**Source**: Manually constructed from the ClassEval benchmark via line-wise translation

**Size**: 94 tasks

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Holistic translation
- Min-dependency translation
- Standalone translation

**Metrics**:
- Compilation Success Rate (CSR)
- Computational Accuracy (CA)

**Calculation**: CSR is the ratio of successfully compiled code samples; CA is the ratio of translated programs producing the same execution result as the ground truths.

**Interpretation**: Higher CSR and CA values indicate better performance in code translation tasks.

**Validation**: Manually reviewed by experts and evaluations are conducted on zero-shot translation settings.

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
