# SILENCER

## 📊 Benchmark Details

**Name**: SILENCER

**Overview**: SILENCER is a framework that neutralizes self-bias in LLM-as-Benchmark-Generator methods, allowing for the construction of high-quality benchmarks for evaluation through bias suppression techniques.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- MMLU-Pro
- HellaSwag

**Resources**:
- [Resource](https://arxiv.org/abs/2505.20738)

## 🎯 Purpose and Intended Users

**Goal**: To mitigate self-bias in LLM-generated benchmarks and enhance evaluation accuracy.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Benchmark Generation

**Limitations**: SILENCER incurs approximately 30% additional token costs.

## 💾 Data

**Source**: BenchMaker method for benchmark generation, detailed in experiments.

**Size**: Assumed size in experiments is 50 samples per benchmark.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Attribute Integration
- Cross Paraphrase
- Label Calibration
- Bias-Neutralizing Ensemble

**Metrics**:
- Pearson correlation

**Calculation**: Pearson correlation calculated between model performance on generated benchmarks and human-annotated benchmarks.

**Interpretation**: Higher Pearson correlation indicates better performance and evaluation consistency.

**Baseline Results**: Average Pearson correlation improved from 0.655 to 0.833.

**Validation**: Extensive testing across various LLMs and benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Mitigates potential risks of bias in generated benchmarks.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
