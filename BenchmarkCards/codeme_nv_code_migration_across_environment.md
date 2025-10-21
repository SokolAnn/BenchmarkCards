# CODEME NV (Code Migration Across Environment)

## 📊 Benchmark Details

**Name**: CODEME NV (Code Migration Across Environment)

**Overview**: A benchmark designed to assess LLMs’ abilities in code migration scenarios, encompassing 922 examples spanning 19 Python and Java packages, structured around three tasks: identifying version-incompatible functions, detecting changes in function definitions, and adapting code to target environments.

**Data Type**: code migration examples

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java

**Resources**:
- [GitHub Repository](https://github.com/xdshen-ai/Benchmark-of-Code-Migration)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess the code migration capabilities of LLMs across different environments.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Identifying Version-Incompatible Functions
- Answering Function Changes
- Code Migration

**Limitations**: CODEME NV is relatively small, particularly the Java dataset.

## 💾 Data

**Source**: Official documentation and release notes of Python and Java packages containing function changes.

**Size**: 922 examples

**Format**: N/A

**Annotation**: Manually curated from official sources.

## 🔬 Methodology

**Methods**:
- Agent-based Evaluation
- Unit Test-based Evaluation

**Metrics**:
- Pass@1
- Pass@5
- Accuracy

**Calculation**: Metrics are calculated based on the ability of LLMs to accurately identify incompatible functions and migration correctness.

**Interpretation**: Higher scores indicate better LLM performance in locating incompatible functions and performing successful migrations.

**Baseline Results**: Average accuracy across seven models shows a pass@1 rate of 26.50%, with GPT-4 O achieving a highest score of 43.84%.

**Validation**: Experimental evaluation with nine different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
