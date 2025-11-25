# BUG (Bias Under Gender)

## 📊 Benchmark Details

**Name**: BUG (Bias Under Gender)

**Overview**: We present BUG, a first publicly available large-scale corpus for gender bias evaluation which consists of diverse, real-world sentences. This dataset enables evaluation of gender bias in various coreference resolution and machine translation models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WinoGender
- WinoBias
- GAP

**Resources**:
- [GitHub Repository](https://github.com/SLAB-NLP/BUG)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate gender bias in machine translation and coreference resolution models using a large-scale dataset of real-world sentences.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Coreference Resolution
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Three diverse domains including Wikipedia, Covid19 research, and PubMed abstracts

**Size**: 108,000 sentences

**Format**: N/A

**Annotation**: Manually verified by human annotators

## 🔬 Methodology

**Methods**:
- Evaluation of models using BUG
- Error analysis

**Metrics**:
- Accuracy
- Population bias (ΔG)
- Historical bias (ΔS)

**Calculation**: Metrics are calculated based on F1 scores for correct gender predictions in machine translation and coreference resolution.

**Interpretation**: Higher ΔG or ΔS values indicate a greater performance bias towards masculine pronouns or stereotypical assignments.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
