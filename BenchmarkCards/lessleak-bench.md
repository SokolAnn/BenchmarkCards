# LessLeak-Bench

## 📊 Benchmark Details

**Name**: LessLeak-Bench

**Overview**: LessLeak-Bench is a new benchmark that provides cleaned versions of 83 studied SE benchmarks with all identified leaked samples removed, enabling more reliable LLM evaluations in future research.

**Data Type**: tabular

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- C/C++

**Resources**:
- [Resource](https://huggingface.co/bigcode/lessleak-bench)

## 🎯 Purpose and Intended Users

**Goal**: To enable more reliable evaluations of LLMs in future research by addressing data leakage in SE benchmarks.

**Target Audience**:
- ML Researchers
- Software Engineers

**Tasks**:
- Code Generation
- Program Repair
- Code Editing
- Code Translation
- Code Review
- Debugging
- Vulnerability Detection

**Limitations**: N/A

## 💾 Data

**Source**: Identification and removal of leaked samples from 83 SE benchmarks.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual labeling of duplicate pairs to confirm leaked data.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Leakage Count
- Leakage Ratio

**Calculation**: Leakage Ratio is calculated as the number of leaked samples over the total number of samples in the benchmark.

**Interpretation**: Higher leakage ratios indicate greater risks to evaluation validity due to potential prior exposure of LLMs to benchmark data.

**Baseline Results**: Average leakage ratios found were 4.8% for Python, 2.8% for Java, and 0.7% for C/C++.

**Validation**: Manual verification of flagged duplicate pairs identified by the automated tool.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
