# Flow2Code

## 📊 Benchmark Details

**Name**: Flow2Code

**Overview**: Flow2Code is a benchmark for flowchart-based code generation evaluation, spanning 15 programming languages and including 5,622 code segments paired with 16,866 flowcharts of code, UML, and pseudocode types.

**Data Type**: code-flowchart pairs

**Domains**:
- Computer Science

**Languages**:
- Python
- Java
- C
- C++
- JavaScript
- PHP
- Ruby
- C#
- Fortran
- Shell
- Pascal
- Perl
- HTML
- Tcl
- Visual Basic

**Similar Benchmarks**:
- HumanEval
- MBPP
- CodeContests
- MCEVAL

**Resources**:
- [GitHub Repository](https://github.com/hml-github/Flow2Code)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized platform for assessing flowchart-based code generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from four key datasets: HumanEval-X, MBXP, MCEval, and ClassEval.

**Size**: 5,622 code segments and 16,866 flowcharts

**Format**: N/A

**Annotation**: Two-step human evaluation for verification and validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Execution-based evaluation

**Metrics**:
- Pass@1
- Pass@3
- Pass@5

**Calculation**: Tasks are successful if any of the top k samples are correct.

**Interpretation**: Higher Pass@k indicates better code generation performance from flowcharts.

**Baseline Results**: Evaluation conducted on 13 multimodal LLMs.

**Validation**: Data was verified through a two-step human evaluation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured compliance with the terms of use of original datasets, protecting intellectual property rights.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
