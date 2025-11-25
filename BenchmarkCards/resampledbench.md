# ResampledBench

## 📊 Benchmark Details

**Name**: ResampledBench

**Overview**: ResampledBench is constructed using farthest point sampling (FPS) to yield efficient evaluations of vision-language models (VLMs) with a strong correlation (> 0.96) to full benchmark assessments, while using only 1% of the original data.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enable efficient and comprehensive evaluation of large vision-language models by constructing a representative benchmark from existing datasets.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering
- Multiple Choice Question Answering

**Limitations**: Increased sample sizes can degrade the correlation between benchmark evaluations due to distortions in the feature space.

## 💾 Data

**Source**: Constructed using FPS from existing multiple choice question benchmarks and visual question answering benchmarks.

**Size**: 1,000 samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Benchmark classification
- Statistical correlation analysis

**Metrics**:
- Spearman's rank correlation coefficient

**Calculation**: Average ranks of models calculated based on their performance across all benchmarks.

**Interpretation**: Higher correlations indicate better performance rankings alignment with comprehensive evaluations.

**Validation**: The performance of ResampledBench was validated by comparing its correlation with full benchmark results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Unintended biases in benchmark scoring']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
