# SOPBench (Standard Operating Procedures Benchmark)

## 📊 Benchmark Details

**Name**: SOPBench (Standard Operating Procedures Benchmark)

**Overview**: SOPBench is a benchmark developed for evaluating language agents' adherence to domain-specific standard operating procedures (SOPs) across customer service domains. It features an automated evaluation pipeline with executable environments, tool functions, and verified test cases to assess the procedural compliance of language agents.

**Data Type**: test cases

**Domains**:
- Bank
- DMV
- Healthcare
- Library
- Online Market
- University
- Hotel

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Leezekun/SOPBench)
- [Resource](https://huggingface.co/datasets/Zekunli/SOPBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the compliance of language agents with standard operating procedures in real customer service environments.

**Target Audience**:
- ML Researchers
- Language Model Developers
- Industry Practitioners

**Tasks**:
- Text Classification
- Task Completion

**Limitations**: SOPBench is limited to evaluating language agents' compliance with procedural requirements and does not encompass other types of procedural workflows.

## 💾 Data

**Source**: Generated test cases based on domain-specific SOPs and constraints.

**Size**: 903 test cases

**Format**: JSON

**Annotation**: Test cases are auto-validated using executable code implementations that act as rule-based verifiers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Tool-based evaluation

**Metrics**:
- Accuracy
- Correctness of final states
- Compliance with action graphs

**Calculation**: Metrics are calculated by comparing agent outputs to expected outcomes based on procedural requirements and constraints coded as executable functions.

**Interpretation**: High accuracy and compliance indicate an agent's proficiency in following SOPs, while discrepancies suggest potential improvements in model training or architecture.

**Validation**: Test cases are systematically generated and validated against predefined constraints.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Potential Harm**: ['Misuse for probing weaknesses in language agents']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under CC BY 4.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
