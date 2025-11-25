# FullStack Bench

## 📊 Benchmark Details

**Name**: FullStack Bench

**Overview**: FullStack Bench is a comprehensive code evaluation dataset that spans multiple computer science domains and programming languages, containing 3374 problems. It is designed to assess large language models' capabilities in real-world code development scenarios.

**Data Type**: programming problems with unit test cases

**Domains**:
- Natural Language Processing
- Software Engineering
- Data Analysis
- Machine Learning
- Computer Science

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- HumanEval
- MBPP
- DS-1000
- xCodeEval

**Resources**:
- [Resource](https://huggingface.co/datasets/ByteDance/FullStackBench)
- [GitHub Repository](https://github.com/bytedance/FullStackBench)
- [GitHub Repository](https://github.com/bytedance/SandboxFusion)

## 🎯 Purpose and Intended Users

**Goal**: To provide a holistic evaluation framework for code intelligence and to assess the multilingual programming capabilities of large language models in real-world scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Code Evaluation
- Code Debugging

**Limitations**: N/A

## 💾 Data

**Source**: Collected from real-world programming challenges and code-related documents, specifically curated for diverse application domains.

**Size**: 3374 problems

**Format**: N/A

**Annotation**: Systematic human annotation process for producing code samples across different application domains.

## 🔬 Methodology

**Methods**:
- Automated evaluation using unit tests
- Human evaluation for data accuracy
- Benchmarking against existing models

**Metrics**:
- Pass@1

**Calculation**: Evaluation metrics calculated based on the percentage of unit tests passed by the generated solutions.

**Interpretation**: Higher Pass@1 metrics indicate better performance of language models on the benchmark.

**Baseline Results**: N/A

**Validation**: Comprehensive experimental results validate the effectiveness of FullStack Bench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
