# AntiLeakBench

## 📊 Benchmark Details

**Name**: AntiLeakBench

**Overview**: AntiLeakBench is an automated anti-leakage benchmarking framework designed to prevent data contamination in evaluations of large language models by constructing test samples with updated real-world knowledge that is absent from LLMs' training sets.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GSM8K
- BIG-bench
- LiveBench

**Resources**:
- [GitHub Repository](https://github.com/bobxwu/AntiLeakBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable and practical benchmarking framework for contamination-free evaluation of large language models.

**Target Audience**:
- ML Researchers
- Benchmark Developers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata and Wikipedia

**Size**: 10,000 samples

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the precision of answers and context provided against established ground truth.

**Interpretation**: Higher scores indicate better model performance in understanding and processing question-answering tasks.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
