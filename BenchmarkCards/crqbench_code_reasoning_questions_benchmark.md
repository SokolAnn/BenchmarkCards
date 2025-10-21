# CRQBench (Code Reasoning Questions Benchmark)

## 📊 Benchmark Details

**Name**: CRQBench (Code Reasoning Questions Benchmark)

**Overview**: CRQBench is a benchmark of 100 C++ code reasoning questions and answers derived from contextualized code review comments, specifically designed to evaluate the semantic reasoning ability of models in coding tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a realistic benchmark for evaluating the semantic reasoning ability of language models on code reasoning tasks.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark relies on manually curated answers which may not be verified against formal methods.

## 💾 Data

**Source**: Code review comments in the CodeReviewer dataset

**Size**: 100 examples

**Format**: JSON

**Annotation**: Derived from contextualized code review comments using a cooperative LLM and human validation approach

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-assisted annotation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy is calculated based on the correctness of the responses relative to the provided code context.

**Interpretation**: A correct response is one that is accurate and contextually relevant to the question posed.

**Baseline Results**: GPT-4 performed correctly on 65 out of 100 questions (65% accuracy).

**Validation**: Involving human validation after LLM-generated annotations to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
