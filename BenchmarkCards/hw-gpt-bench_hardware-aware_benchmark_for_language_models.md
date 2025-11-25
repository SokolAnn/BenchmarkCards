# HW-GPT-Bench (Hardware-Aware Benchmark for Language Models)

## 📊 Benchmark Details

**Name**: HW-GPT-Bench (Hardware-Aware Benchmark for Language Models)

**Overview**: HW-GPT-Bench is a hardware-aware benchmark that utilizes surrogate predictions to approximate various hardware metrics across GPT-2 architectures, focusing on the optimization of language models under specific hardware constraints.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/automl/HW-GPT-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The objective of the benchmark is to facilitate the evaluation and optimization of neural architecture search methods on language models subject to different hardware constraints and resources.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Neural Architecture Search
- Multi-Objective Optimization

**Limitations**: The benchmark is currently limited to decoder-only models and does not profile architectures on edge devices.

## 💾 Data

**Source**: GPT-2 architectures and surrogate predictions based on performance in various hardware metrics.

**Size**: 10,000 unique architectures sampled from different scales.

**Format**: N/A

**Annotation**: Manual and automated methods used for surrogate performance and hardware metrics estimation.

## 🔬 Methodology

**Methods**:
- Multi-objective Neural Architecture Search
- Surrogate modeling
- Latent variable modeling

**Metrics**:
- Perplexity
- Latency (ms)
- Energy (kWh)
- Memory (GB)
- FLOPS

**Calculation**: The surrogate models provide latencies and energy estimates based on architecture parameters and performance predictions.

**Interpretation**: Lower perplexity indicates better performance of the language model under given constraints.

**Baseline Results**: NSGA-II, MOREA, Random Search, and others tested for performance on Pareto optimal architectures.

**Validation**: Tested across various GPU and CPU platforms with differing hardware metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misuse of optimized architectures for inefficient resource allocation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under Apache 2.0 License, with attribution required.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
