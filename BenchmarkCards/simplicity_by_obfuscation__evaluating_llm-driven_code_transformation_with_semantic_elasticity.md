# Simplicity by Obfuscation: Evaluating LLM-Driven Code Transformation with Semantic Elasticity

## 📊 Benchmark Details

**Name**: Simplicity by Obfuscation: Evaluating LLM-Driven Code Transformation with Semantic Elasticity

**Overview**: This paper presents an empirical study on the ability of LLMs to obfuscate Python source code. It introduces a metric, 'semantic elasticity', to evaluate the quality of obfuscated code while maintaining functional correctness. The study compares the performance of three leading LLMs (Claude-3.5-Sonnet, Gemini-1.5, GPT-4-Turbo) on a dataset of 30 Python functions.

**Data Type**: Python functions

**Domains**:
- Software Engineering

**Languages**:
- Python

**Resources**:
- [Resource](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how modern LLMs can be applied to code obfuscation while preserving functional integrity and to introduce and validate the 'semantic elasticity' metric.

**Target Audience**:
- ML Researchers
- Software Engineers
- Security Practitioners

**Tasks**:
- Code Obfuscation
- Functionality Preservation

**Limitations**: N/A

## 💾 Data

**Source**: 30 Python functions collected from established repositories, including TheAlgorithms/Python, python-patterns, and Problem-Solving with Algorithms and Data Structures.

**Size**: 30 Python functions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Empirical study
- Metrics computation

**Metrics**:
- Pass Rate
- Code Expansion Ratio
- Cyclomatic Complexity Change
- Identifier Entropy Change
- Execution Time Difference
- Semantic Elasticity

**Calculation**: Metrics calculated as described in the paper using statistical analysis and custom implementations.

**Interpretation**: Semantically elastic transformations maintain functionality while integrating substantial structural complexity changes.

**Baseline Results**: N/A

**Validation**: Empirical validation through comparisons across different LLMs and prompt techniques.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
