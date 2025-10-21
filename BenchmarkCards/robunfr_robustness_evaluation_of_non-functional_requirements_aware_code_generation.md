# RobuNFR (Robustness Evaluation of Non-Functional Requirements Aware Code Generation)

## 📊 Benchmark Details

**Name**: RobuNFR (Robustness Evaluation of Non-Functional Requirements Aware Code Generation)

**Overview**: RobuNFR is an automated framework that evaluates the robustness of LLMs in code generation while incorporating Non-Functional Requirements (NFRs). It examines four NFR dimensions—design, readability, reliability, and performance—across three methodologies: prompt variation, regression testing, and diverse workflows.

**Data Type**: code generation tasks

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- HumanEval-ET
- MBPP
- MBPP-ET

**Resources**:
- [Resource](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of LLMs in addressing Non-Functional Requirements (NFRs) during code generation.

**Target Audience**:
- Software Developers
- Machine Learning Researchers

**Tasks**:
- Code Generation
- Code Quality Assessment

**Limitations**: N/A

## 💾 Data

**Source**: HumanEval, HumanEval-ET, MBPP, MBPP-ET benchmarks.

**Size**: 164 programming problems (HumanEval), 427 programming problems (MBPP)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Prompt Variation
- Regression Testing
- NFR-Aware Code Generation Workflows

**Metrics**:
- Pass@1
- Code Smell Density
- Readability Density
- Exception Handling Density
- Execution Time

**Calculation**: Metrics are calculated based on passing tests and performance of generated code.

**Interpretation**: Higher Pass@1 indicates better performance in functional correctness; lower code smell density indicates better design.

**Validation**: Tests against existing benchmarks to ensure consistency of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Inconsistencies in LLM outputs could lead to unreliable code generation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
