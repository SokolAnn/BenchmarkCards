# Cross-Care

## 📊 Benchmark Details

**Name**: Cross-Care

**Overview**: Cross-Care is the first benchmark framework dedicated to assessing biases and real-world knowledge in language models, specifically focusing on the representation of disease prevalence across diverse demographic groups. It evaluates how demographic biases embedded in pre-training corpora influence outputs of Large Language Models (LLMs).

**Data Type**: demographic-disease association pairs

**Domains**:
- Healthcare

**Languages**:
- English
- Chinese
- French
- Spanish

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [Resource](https://www.crosscare.net)

## 🎯 Purpose and Intended Users

**Goal**: To assess the representation of disease prevalence across demographic subgroups in language models and identify underlying biases in their outputs.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Bias Assessment
- Model Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The Pile dataset and CDC real-world prevalence data.

**Size**: 89 diseases and demographic associations

**Format**: CSV

**Annotation**: Co-occurrence analysis and demographic representation calculated from public health datasets.

## 🔬 Methodology

**Methods**:
- Co-occurrence analysis
- Model logits examination

**Metrics**:
- Kendall's tau correlation

**Calculation**: Kendall's tau is calculated to compare ranks of disease prevalence across different demographic groups.

**Interpretation**: Kendall's tau values indicate the strength of correlation between model outputs and real-world prevalence data.

**Baseline Results**: N/A

**Validation**: Findings validated with multiple language model architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The framework includes analysis across demographic factors as it evaluates the representation of disease prevalence among different subgroups.

**Potential Harm**: This framework aims to identify and potentially mitigate biases in LLM outputs that could impact healthcare decision-making.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
