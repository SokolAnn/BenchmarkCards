# PerfCurator

## 📊 Benchmark Details

**Name**: PerfCurator

**Overview**: PerfCurator is a repository mining tool designed to identify performance-related bug-fix commits at scale. It employs the PcBERT-KD model to classify commits, producing a large-scale dataset of performance-related bug-fixes across multiple programming languages.

**Data Type**: commit messages

**Domains**:
- Software Engineering

**Languages**:
- Python
- C++
- Java

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale curated dataset of performance-related commits, aiding in the development of better performance bug detection tools.

**Target Audience**:
- Software Engineers
- Researchers in Software Performance

**Tasks**:
- Performance Bug Detection

**Limitations**: N/A

## 💾 Data

**Source**: GitHub repositories

**Size**: 408,500 commits

**Format**: N/A

**Annotation**: Annotated using heuristic supervision and knowledge distillation

## 🔬 Methodology

**Methods**:
- Commit classification using PcBERT-KD
- Repository mining

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated based on precision and recall of performance commits.

**Interpretation**: Higher F1 Scores indicate better performance in identifying performance-related commits.

**Baseline Results**: Keyword-filtering baseline achieved an F1 Score of 0.59.

**Validation**: Validated through manual review of a statistically significant sample of commits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
