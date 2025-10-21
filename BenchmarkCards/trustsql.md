# TrustSQL

## 📊 Benchmark Details

**Name**: TrustSQL

**Overview**: TrustSQL is a new benchmark designed to assess text-to-SQL reliability, defined as models’ ability to correctly handle any type of input question by generating correct SQL queries for feasible questions and abstaining from infeasible ones.

**Data Type**: question-SQL pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ATIS
- Advising
- EHRSQL
- Spider

**Resources**:
- [GitHub Repository](https://github.com/glee4810/TrustSQL)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TrustSQL is to evaluate text-to-SQL reliability by integrating both feasible and infeasible questions.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text-to-SQL

**Limitations**: The benchmark does not encompass all possible infeasible questions that may be encountered in real-world scenarios.

## 💾 Data

**Source**: TrustSQL was constructed using domain-specific datasets (ATIS, Advising, EHRSQL) and one cross-domain dataset (Spider).

**Size**: 21,400 examples

**Format**: N/A

**Annotation**: Annotated by the authors based on existing databases.

## 🔬 Methodology

**Methods**:
- Pipeline-based methods
- Unified methods

**Metrics**:
- Reliability Score (RS)

**Calculation**: The reliability is quantified as the difference between utility (correct SQL generations and correct abstentions) and risk (incorrect SQL generations).

**Interpretation**: A reliability score (RS) of 100% indicates perfect reliability, and RS > 0 means the utility is greater than the risk.

**Validation**: Models evaluated under different penalty scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
