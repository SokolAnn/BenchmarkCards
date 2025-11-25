# TRACY: Benchmarking Execution Efficiency of LLM-Based Code Translation

## 📊 Benchmark Details

**Name**: TRACY: Benchmarking Execution Efficiency of LLM-Based Code Translation

**Overview**: TRACY is the first comprehensive benchmark designed to evaluate the execution efficiency of LLM-translated code, constructed through an LLM-driven two-stage pipeline that generates a suite of stress tests followed by efficiency-oriented task pruning.

**Data Type**: code translation tasks

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- TransCoder-Test

**Resources**:
- [GitHub Repository](https://github.com/deepseek-ai/TRACY)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a benchmark focused on the execution efficiency of LLM-translated code.

**Target Audience**:
- ML Researchers
- Software Engineers
- Code Developers

**Tasks**:
- Code Translation

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from Transcoder-Test, volume of 2,800 candidate tasks, filtered to 1,011 efficiency-critical translation tasks.

**Size**: 1,011 tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Expert evaluation

**Metrics**:
- Efficiency evaluation
- Correctness checks

**Calculation**: Each LLM-generated translation is validated and scored based on execution time and memory usage against stress tests.

**Interpretation**: A higher Beyond score indicates better efficiency comparison against verified reference translations.

**Baseline Results**: N/A

**Validation**: Validated against execution profiles through extensive evaluation on 26 LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Efficiency
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
