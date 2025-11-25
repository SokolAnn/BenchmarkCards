# CodeCriticBench

## 📊 Benchmark Details

**Name**: CodeCriticBench

**Overview**: CodeCriticBench is a holistic benchmark for evaluating the code critique capabilities of Large Language Models (LLMs) on two core tasks: code generation and code-based question answering, each incorporating multiple levels of difficulty and advanced evaluation metrics.

**Data Type**: code critique pairs

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- CriticBench
- CriticEval
- JudgeBench
- RealCritic

**Resources**:
- [GitHub Repository](https://github.com/multimodal-art-projection/CodeCriticBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the critique abilities of LLMs on the code domain, providing a comprehensive analysis of their performance in code generation and code QA tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Code Generation
- Code Question Answering

**Limitations**: The evaluation is confined to single-file scenarios and currently focuses only on code.

## 💾 Data

**Source**: Collected from various coding datasets including CodeForces, MBPP, and LiveCodeBench, with modifications for error generation and real-world applicability.

**Size**: 4,300 problems

**Format**: JSON

**Annotation**: Manually annotated by experts and through majority voting for correctness.

## 🔬 Methodology

**Methods**:
- Systematic Analysis of Models
- Fine-Grained Evaluation Metrics

**Metrics**:
- Accuracy
- Mean Squared Error (MSE)

**Calculation**: Metrics are calculated based on predictions matching true labels for the accuracy and measuring the discrepancy for MSE.

**Interpretation**: Higher accuracy and lower MSE scores indicate better performance in model evaluations.

**Validation**: Evaluated against a variety of LLMs using predefined benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Data integrity issues due to the potential for unannounced ethical biases in the benchmarks.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
