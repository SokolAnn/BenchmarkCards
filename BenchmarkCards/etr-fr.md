# ETR-fr

## 📊 Benchmark Details

**Name**: ETR-fr

**Overview**: ETR-fr is the first dataset specifically designed for Easy-to-Read (ETR) text generation, tailored to users with cognitive disabilities. It consists of 523 aligned text pairs fully compliant with European ETR guidelines.

**Data Type**: aligned text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- French

**Resources**:
- [GitHub Repository](https://github.com/FrLdy/ETR-fr)

## 🎯 Purpose and Intended Users

**Goal**: To enhance accessibility and facilitate understanding for individuals with cognitive impairments through the provision of ETR-compliant texts.

**Target Audience**:
- Researchers
- Practitioners in accessibility
- Developers of AI-driven text simplification tools

**Tasks**:
- Text Simplification
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: ETR book collection published by François Baudez Publishing.

**Size**: 523 text pairs

**Format**: N/A

**Annotation**: Aligned by experts based on European ETR guidelines.

## 🔬 Methodology

**Methods**:
- Parameter-efficient fine-tuning of PLMs and LLMs

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERT Score
- SARI
- Kandel-Moles Readability Estimate (KMRE)

**Calculation**: Metrics are calculated based on the performance of models on the ETR-fr test set.

**Interpretation**: Higher scores in ROUGE metrics indicate better quality in text generation.

**Baseline Results**: N/A

**Validation**: Internal evaluations using automatic metrics and manual assessments according to ETR guidelines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
