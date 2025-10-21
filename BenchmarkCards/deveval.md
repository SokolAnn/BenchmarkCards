# DevEval

## 📊 Benchmark Details

**Name**: DevEval

**Overview**: DevEval is a new code generation benchmark that aligns with real-world code repositories. It contains 1,874 testing samples from 117 repositories, covering 10 popular domains, and is designed to facilitate the evaluation of Large Language Models' coding abilities.

**Data Type**: function code samples with requirements and dependencies

**Domains**:
- Software Development

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- CoNaLA
- CoderEval

**Resources**:
- [GitHub Repository](https://github.com/seketeam/DevEval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of DevEval is to evaluate the coding abilities of Large Language Models in the context of repository-level code generation.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Software Developers

**Tasks**:
- Code Generation

**Limitations**: DevEval is a monolingual benchmark and ignores other programming languages.

## 💾 Data

**Source**: Derived from 117 real-world code repositories collected from PyPI.

**Size**: 1,874 samples

**Format**: JSON

**Annotation**: Annotated by 13 developers with natural language descriptions, original code requirements, and reference dependencies.

## 🔬 Methodology

**Methods**:
- Repository-level code generation evaluation

**Metrics**:
- Pass@k
- Recall@k

**Calculation**: Pass@k is calculated based on the number of programs that pass predefined test cases out of the total generated programs.

**Interpretation**: Higher Pass@k and Recall@k values indicate better coding performance of the model.

**Validation**: Evaluated against 8 popular LLMs to determine performance in real-world coding scenarios.

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
