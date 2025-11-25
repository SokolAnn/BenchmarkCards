# SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability

## 📊 Benchmark Details

**Name**: SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability

**Overview**: SAEBench provides a comprehensive evaluation framework that moves beyond the traditional sparsity-fidelity frontier to capture multiple dimensions of SAE performance, measuring performance across eight diverse metrics, spanning interpretability, feature disentanglement and practical applications like unlearning.

**Data Type**: evaluation metrics

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/adamkarvonen/SAEBench)
- [Resource](http://neuronpedia.org/sae-bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark suite and reveal previously hidden trade-offs in Sparse Autoencoders for interpretability research.

**Target Audience**:
- ML Researchers
- Practitioner Researchers

**Tasks**:
- Feature Disentanglement
- Interpretability Assessment
- Unlearning Capability Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Open-source suite of over 200 SAEs across seven SAE architectures and training algorithms.

**Size**: 200 models

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Loss Recovered
- Automated Interpretability
- Sparse Probing
- Feature Absorption
- Spurious Correlation Removal
- Targeted Probe Perturbation
- Unlearning
- RA VEL

**Calculation**: Metrics are calculated based on model evaluation across different defined tasks, presenting scores for each defined metric.

**Interpretation**: Higher scores on defined metrics indicate better performance in terms of interpretability and feature disentanglement.

**Validation**: Evaluated against a comprehensive said of SAE architectures and models

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
