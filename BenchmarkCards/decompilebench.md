# DecompileBench

## 📊 Benchmark Details

**Name**: DecompileBench

**Overview**: DecompileBench is the first comprehensive framework for evaluating decompilers in reverse engineering workflows, integrating real-world function extraction, runtime-aware validation, and automated human-centric assessments using LLM-as-Judge.

**Data Type**: function extraction

**Domains**:
- Computer Security

**Languages**:
- N/A

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/Jennieett/DecompileBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic framework for evaluating decompilers and assist security experts in choosing appropriate tools based on specific requirements.

**Target Audience**:
- Security Analysts
- Research Community

**Tasks**:
- Decompilation Evaluation

**Limitations**: Evaluation is limited to x86-64 architectures; limited human validation with a small sample size.

## 💾 Data

**Source**: Extracted from OSS-Fuzz projects capturing 23,400 real-world functions from 130 programs.

**Size**: 23,400 functions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Recompile Success Rate (RSR)
- Coverage Equivalence Rate (CER)

**Calculation**: Metrics calculated via runtime consistency checks and side effect analysis during program execution.

**Interpretation**: Higher metrics indicate better functionality preservation and understandability in decompilation.

**Baseline Results**: Evaluated against performance of existing industrial-strength decompilers.

**Validation**: Validated by comparing outputs with expert ratings using Cohen's kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
