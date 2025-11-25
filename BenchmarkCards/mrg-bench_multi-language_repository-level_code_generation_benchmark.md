# MRG-Bench (Multi-language Repository-level Code Generation Benchmark)

## 📊 Benchmark Details

**Name**: MRG-Bench (Multi-language Repository-level Code Generation Benchmark)

**Overview**: MRG-Bench is a novel dataset designed for evaluating LLMs in practical repository-level code generation tasks, offering multi-language support and project-level runnable test cases to enhance the credibility of evaluation results.

**Data Type**: function-level code generation tasks

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- Go

**Similar Benchmarks**:
- HumanEval
- CoderEval
- APPS
- RepoBench

**Resources**:
- [GitHub Repository](https://github.com/MRG-Bench/MRG-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide an effective evaluation framework for large language models in repository-level code generation tasks.

**Target Audience**:
- ML Researchers
- Software Engineers
- Students

**Tasks**:
- Code Generation

**Limitations**: The dataset primarily covers three languages and may not include all programming paradigms.

## 💾 Data

**Source**: Data is sourced from real-world open-source repositories collected via the GitHub API.

**Size**: 383 samples

**Format**: N/A

**Annotation**: Annotations were manually verified to ensure meaningful descriptions of functionality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass@k

**Calculation**: Pass@n is defined as the proportion of samples with at least one generation result that passes all test cases.

**Interpretation**: Higher Pass@n indicates better performance in generating correct and runnable code.

**Baseline Results**: Claude-3.5-Sonnet achieved an average Pass@1 score of 32.5% on MRG-Bench.

**Validation**: The dataset was validated by ensuring that all projects successfully ran their test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
