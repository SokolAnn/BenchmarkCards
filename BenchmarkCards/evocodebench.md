# EvoCodeBench

## 📊 Benchmark Details

**Name**: EvoCodeBench

**Overview**: EvoCodeBench is designed to evaluate Large Language Models (LLMs) in code generation, addressing limitations such as data leakage and lack of domain-specific evaluations. It includes evolving data updated regularly and domain-specific evaluations to help practitioners select superior LLMs.

**Data Type**: code generation tasks with requirements and code samples

**Domains**:
- Software Development

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- ClassEval
- DevEval

**Resources**:
- [GitHub Repository](https://github.com/seketeam/EvoCodeBench)
- [Resource](https://huggingface.co/datasets/LJ0815/EvoCodeBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of EvoCodeBench is to evaluate LLMs in code generation across different domains, providing insights for practitioners and researchers.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: EvoCodeBench is currently monolingual (Python) and smaller in size compared to some existing benchmarks.

## 💾 Data

**Source**: Collected from high-quality open-source Python repositories through an automatic pipeline.

**Size**: 275 samples

**Format**: JSON

**Annotation**: Automatically generated with human evaluation for quality assurance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass@k
- Recall@k

**Calculation**: Pass@k is calculated based on the number of correct programs out of generated programs that pass test cases; Recall@k measures the recall of reference dependencies in generated programs.

**Interpretation**: Higher Pass@k and Recall@k scores indicate better performance in generating accurate solutions.

**Baseline Results**: For example, the highest Pass@1 of gpt-4 on EvoCodeBench-2403 is 20.74%.

**Validation**: The benchmarks' integrity and performance were validated through extensive experiments with various LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is collected from public open-source repositories; no personal data is included.

**Data Licensing**: EvoCodeBench is available under a CC-4.0 license.

**Consent Procedures**: Only high-quality open-source repositories are used, ensuring compliance with legal standards.

**Compliance With Regulations**: The dataset adheres to open-source licensing guidelines.
