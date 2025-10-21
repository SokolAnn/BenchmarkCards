# SymbolBench

## 📊 Benchmark Details

**Name**: SymbolBench

**Overview**: SymbolBench is a comprehensive benchmark designed to assess symbolic reasoning over real-world time series across three tasks: multivariate symbolic regression, Boolean network inference, and causal discovery.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Biology
- Physics
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- ODEbench
- LLM-SRBench

**Resources**:
- [GitHub Repository](https://github.com/jakobrunge/tigramite?tab=readme-ov-file)
- [Resource](https://arxiv.org/abs/2508.03963)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the symbolic reasoning capabilities of LLMs over time series data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Multivariate Symbolic Regression
- Boolean Network Inference
- Causal Discovery

**Limitations**: N/A

## 💾 Data

**Source**: Real-world time series data curated from various domains including biology, physics, and healthcare.

**Size**: Over 400 samples across three tasks

**Format**: N/A

**Annotation**: Each sample is accompanied by variable descriptions and task-specific ground truths.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score
- Accuracy
- R2 Score
- Conditional Independence score (CI-score)

**Calculation**: Metrics such as F1 Score are calculated using standard formulas based on predicted and true outcomes.

**Interpretation**: Performance is interpreted based on task-specific metrics and benchmarks.

**Baseline Results**: Various standard baseline models including traditional symbolic regression methods.

**Validation**: Each evaluation task is validated through in-distribution and out-of-distribution setups to assess robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
