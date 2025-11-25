# TRANS REPO-BENCH

## 📊 Benchmark Details

**Name**: TRANS REPO-BENCH

**Overview**: TRANS REPO-BENCH is a benchmark of high-quality open-source Java repositories and their corresponding C# skeletons, including matching unit tests and build configurations, designed for repository-level code translation and fine-grained quality evaluation.

**Data Type**: code repositories with unit tests

**Domains**:
- Software Engineering

**Languages**:
- Java
- C#

**Similar Benchmarks**:
- RepoTransBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework and benchmark for repository-level code translation, focusing on fine-grained evaluation metrics for assessing translation quality.

**Target Audience**:
- ML Researchers
- Software Developers
- Model Developers

**Tasks**:
- Code Translation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from high-quality open-source GitHub projects with successful testing workflows.

**Size**: 13 tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated evaluation

**Metrics**:
- Build success rate
- Unit test success rate

**Calculation**: Build success rate is the proportion of unit tests that compile successfully; unit test success rate is the proportion of unit tests that pass successfully out of those that compile.

**Interpretation**: Higher rates represent better translation accuracy and success in translating repository components.

**Baseline Results**: Evaluations using state-of-the-art models including GPT-4o and DeepSeek-v3.

**Validation**: The evaluation mechanism runs unit tests on the translated outputs within a structured skeleton to ensure accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
