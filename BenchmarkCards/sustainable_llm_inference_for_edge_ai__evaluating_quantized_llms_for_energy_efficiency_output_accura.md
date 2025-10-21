# Sustainable LLM Inference for Edge AI: Evaluating Quantized LLMs for Energy Efficiency, Output Accuracy, and Inference Latency

## 📊 Benchmark Details

**Name**: Sustainable LLM Inference for Edge AI: Evaluating Quantized LLMs for Energy Efficiency, Output Accuracy, and Inference Latency

**Overview**: This paper presents a systematic evaluation of 28 quantized LLMs deployed on edge devices, focusing on their energy efficiency, output accuracy, and inference latency across multiple datasets and task types.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CommonsenseQA
- BIG-Bench Hard
- TruthfulQA
- GSM8K
- HumanEval

**Resources**:
- [GitHub Repository](https://github.com/ejhusom/neurips-edge-llm-challenge-sampled/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of quantized LLMs on edge devices, analyzing energy efficiency and accuracy trade-offs.

**Target Audience**:
- Researchers
- Engineers
- AI Practitioners

**Tasks**:
- Energy Efficiency Assessment
- Inference Latency Measurement
- Output Accuracy Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Datasets used include CommonsenseQA, BIG-Bench Hard, TruthfulQA, GSM8K, and HumanEval, specifically selected for their relevance to evaluating LLM performance on edge devices.

**Size**: 10,000 examples

**Format**: CSV

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Inference Latency
- Energy Consumption

**Calculation**: Energy consumption measured using Joulescope; accuracy calculated as the proportion of correct answers.

**Interpretation**: Higher scores indicate better performance in terms of energy efficiency and accuracy.

**Baseline Results**: N/A

**Validation**: Results validated using systematic sampling from each benchmark dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Energy Efficiency
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
