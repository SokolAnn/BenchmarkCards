# CoSQA+ (Code Search Question Answering Plus)

## 📊 Benchmark Details

**Name**: CoSQA+ (Code Search Question Answering Plus)

**Overview**: CoSQA+ introduces a new multi-choice code search benchmark that pairs high-quality queries from CoSQA with multiple suitable code snippets, utilizing an automated annotation system with test-driven agents.

**Data Type**: query-code pairs

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- CoSQA

**Resources**:
- [GitHub Repository](https://github.com/DeepSoftwareAnalytics/CoSQA_Plus)

## 🎯 Purpose and Intended Users

**Goal**: To enhance code search evaluation by providing a multi-choice benchmark.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Search

**Limitations**: N/A

## 💾 Data

**Source**: CoSQA and CodeSearchNet

**Size**: 412,080 pairs

**Format**: N/A

**Annotation**: Automated annotation using test-driven agents

## 🔬 Methodology

**Methods**:
- Automated metrics
- Test-driven verification

**Metrics**:
- Normalized Discounted Cumulative Gain at rank 10 (NDCG@10)
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are calculated based on query-code pairs matched against ground truth annotations through empirical testing.

**Interpretation**: Higher NDCG@10 and MRR indicate better performance in retrieving relevant code snippets.

**Baseline Results**: CoSQA+ demonstrated superior quality over CoSQA in benchmarks.

**Validation**: Rigorous validation using 400 randomly selected query-code pairs and test programs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from human participants involved in the study.

**Compliance With Regulations**: The dataset sources are publicly available under permissible licenses.
