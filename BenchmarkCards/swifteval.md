# SwiftEval

## 📊 Benchmark Details

**Name**: SwiftEval

**Overview**: SwiftEval is the first Swift-oriented benchmark consisting of 28 carefully hand-crafted problems designed to evaluate LLM coding capabilities specifically for the Swift programming language.

**Data Type**: programming problems

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MultiPL-E
- MBXP

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.14445601)

## 🎯 Purpose and Intended Users

**Goal**: To develop a high-quality evaluation method specifically tailored to the Swift programming language.

**Target Audience**:
- ML Researchers
- Software Engineers

**Tasks**:
- Code Generation

**Limitations**: SwiftEval currently contains 28 problems, which is significantly fewer than other benchmarks like HumanEval or MBPP.

## 💾 Data

**Source**: Manually crafted problems designed by an industry Software Engineer with deep Swift knowledge.

**Size**: 28 problems

**Format**: N/A

**Annotation**: Carefully hand-crafted

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Pass@k

**Calculation**: Pass@k is calculated based on the number of unit tests that the generated code passes.

**Interpretation**: A higher pass@k score indicates better performance in generating correct code for the given problems.

**Baseline Results**: Comparative results reported against the HumanEval benchmark using various Code LLMs.

**Validation**: Evaluation conducted using 44 popular Code LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
