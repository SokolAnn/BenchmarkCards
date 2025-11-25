# ProLiFIC (Procedural Lawmaking Flow in Italian Chambers)

## 📊 Benchmark Details

**Name**: ProLiFIC (Procedural Lawmaking Flow in Italian Chambers)

**Overview**: ProLiFIC is a comprehensive event log dataset of the Italian lawmaking process from 1987 to 2022, created from unstructured data from the Normattiva portal and structured using large language models (LLMs), aimed at supporting process-oriented analyses in legal process mining.

**Data Type**: event log of legislative actions

**Domains**:
- Legal

**Languages**:
- Italian

**Similar Benchmarks**:
- ILMA

**Resources**:
- [Resource](https://zenodo.org/record/15746419)
- [GitHub Repository](https://github.com/matildeec/ProLiFIC)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured dataset that enhances the understanding and analysis of the Italian lawmaking process.

**Target Audience**:
- Legal Researchers
- Political Scientists
- Public Administration Experts

**Tasks**:
- Process Mining
- Legislative Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Normattiva portal events

**Size**: 43,953 laws

**Format**: structured event log

**Annotation**: Automatically generated using large language models

## 🔬 Methodology

**Methods**:
- Automated metrics
- Process mining techniques

**Metrics**:
- Median duration of legislative processes

**Calculation**: Duration is calculated as the difference in days between the first and last recorded events for each law.

**Interpretation**: Shorter durations indicate efficiency in legislative processes.

**Validation**: Initial analyses performed to examine legislative output and duration

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
