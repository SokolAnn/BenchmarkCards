# MigrationBench

## 📊 Benchmark Details

**Name**: MigrationBench

**Overview**: MigrationBench is a comprehensive benchmark for migration from Java 8 to Java 17 and 21, including a full dataset of 5,102 repositories and a selected subset of 300 repositories curated for complexity and difficulty in code migration tasks.

**Data Type**: code migration from Java repositories

**Domains**:
- Software Engineering

**Languages**:
- Java

**Similar Benchmarks**:
- SWE-Bench
- HumanEval

**Resources**:
- [Resource](https://huggingface.co/collections/AmazonScience)
- [GitHub Repository](https://github.com/amazon-science/MigrationBench)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a comprehensive benchmark for evaluating large language models' capabilities in code migration.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Migration

**Limitations**: The benchmark does not enforce test coverage and relies on existing test cases, which may be insufficient for high-quality migration.

## 💾 Data

**Source**: Collected from open-source Java repositories on GitHub filtered by licenses and quality metrics.

**Size**: 5,102 repositories (full), 300 repositories (selected)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated evaluation
- SD-Feedback for code migration

**Metrics**:
- success rate (pass@1)

**Calculation**: Success rates are calculated based on passing requirements outlined for minimal and maximal migration.

**Interpretation**: A higher success rate indicates better performance of models in executing repository-level code migrations.

**Baseline Results**: For minimal migration with Claude-3.5-Sonnet-v2, 62.33% success rate; for maximal migration, 27.33% success rate.

**Validation**: Validated through maven clean verify command and checks for compiled class major versions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**
- **Fairness**
- **Privacy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
