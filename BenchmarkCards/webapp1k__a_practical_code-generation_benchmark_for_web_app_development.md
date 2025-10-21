# WebApp1K: A Practical Code-Generation Benchmark for Web App Development

## 📊 Benchmark Details

**Name**: WebApp1K: A Practical Code-Generation Benchmark for Web App Development

**Overview**: WebApp1K is a practical code-generation benchmark designed to measure LLM ability to develop web apps. It aims to calibrate LLM output and improve code correctness and functionality.

**Data Type**: code generation problems

**Domains**:
- Software Development

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/onekq-ai/WebApp1K-React)
- [GitHub Repository](https://github.com/onekq/WebApp1k)
- [Resource](https://huggingface.co/spaces/onekq-ai/WebApp1K-models-2024)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark LLM performance in practical application development.

**Target Audience**:
- Practitioners
- Model Developers
- Researchers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Human curated and LLM synthesized user journeys depicting unique user journeys for web applications.

**Size**: 1,000 problems

**Format**: N/A

**Annotation**: Combination of human curation and data synthesis by LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- pass@1
- pass@5
- pass@10

**Calculation**: Calculated as the number of problems solved correctly within a certain number of attempts.

**Interpretation**: Higher pass@k scores indicate better performance in generating correct code for the problems.

**Baseline Results**: N/A

**Validation**: The benchmark is validated through performance results from evaluating various LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
