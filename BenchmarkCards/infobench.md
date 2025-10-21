# INFOBENCH

## 📊 Benchmark Details

**Name**: INFOBENCH

**Overview**: INFOBENCH is a benchmark comprising 500 diverse instructions and 2,250 decomposed questions designed to evaluate Large Language Models' (LLMs) instruction-following ability using the Decomposed Requirements Following Ratio (DRFR) metric.

**Data Type**: instruction-following tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [GitHub Repository](https://github.com/qinyiwei/InfoBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable benchmark and evaluation framework for assessing the instruction-following capabilities of Large Language Models (LLMs).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following

**Limitations**: The dataset is limited in size, covering only 500 instructions and 2,250 decomposed questions, which may not comprehensively represent all instruction types.

## 💾 Data

**Source**: Created through expert curation and validation for diverse instruction types.

**Size**: 500 instructions and 2,250 questions

**Format**: N/A

**Annotation**: Curated by human experts and validated through a consensus process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Decomposed Requirements Following Ratio (DRFR)
- Agreement among human annotators

**Calculation**: DRFR is calculated as the ratio of met requirements to total requirements within the dataset.

**Interpretation**: A higher DRFR indicates better performance in following detailed instructions.

**Baseline Results**: N/A

**Validation**: The framework was validated by comparing DRFR against traditional scoring methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
