# DebugBench

## 📊 Benchmark Details

**Name**: DebugBench

**Overview**: DebugBench is a new LLM debugging benchmark consisting of 4,253 instances to evaluate the debugging capabilities of large language models across various bug categories and types.

**Data Type**: code snippets with embedded bugs

**Domains**:
- Software Engineering

**Languages**:
- Python
- C++
- Java

**Similar Benchmarks**:
- QuixBugs
- Defects4J

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/DebugBench)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate the debugging capabilities of large language models.

**Target Audience**:
- Researchers
- Practitioners
- Developers

**Tasks**:
- Debugging

**Limitations**: The benchmark's reliance on synthetic bugs may limit its applicability to real-world scenarios.

## 💾 Data

**Source**: Collected from LeetCode and synthesized with GPT-4.

**Size**: 4,253 instances

**Format**: JSON

**Annotation**: Implemented using GPT-4 to create bugs and explanations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass Rate

**Calculation**: Pass Rate is calculated as the ratio of successfully fixed bug instances to total bug instances.

**Interpretation**: A higher Pass Rate indicates better debugging capability of the model.

**Validation**: Evaluations were performed on various models in zero-shot scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache-2.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
