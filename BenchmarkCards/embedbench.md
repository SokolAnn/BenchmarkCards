# EmbedBench

## 📊 Benchmark Details

**Name**: EmbedBench

**Overview**: EmbedBench is a benchmark designed to evaluate the capabilities of LLMs on embedded system programming, circuit design, and cross-platform migration tasks, consisting of 126 cases covering 9 electronic components across 3 hardware platforms.

**Data Type**: programming tasks with circuit schematics and code generation

**Domains**:
- Computer Engineering
- Embedded Systems

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- SWE-bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of EmbedBench is to assess the capabilities of large language models in performing embedded system design tasks, including programming, circuit design, and code migration.

**Target Audience**:
- ML Researchers
- Embedded Systems Engineers

**Tasks**:
- Embedded System Programming
- Circuit Design
- Cross-Platform Migration

**Limitations**: N/A

## 💾 Data

**Source**: Constructed manually for the purpose of benchmarking LLMs on embedded systems tasks.

**Size**: 126 cases

**Format**: JSON

**Annotation**: Cases are validated by independent annotators and reviewed for quality control.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- pass@1

**Calculation**: The pass@1 score indicates the percentage of tasks for which the generated code passes all specified test cases.

**Interpretation**: A higher pass@1 score signifies better model performance in accurately generating functional embedded system outcomes based on the provided tasks.

**Validation**: Validation is performed through an automated evaluation pipeline using the Wokwi simulation platform.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
