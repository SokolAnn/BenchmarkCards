# JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models

**Overview**: JailBench is the first comprehensive Chinese benchmark for evaluating deep-seated vulnerabilities in large language models (LLMs), featuring a refined hierarchical safety taxonomy tailored to the Chinese context.

**Data Type**: jailbreak-enhanced query pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- SafetyBench
- Flames

**Resources**:
- [GitHub Repository](https://github.com/STAIR-BUPT/JailBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive assessment of safety vulnerabilities in large language models within the Chinese linguistic context.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available datasets and ChatGPT for automatic generation.

**Size**: 10,800 queries

**Format**: N/A

**Annotation**: Manual correction and categorization by experts with random sampling and verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: ASR is calculated as the ratio of test queries that successfully induce harmful outputs to the total queries.

**Interpretation**: A higher ASR indicates a greater effectiveness of the benchmark in identifying vulnerabilities in LLMs.

**Baseline Results**: Compared against existing Chinese benchmarks, JailBench achieves the highest ASR of 73.86% against ChatGPT.

**Validation**: Extensive evaluations conducted on 13 mainstream LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Security

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
