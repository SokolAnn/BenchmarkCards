# LongCodeBench (LCB)

## 📊 Benchmark Details

**Name**: LongCodeBench (LCB)

**Overview**: LongCodeBench (LCB) is a benchmark to test coding LLMs in long-context scenarios, evaluating their comprehension and repair capabilities using tasks derived from real-world GitHub issues.

**Data Type**: question-answering pairs and code repair tasks

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- SWE-Bench
- HELMET

**Resources**:
- [Resource](https://huggingface.co/datasets/Steefano/LCB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating long-context language models on realistic coding tasks.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Comprehension
- Bug Fixing

**Limitations**: N/A

## 💾 Data

**Source**: Collected from public GitHub repositories.

**Size**: 1,043 instances

**Format**: N/A

**Annotation**: Curated with human supervision

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on correctness of answers for LongCodeQA and execution results for LongSWE-Bench.

**Interpretation**: Scores indicate how well models comprehend and repair code issues based on a passing rate of unit tests and accuracy of answer selection.

**Validation**: Results validated against established performance standards for coding tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
