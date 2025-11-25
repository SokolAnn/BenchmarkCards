# EffiEval

## 📊 Benchmark Details

**Name**: EffiEval

**Overview**: EffiEval is a training-free approach for efficient benchmarking that addresses data redundancy while maintaining high evaluation reliability, ensuring comprehensive coverage of model capabilities, fairness, and generalizability.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- HELM
- BIG-Bench

**Resources**:
- [Resource](https://castria-cn.github.io/EffiEval-homepage/performance)

## 🎯 Purpose and Intended Users

**Goal**: To provide a practical and generalizable solution for reliable, fair, and efficient evaluation in the era of large language models (LLMs).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Public benchmarks including GSM8K, ARC-Challenge, Hellaswag, MMLU.

**Size**: 14,042 samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Static evaluation

**Metrics**:
- Kendall's τ
- Spearman's r

**Calculation**: Metrics calculated by comparing model performances from selected subsets against those from full datasets.

**Interpretation**: Higher correlation coefficients indicate better performance alignment between subset and full dataset.

**Baseline Results**: N/A

**Validation**: Smart subset size adjustment based on coverage requirements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
