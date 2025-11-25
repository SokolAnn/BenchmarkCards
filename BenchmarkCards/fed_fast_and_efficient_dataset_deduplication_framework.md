# FED (Fast and Efficient Dataset Deduplication Framework)

## 📊 Benchmark Details

**Name**: FED (Fast and Efficient Dataset Deduplication Framework)

**Overview**: FED is a GPU-accelerated deduplication framework optimized for MinHash LSH, significantly enhancing data quality and training performance of large language models by efficiently removing duplicate entries in large datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mcrl/FED)

## 🎯 Purpose and Intended Users

**Goal**: To provide an efficient and scalable solution for dataset deduplication that enhances data quality for training large language models.

**Target Audience**:
- ML Researchers
- Data Scientists
- AI Practitioners

**Tasks**:
- Dataset Deduplication

**Limitations**: N/A

## 💾 Data

**Source**: Generated from large-scale document datasets, including RealNews and C4.

**Size**: 1.2 trillion tokens

**Format**: JSONL

**Annotation**: Identifying and removing duplicate entries based on Jaccard similarity thresholds.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Jaccard Similarity

**Calculation**: Calculated using pairwise comparisons of document signatures based on Jaccard similarity.

**Interpretation**: A higher Jaccard similarity score indicates better performance in identifying and removing duplicates.

**Baseline Results**: Comparison against CPU and GPU baseline methods shows significant speedup and accuracy in deduplication.

**Validation**: Evaluated using large-scale experiments on benchmark datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
