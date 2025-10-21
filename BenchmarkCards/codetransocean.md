# CodeTransOcean

## 📊 Benchmark Details

**Name**: CodeTransOcean

**Overview**: CodeTransOcean is a large-scale comprehensive multilingual benchmark that supports the largest variety of programming languages for code translation. It consists of three novel multilingual datasets: MultilingualTrans, NicheTrans, and LLMTrans, as well as a cross-framework dataset, DLTrans.

**Data Type**: code translation pairs

**Domains**:
- Computer Science

**Languages**:
- Python
- C
- C++
- C#
- Java
- Go
- PHP
- Visual Basic
- Ada
- COBOL
- Fortran
- Perl
- Erlang
- Swift
- Rust
- Julia
- Scala

**Resources**:
- [GitHub Repository](https://github.com/WeixiangYAN/CodeTransOcean)

## 🎯 Purpose and Intended Users

**Goal**: To advance research on code translation by providing a comprehensive benchmark and datasets that reflect real-world demands in programming language translation.

**Target Audience**:
- ML Researchers
- Software Engineers
- Data Scientists

**Tasks**:
- Code Translation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Rosetta Code and open-source teaching platforms.

**Size**: 270,507 samples

**Format**: N/A

**Annotation**: Manual validation to ensure quality and functionality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution-based evaluation

**Metrics**:
- BLEU
- Exact Match
- Debugging Success Rate@K

**Calculation**: Metrics are calculated based on the executed code's performance and similarity to reference translations.

**Interpretation**: Higher scores indicate better translation quality and functional correctness.

**Validation**: Cross-validation with a focus on ensuring data quality and functional equivalence.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) for MultilingualTrans and NicheTrans; Apache-2.0 for DLTrans.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
