# OpenFactCheck

## 📊 Benchmark Details

**Name**: OpenFactCheck

**Overview**: OpenFactCheck is a unified framework for building customized automatic fact-checking systems, benchmarking their accuracy, evaluating LLMs' factuality, and verifying claims in a document.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- FELM-WK
- Factcheck-Bench
- HaluEval
- FactScore-Bio

**Resources**:
- [GitHub Repository](https://github.com/yuxiaw/openfactcheck)

## 🎯 Purpose and Intended Users

**Goal**: To provide a customizable and extensible framework for evaluating the factuality of claims and documents using automatic fact-checking systems.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Factuality Evaluation
- Automatic Fact-Checking

**Limitations**: N/A

## 💾 Data

**Source**: 包含人类注释的 factuality 评估集，使用自动化事实检查系统进行验证。

**Size**: 6,480 examples

**Format**: N/A

**Annotation**: Manual and automated annotation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Exact matching between model responses and gold standard answers to judge factual correctness.

**Interpretation**: Factual accuracy is assessed based on the correctness of claims relative to human-annotated labels.

**Validation**: The framework is validated through extensive experiments comparing different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential spread of misinformation', 'Impact on public discourse']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
