# CodableLLM (COdeDAtaset BuiLdEr for LLM s)

## 📊 Benchmark Details

**Name**: CodableLLM (COdeDAtaset BuiLdEr for LLM s)

**Overview**: CodableLLM is an open-source framework designed to automate the creation and curation of datasets by mapping decompiled functions to their corresponding source functions, enhancing the alignment between decompiled and source code representations for training code-focused large language models (LLMs).

**Data Type**: source and decompiled function pairs

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- C
- C++
- Java
- Python
- JavaScript
- TypeScript
- Rust

**Resources**:
- [GitHub Repository](https://github.com/dmanuel64/codablellm/)
- [Resource](https://pypi.org/project/codablellm/)
- [Resource](https://codablellm.readthedocs.io/en/latest/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide an automated, extensible framework for generating datasets that map decompiled binaries to source code functions, facilitating research and training of code-focused LLMs.

**Target Audience**:
- Researchers in software engineering
- AI and ML practitioners
- Developers in reverse engineering

**Tasks**:
- Code Understanding
- Code Generation
- Function Recovery

**Limitations**: The framework relies on symbol-based mapping which can pose challenges with stripped binaries; current support depends on Ghidra as the primary decompiler.

## 💾 Data

**Source**: Public datasets used in automated dataset generation and models from real-world repositories.

**Size**: N/A

**Format**: CSV

**Annotation**: Automatically generated through the mapping of decompiled functions to source functions.

## 🔬 Methodology

**Methods**:
- Automated dataset generation
- Function mapping
- Parallel processing

**Metrics**:
- Processing time
- Mapping accuracy

**Calculation**: Performance is assessed by comparing execution times against a naive single-threaded approach.

**Interpretation**: Reduced time indicates improved efficiency and capability of the automated framework.

**Baseline Results**: Comparison with an earlier single-threaded extraction approach demonstrates nearly 10x time improvement in decompilation tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential bias in dataset due to reliance on existing code repositories that may not be diverse.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: BSD 3-Clause License for source code from libhv project.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
