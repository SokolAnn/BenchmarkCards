# ELEPHANT (Evaluating Large Language Models for Social Sycophancy)

## 📊 Benchmark Details

**Name**: ELEPHANT (Evaluating Large Language Models for Social Sycophancy)

**Overview**: ELEPHANT is a benchmark for measuring social sycophancy in large language models (LLMs), characterizing sycophancy as the excessive preservation of a user's face by affirming their self-image or avoiding challenges to it. The benchmark evaluates LLMs across four dimensions of sycophancy using multiple datasets that encompass various real-world situations and moral dilemmas.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Moral Reasoning Benchmarks
- Bias and Fairness in NLP

**Resources**:
- [GitHub Repository](https://github.com/myracheng/elephant)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework and empirical benchmarks for quantifying social sycophancy in LLMs, thereby facilitating their evaluation and improvement.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Various datasets including open-ended queries, Reddit posts from r/AmITheAsshole, and assumption-laden statements from r/Advice.

**Size**: 3,027 advice queries, 2,000 posts from r/AmITheAsshole, 3,777 assumption-laden statements, 1,591 pairs of moral dilemmas.

**Format**: JSON

**Annotation**: Human-validated annotations by expert raters.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Validation
- Indirectness
- Framing

**Calculation**: Scores are calculated based on human-validated sycophancy judgments comparing LLM outputs to crowdsourced human responses.

**Interpretation**: A score closer to 0 indicates behavior akin to human respondents, while positive values indicate higher levels of sycophancy than humans.

**Baseline Results**: Scores compared against human-validated judgments across the datasets, ensuring comprehensive evaluation of model outcomes.

**Validation**: High inter-annotator agreement (Fleiss’ κ ≥ 0.70) after a pilot round for discrepancy resolution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
