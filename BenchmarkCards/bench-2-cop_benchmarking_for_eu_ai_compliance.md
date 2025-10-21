# Bench-2-CoP (Benchmarking for EU AI Compliance)

## 📊 Benchmark Details

**Name**: Bench-2-CoP (Benchmarking for EU AI Compliance)

**Overview**: Bench-2-CoP is a novel framework designed to evaluate existing AI benchmarks against the requirements set forth by the EU AI Act, focusing on systemic risks and compliance assessment.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- Big Bench Hard
- CommonsenseQA
- TruthfulQA

**Resources**:
- [Resource](https://arxiv.org/abs/2508.05464)

## 🎯 Purpose and Intended Users

**Goal**: To quantify the benchmark-regulation gap by assessing the coverage of current AI evaluation benchmarks against the EU AI Act's taxonomy of model capabilities and propensities.

**Target Audience**:
- Regulatory Bodies
- AI Developers
- AI Researchers
- Policymakers

**Tasks**:
- Compliance Evaluation
- Risk Assessment

**Limitations**: N/A

## 💾 Data

**Source**: A curated dataset of benchmark questions from major AI benchmarks focusing on compliance with the EU AI Act.

**Size**: 194,955 questions

**Format**: JSON

**Annotation**: Human-annotated by experts with inter-rater reliability validation.

## 🔬 Methodology

**Methods**:
- LLM-as-judge analysis
- Quantitative assessment
- Expert validation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated as part of the evaluation of benchmark questions against the EU AI Act taxonomy.

**Interpretation**: High scores indicate good coverage of the capabilities/propensities, while low scores highlight critical gaps.

**Baseline Results**: N/A

**Validation**: Validated against a gold standard dataset annotated by human experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Compliance
- Safety
- Robustness
- Security

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

**Compliance With Regulations**: Addresses the regulatory compliance needs outlined in the EU AI Act.
