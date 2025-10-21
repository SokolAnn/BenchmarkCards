# ScenEval

## 📊 Benchmark Details

**Name**: ScenEval

**Overview**: ScenEval is constructed from problems in textbooks, an online tutorial website, and Stack Overflow to evaluate large language models for code generation through scenario-based testing.

**Data Type**: coding tasks with scenario metadata in JSON format

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.48550/arXiv.2406.12635)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for scenario-based evaluation of machine learning models capable of code generation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from textbooks, online learning websites, and Stack Overflow.

**Size**: 12,864 coding tasks

**Format**: JSON

**Annotation**: Extracted manually and automatically with metadata tagging.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass rate
- Cyclomatic Complexity
- Cognitive Complexity

**Calculation**: Measured by the percentage of test cases passed for generated solutions.

**Interpretation**: Pass@1 metric indicates the correctness of a generated solution.

**Baseline Results**: N/A

**Validation**: Test cases validated through Java unit testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
