# AutoEval

## 📊 Benchmark Details

**Name**: AutoEval

**Overview**: This paper presents AutoEval, a novel benchmark for scaling Large Language Model (LLM) assessment in formal tasks with clear notions of correctness, such as truth maintenance in translation and logical reasoning. AutoEval is the first benchmarking paradigm that offers several key advantages necessary for scaling objective evaluation of LLMs without human labeling.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- LogiEval
- FOLIO

**Resources**:
- [GitHub Repository](https://github.com/AAIR-lab/autoeval)

## 🎯 Purpose and Intended Users

**Goal**: Provide a robust framework for evaluating the suitability and safety of LLMs in FL-based tasks such as autoformalization and code generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Logical Reasoning
- Translation

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated datasets through context-free grammars and vocabulary generation.

**Size**: 170,000 examples

**Format**: N/A

**Annotation**: Automatically generated ground truth without human annotation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Formal verification

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance comparison with other benchmarks.

**Interpretation**: Higher scores signify better performance in maintaining truth across translations.

**Validation**: Empirical analysis shows AutoEval's performance is indicative of other benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: plagiarism

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
