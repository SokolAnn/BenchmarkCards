# CDALBench (Cross-Domain Active Learning Benchmark)

## 📊 Benchmark Details

**Name**: CDALBench (Cross-Domain Active Learning Benchmark)

**Overview**: CDALBench is the first active learning benchmark which includes tasks in computer vision, natural language processing, and tabular learning. It features a large number of experimental runs for reliable evaluation and provides datasets in normal and embedded formats.

**Data Type**: multiple datasets (image, text, tabular)

**Domains**:
- Computer Vision
- Natural Language Processing
- Tabular Learning

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/wernerth94/A-Cross-Domain-Benchmark-for-Active-Learning/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust, reproducible framework for evaluating active learning methods across multiple domains and datasets.

**Target Audience**:
- ML Researchers
- Research Institutions
- Active Learning Practitioners

**Tasks**:
- Active Learning Evaluation

**Limitations**: The datasets per domain are still limited and may not fully represent their domains.

## 💾 Data

**Source**: Datasets from computer vision, natural language processing, and tabular datasets including synthetic datasets.

**Size**: 9 datasets (14 including the encoded versions)

**Format**: Normal and Embedded Formats

**Annotation**: Diverse datasets with varying annotations; includes pre-encoded datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Area Under Curve (AUC)

**Calculation**: The quality of an AL method is evaluated using performance at every iteration rather than after budget exhaustion.

**Interpretation**: Results are assessed based on the ranks across datasets to ensure robust comparisons between methods.

**Baseline Results**: Benchmarked against established active learning methods across diverse datasets.

**Validation**: Each experiment is repeated 50 times to ensure consistent results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Public datasets only.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
