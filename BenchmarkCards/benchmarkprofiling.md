# BENCHMARKPROFILING

## 📊 Benchmark Details

**Name**: BENCHMARKPROFILING

**Overview**: BENCHMARKPROFILING is a diagnostic framework designed to systematically profile benchmark performance into ten cognitively grounded abilities, quantifying their contributions to a model's success on evaluation benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- HellaSwag
- TruthfulQA
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/junkim100/Benchmark-Profiling)

## 🎯 Purpose and Intended Users

**Goal**: To provide a transparent method for diagnosing benchmark capabilities and aligning model evaluations with human-aligned competencies.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic datasets for ten operationalized abilities created through targeted prompts and validation by domain experts.

**Size**: 20,000 examples

**Format**: JSON

**Annotation**: Guided by few-shot examples and validated through expert assessments.

## 🔬 Methodology

**Methods**:
- Gradient-based importance scoring
- Targeted parameter ablation

**Metrics**:
- Ability Impact Score (AIS)

**Calculation**: AIS is calculated as the normalized performance drop relative to the baseline improvement over chance, highlighting the dependence of benchmarks on specific abilities.

**Interpretation**: An AIS value near 1 indicates strong dependence on the ability, while values near 0 suggest little reliance.

**Baseline Results**: N/A

**Validation**: Validated through expert evaluations and performance assessments across models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All diagnostic items are synthetically generated and contain no personal or identifying details.

**Data Licensing**: MIT License for research and non-commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
