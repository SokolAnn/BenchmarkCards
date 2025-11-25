# SecBench (Security Benchmark)

## 📊 Benchmark Details

**Name**: SecBench (Security Benchmark)

**Overview**: SecBench is a multi-dimensional benchmarking dataset specifically designed to evaluate LLMs in the cybersecurity domain. It includes questions in various formats (MCQs and SAQs), at different capability levels (Knowledge Retention and Logical Reasoning), in multiple languages (Chinese and English), and across various sub-domains.

**Data Type**: multiple-choice questions (MCQs) and short-answer questions (SAQs)

**Domains**:
- Cybersecurity

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- MMLU
- C-Eval
- HumanEval

**Resources**:
- [Resource](https://secbench.org/)
- [Resource](https://zenodo.org/records/14575303)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmarking dataset for evaluating LLM capabilities and limitations in the cybersecurity domain.

**Target Audience**:
- Researchers
- Practitioners
- Developers in Cybersecurity

**Tasks**:
- Knowledge Retention Assessment
- Logical Reasoning Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using high-quality data from open sources and a Cybersecurity Question Design Contest.

**Size**: 44,823 MCQs and 3,087 SAQs

**Format**: JSON

**Annotation**: Manual and LLM-based annotation for labeling questions.

## 🔬 Methodology

**Methods**:
- Automated grading using a grading agent based on LLM output
- Human evaluation for annotation and quality control

**Metrics**:
- Accuracy of question answering and grading
- Correctness percentage

**Calculation**: Comparing model outputs with ground truth for grading.

**Interpretation**: Higher models scores indicate better performance against the dataset questions.

**Baseline Results**: N/A

**Validation**: Benchmarking results evaluated on 16 State-of-the-Art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
