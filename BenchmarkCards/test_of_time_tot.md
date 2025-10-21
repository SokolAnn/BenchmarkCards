# Test of Time (ToT)

## 📊 Benchmark Details

**Name**: Test of Time (ToT)

**Overview**: ToT is a benchmark designed to assess LLMs' temporal reasoning abilities through two distinct tasks focused on temporal semantics and arithmetic, enabling a comprehensive evaluation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TGQA (Temporal Graph Question Answering)
- TEMPTABQA (Temporal Question Answering for Semi-Structured Tables)
- TempLama (Temporal Language Model Assessment)

**Resources**:
- [Resource](https://huggingface.co/datasets/baharef/ToT)

## 🎯 Purpose and Intended Users

**Goal**: The objective of ToT is to provide a rigorous and informative assessment of LLMs' temporal reasoning capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Temporal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic dataset generated using controlled graph structures and temporal relationships.

**Size**: 46,480 examples (ToT-Semantic), 2,800 examples (ToT-Arithmetic)

**Format**: text

**Annotation**: Automatically generated and manually curated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model performance across the different question types in the benchmark.

**Interpretation**: Higher accuracy indicates a better understanding of temporal reasoning.

**Baseline Results**: Results evaluated using Claude-3-Sonnet, GPT-4, and Gemini 1.5 Pro.

**Validation**: Extensive experiments conducted to validate model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misuse in generating misleading temporal information.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No sensitive or personal data included.

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
