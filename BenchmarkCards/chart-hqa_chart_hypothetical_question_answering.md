# Chart-HQA (Chart Hypothetical Question Answering)

## 📊 Benchmark Details

**Name**: Chart-HQA (Chart Hypothetical Question Answering)

**Overview**: Chart-HQA is a challenging benchmark for chart hypothetical question answering that requires models to engage in counterfactual reasoning based on chart content.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA

**Resources**:
- [Resource](https://arxiv.org/abs/2503.04095)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the true understanding capabilities of MLLMs on chart-based reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Synthesized from publicly available data sources and modified from ChartQA.

**Size**: 2,173 hypothetical questions

**Format**: JSON

**Annotation**: Generated using a combination of human feedback and automated methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Relaxed accuracy

**Calculation**: Relaxed accuracy is calculated using exact match accuracy with 5% tolerance on numerical error.

**Interpretation**: A higher relaxed accuracy indicates better model performance on hypothetical question answering.

**Baseline Results**: N/A

**Validation**: Zero-shot testing was performed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable or sensitive information is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
