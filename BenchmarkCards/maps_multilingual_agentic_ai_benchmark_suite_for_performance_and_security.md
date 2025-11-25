# MAPS (Multilingual Agentic AI Benchmark Suite for Performance and Security)

## 📊 Benchmark Details

**Name**: MAPS (Multilingual Agentic AI Benchmark Suite for Performance and Security)

**Overview**: MAPS introduces the first multilingual benchmark suite designed to evaluate agentic AI systems across diverse languages and tasks, addressing critical gaps in assessing language-specific performance and safety limitations.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- Spanish
- Portuguese
- Japanese
- Russian
- Italian
- Arabic
- Hebrew
- Korean
- Chinese
- Hindi

**Similar Benchmarks**:
- GAIA
- SWE-bench
- MATH
- Agent Security Benchmark

**Resources**:
- [Resource](https://huggingface.co/datasets/Fujitsu-FRE/MAPS)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of agentic AI systems in multilingual settings and to identify performance and security gaps across different languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Mathematical Reasoning
- Real-World Task Completion
- Security Assessment

**Limitations**: Current suite includes four datasets and eleven target languages, but extending to additional domains and extremely low-resource languages would enhance the benchmark.

## 💾 Data

**Source**: The benchmark is constructed by translating established English benchmarks (GAIA, SWE-bench, MATH, Agent Security Benchmark) into multiple languages.

**Size**: 9,660 total language-specific instances

**Format**: N/A

**Annotation**: Hybrid machine and LLM-based translation with expert verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Attack success rate

**Calculation**: Metrics are calculated as defined in the original benchmarks for each task type.

**Interpretation**: Success is determined based on correct outputs or responses matching reference outputs.

**Baseline Results**: Performance metrics are compared against the English baseline across all languages.

**Validation**: Validation through human expert review and automated evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Performance
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Analysis emphasizes the uneven performance of agentic systems in non-English languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License, allowing unrestricted use, modification, and distribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
