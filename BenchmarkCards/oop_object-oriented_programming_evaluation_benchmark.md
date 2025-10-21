# OOP (Object-Oriented Programming) Evaluation Benchmark

## 📊 Benchmark Details

**Name**: OOP (Object-Oriented Programming) Evaluation Benchmark

**Overview**: This paper introduces a pioneering OOP-focused benchmark featuring 431 Python programs that encompass essential OOP concepts such as classes and encapsulation methods, and proposes a novel evaluation metric pass@o tailored for OOP, which enhances traditional metrics.

**Data Type**: Python code examples

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP

**Resources**:
- [GitHub Repository](https://github.com/alphadl/OOP-eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in generating object-oriented programming code.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: Our proposed OOP benchmark is based on the Python programming language and does not cover other OOP languages.

## 💾 Data

**Source**: Collected from platforms like LeetCode, GitHub, Stack Overflow, and Codewars.

**Size**: 431 programs

**Format**: N/A

**Annotation**: Manual rewriting of problems or requirements to include OOP concepts.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- pass@k
- pass@o

**Calculation**: pass@o is calculated by matching keyword points in natural language with programming language constructs.

**Interpretation**: Higher pass@o scores indicate better performance at generating OOP concepts.

**Baseline Results**: N/A

**Validation**: Evaluation conducted on 23 leading large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misinterpretation of OOP tasks by models']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
