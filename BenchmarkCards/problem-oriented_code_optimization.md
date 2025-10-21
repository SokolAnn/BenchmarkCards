# Problem-Oriented Code Optimization

## 📊 Benchmark Details

**Name**: Problem-Oriented Code Optimization

**Overview**: This benchmark introduces a problem-oriented perspective for code optimization, significantly enhancing the optimization capabilities of large language models (LLMs) by integrating diverse ideas from multiple programmers tackling the same problem.

**Data Type**: code optimization pairs

**Domains**:
- Computer Science
- Software Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/code-optimization-85ED)

## 🎯 Purpose and Intended Users

**Goal**: To improve code optimization performance by utilizing a problem-oriented perspective.

**Target Audience**:
- ML Researchers
- Software Engineers
- Linguistic Model Developers

**Tasks**:
- Code Optimization

**Limitations**: The focus is solely on time efficiency optimization without considering other optimization directions.

## 💾 Data

**Source**: Optimized and unoptimized code pairs derived from programming competition submissions.

**Size**: 77,967 pairs

**Format**: JSON

**Annotation**: Manual verification of optimization pairs for correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Percent Optimized [%OPT]
- Speedup [SPEEDUP]
- Percent Correct [CORRECT]

**Calculation**: Metrics are calculated based on the performance improvements of LLMs on the optimization pairs.

**Interpretation**: Higher optimization ratios and speedups indicate better optimization performance.

**Validation**: Validation procedures involve testing the benchmark using established coding competitions and checking for performance improvements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
