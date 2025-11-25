# pyMethods2Test

## 📊 Benchmark Details

**Name**: pyMethods2Test

**Overview**: The pyMethods2Test dataset provides a large number of open-source unit test methods and their mapping back to their focal methods, focusing on Python code. It is the first dataset to create such mappings for Python, enabling training for large language models (LLMs) in generating tests.

**Data Type**: unit test mappings

**Domains**:
- Software Engineering

**Languages**:
- English
- Python

**Similar Benchmarks**:
- Methods2Test

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.14264518)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large dataset of Python test methods mapped to their focal methods to aid in testing strategies, automatic test generation, and training LLMs.

**Target Audience**:
- Researchers
- Developers
- Educators

**Tasks**:
- Test Generation
- Test Analysis

**Limitations**: The dataset may not accurately map tests in projects following unconventional naming schemes and focuses only on Pytest and unittest frameworks.

## 💾 Data

**Source**: Analyzed 2,661,596 GitHub repositories to generate the dataset.

**Size**: 2,198,378 focal method mappings and over 22M test methods identified.

**Format**: JSON

**Annotation**: Data extracted through automated parsing and analysis of Python source files.

## 🔬 Methodology

**Methods**:
- Automated analysis

**Calculation**: Metrics were not explicitly defined but were generated through extraction and mapping processes.

**Interpretation**: N/A

**Validation**: Based on analysis of test and focal method match criteria.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
