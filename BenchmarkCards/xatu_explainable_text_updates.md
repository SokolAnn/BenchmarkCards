# XATU (Explainable Text Updates)

## 📊 Benchmark Details

**Name**: XATU (Explainable Text Updates)

**Overview**: XATU is the first benchmark specifically designed for fine-grained instruction-based explainable text editing, which includes fine-grained instructions and gold-standard edit explanations for evaluating the text editing capabilities of large language models (LLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EditEval

**Resources**:
- [GitHub Repository](https://github.com/megagonlabs/xatu)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating instruction-based text editing capabilities and improve the interpretability and effectiveness of text editing systems.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Editing
- Information Update
- Grammar Error Correction
- Style Transfer

**Limitations**: N/A

## 💾 Data

**Source**: Data is collected from various high-quality sources and includes fine-grained instructions and explanations through both LLM-based and human annotations.

**Size**: 1,000 examples

**Format**: N/A

**Annotation**: Combination of LLM-based annotation and manual validation by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- SARI Score

**Calculation**: SARI Score is calculated as the average of F1 scores for add, keep, and delete operations.

**Interpretation**: Higher SARI scores indicate better performance in adhering to the editing instructions.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through inter-annotator agreement achieving a rate of 80.27%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Explainability

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Explainability**: Unexplainable output

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
