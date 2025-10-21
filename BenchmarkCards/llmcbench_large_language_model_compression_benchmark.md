# LLMCBench (Large Language Model Compression Benchmark)

## 📊 Benchmark Details

**Name**: LLMCBench (Large Language Model Compression Benchmark)

**Overview**: LLMCBench is the first benchmark to provide a comprehensive evaluation on current LLM compression algorithms, designed to systematically compare and analyze methods in practical scenarios.

**Data Type**: evaluation metrics

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AboveParadise/LLMCBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLM compression algorithms and provide insights for practical usage.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Model Compression Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Multiple datasets including MMLU, HellaSwag, PIQA, WinoGrande, QNLI, MNLI, WikiText2.

**Size**: 11 datasets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Comparison of compression techniques
- Evaluation across multiple datasets
- Performance metrics calculation

**Metrics**:
- Overall Metric (OM) for compression performance
- Generalization Ability
- Training Consumption
- Inference Consumption
- Hardware Acceleration
- Trustworthiness

**Calculation**: Overall Metric calculated as the mean accuracy over all models and datasets using quadratic mean.

**Interpretation**: Higher metric scores indicate better performance and efficiency of compression algorithms.

**Baseline Results**: None stated.

**Validation**: Extensive experiments conducted using established datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Trustworthiness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The assets are open-sourced.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
