# TTS-Uniform (Test-Time Scaling Framework)

## 📊 Benchmark Details

**Name**: TTS-Uniform (Test-Time Scaling Framework)

**Overview**: TTS-Uniform is a framework designed to mitigate the selection bias of reasoning strategies in large language models (LLMs) when applying test-time scaling. It aims to enhance the effectiveness of scaling by uniformly allocating the sampling budget across diverse reasoning strategies.

**Data Type**: N/A

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AQuA
- AIME 2024
- AIME 2025

**Resources**:
- [GitHub Repository](https://github.com/zongqianwu/Uniform-TTS)

## 🎯 Purpose and Intended Users

**Goal**: To propose a framework that can improve the performance of LLMs by addressing strategy-selection bias in chain-of-thought reasoning during test-time scaling.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Mathematical Problem Solving
- Reasoning Tasks

**Limitations**: N/A

## 💾 Data

**Source**: Experimental results validated on reasoning benchmarks with diverse task complexities.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Theoretical Analysis
- Empirical Evaluation
- Ablation Testing

**Metrics**:
- Accuracy
- Pass@k

**Calculation**: Metrics are calculated based on the number of correct responses across sampled paths and the defined metrics from benchmark datasets.

**Interpretation**: Higher accuracy and Pass@k values indicate better performance of the proposed TTS-Uniform framework.

**Baseline Results**: Performance comparisons with baseline methods like Self-Consistency and other test-time scaling methods.

**Validation**: Validation through extensive experiments on multiple reasoning benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
