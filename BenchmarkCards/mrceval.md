# MRCEval

## 📊 Benchmark Details

**Name**: MRCEval

**Overview**: MRCEval is a comprehensive, challenging and accessible benchmark designed to assess the reading comprehension capabilities of Large Language Models (LLMs) using 2,103 high-quality multi-choice questions across 13 distinct RC skills.

**Data Type**: multi-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- DocRED
- FAITH-EVAL
- COSMOSQA
- PubMedQA
- DROP
- MoreHopQA

**Resources**:
- [GitHub Repository](https://github.com/THU-KEG/MRCEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for assessing the reading comprehension capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Reading Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark is constructed using existing MRC datasets like SQuAD, DocRED, and others.

**Size**: 2,103 multi-choice instances

**Format**: multi-choice

**Annotation**: Automatically generated using LLMs and manually filtered for quality.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is reported as the metric from a single run result of models evaluated on the benchmark.

**Interpretation**: Higher accuracy indicates better performance of large language models on reading comprehension tasks.

**Baseline Results**: N/A

**Validation**: Quality detection filtering was performed on the origin data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes measures for sensitive information filtering.

**Data Licensing**: MRCEval will be shared under the CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
