# CausalPitfalls

## 📊 Benchmark Details

**Name**: CausalPitfalls

**Overview**: CausalPitfalls is a comprehensive benchmark designed to rigorously evaluate the capability of large language models (LLMs) in overcoming common causal inference pitfalls through structured challenges and grading rubrics. It focuses on the reliability of causal inference rather than merely accuracy.

**Data Type**: question-answering pairs

**Domains**:
- Statistics
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Causalbench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CausalPitfalls is to evaluate the reliability of LLMs in statistical causal inference, specifically their susceptibility to common causal pitfalls.

**Target Audience**:
- ML Researchers
- Statisticians
- Data Scientists

**Tasks**:
- Causal Inference Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Structured causal models based on directed acyclic graphs (DAGs) simulating potential outcomes.

**Size**: 75 evaluation questions with over 500 samples each

**Format**: N/A

**Annotation**: Questions are graded against a hidden grading rubric established for each challenge.

## 🔬 Methodology

**Methods**:
- Direct Prompting
- Code-Assisted Prompting

**Metrics**:
- Causal Reliability

**Calculation**: Causal reliability is computed as the average normalized score across all benchmark challenges.

**Interpretation**: Higher scores indicate better performance in overcoming causal inference pitfalls.

**Baseline Results**: N/A

**Validation**: Model responses are scored automatically and validated against human assessments for accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
