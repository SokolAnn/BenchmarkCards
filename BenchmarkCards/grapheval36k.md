# GraphEval36K

## 📊 Benchmark Details

**Name**: GraphEval36K

**Overview**: GraphEval36K is a comprehensive graph dataset designed to evaluate the graph coding and reasoning capabilities of large language models (LLMs). It comprises 40 graph coding problems and 36,900 test cases, categorized into eight primary categories and four sub-categories to ensure thorough evaluation.

**Data Type**: graph coding problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CLRS-30
- BIG-Bench
- ProofWriter
- PrOntoQA
- GraCoRe
- HGB

**Resources**:
- [Resource](https://grapheval36k.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the graph-solving capabilities of LLMs through a collection of structured coding problems.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Graph Reasoning
- Graph Coding

**Limitations**: The dataset includes 40 coding problems and 36,900 graph samples, which is smaller compared to other LLM evaluation datasets.

## 💾 Data

**Source**: Generated using problems sourced from LeetCode and custom problem definitions.

**Size**: 36,900 test cases

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Code execution testing

**Metrics**:
- Passing rates

**Calculation**: The passing rate is calculated based on the correctness of the generated code against the provided test cases.

**Interpretation**: A higher passing rate indicates better performance of the LLM on graph problem-solving tasks.

**Baseline Results**: Various baseline models are benchmarked against the dataset, including GPT-3.5, GPT-4, GPT-4o, and others.

**Validation**: The dataset ensures comprehensive coverage by including multiple categories and difficulty levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
