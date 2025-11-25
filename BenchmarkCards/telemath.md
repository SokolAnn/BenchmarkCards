# TeleMath

## 📊 Benchmark Details

**Name**: TeleMath

**Overview**: TeleMath is the first benchmark dataset specifically designed to evaluate LLM performance in solving mathematical problems with numerical solutions in the telecommunications domain. Comprising 500 question-answer (QnA) pairs, it covers a wide spectrum of topics within telecommunications.

**Data Type**: question-answer pairs

**Domains**:
- Telecommunications Engineering
- Electrical Engineering
- Probability and Statistics
- Signal Processing
- Computer Networking
- Operations Research
- Information Theory

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8K

**Resources**:
- [Resource](https://huggingface.co/datasets/netop/TeleMath)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for evaluating Large Language Models on domain-specific mathematical problems in telecommunications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Mathematical Problem Solving

**Limitations**: The seed dataset does not fully represent the entire telecommunications domain.

## 💾 Data

**Source**: Generated from a seed dataset composed of problems designed by Subject Matter Experts.

**Size**: 500 question-answer pairs

**Format**: JSON

**Annotation**: Manual annotations by Subject Matter Experts.

## 🔬 Methodology

**Methods**:
- Synthetic data generation
- Benchmarking

**Metrics**:
- pass@1
- cons@16

**Calculation**: Metrics are calculated over generated answers based on majority voting and single-attempt accuracy.

**Interpretation**: A higher pass@1 indicates that a model correctly generates the answer on its first attempt, while cons@16 reflects the consensus correctness across multiple attempts.

**Validation**: Semantic validation ensures questions are structurally equivalent to the original problems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
