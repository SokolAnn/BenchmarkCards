# MatTools

## 📊 Benchmark Details

**Name**: MatTools

**Overview**: MatTools is a benchmark designed to evaluate the proficiency of large language models (LLMs) in answering materials science questions and generating functional Python code for materials property calculations.

**Data Type**: question-answer pairs and Python code generation tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MaScQA
- SciEval
- SciAssess
- LLM4Mat-Bench

**Resources**:
- [GitHub Repository](https://github.com/Grenzlinie/MatTools)
- [Resource](https://www.kaggle.com/datasets/calvinlyu/mattools/data)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized framework for assessing and improving LLM capabilities for materials science tool applications.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Derive from pymatgen codebase and documentation; include generated examples and real-world tool usage datasets.

**Size**: 69,225 QA pairs and 49 tasks (138 subtasks)

**Format**: JSON

**Annotation**: Generated through automated synthesis and LLM interactions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Task Success Rate

**Calculation**: Metrics are calculated based on the proportion of correct responses and executable code rate.

**Interpretation**: Higher metrics indicate better performance and understanding of materials science tools by LLMs.

**Baseline Results**: General-purpose LLMs outperform domain-specific models by achieving accuracies above 80%.

**Validation**: Results validated through multiple evaluation runs and usage of Docker sandbox for code execution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
