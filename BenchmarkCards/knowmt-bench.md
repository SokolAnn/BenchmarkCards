# KnowMT-Bench

## 📊 Benchmark Details

**Name**: KnowMT-Bench

**Overview**: KnowMT-Bench is the first benchmark designed to systematically evaluate Multi-Turn Long-Form Question Answering (MT-LFQA) for large language models across knowledge-intensive fields including medicine, finance, and law. It features dynamic evaluation settings where models generate multi-turn dialogue histories given logically progressive question sequences, allowing for a thorough examination of factual capability and information delivery efficiency.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- K-QA
- FinTextQA
- cLegal-QA
- MedLFQA

**Resources**:
- [Resource](https://arxiv.org/abs/2509.21856)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for assessing Multi-Turn Long-Form Question Answering (MT-LFQA) in knowledge-intensive domains and to facilitate the evaluation and enhancement of the conversational factual capabilities of large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 801 evidence-grounded LFQA instances from authoritative sources in medicine, finance, and law, constructed from prior LFQA benchmarks and manual annotation.

**Size**: 801 instances

**Format**: JSON

**Annotation**: Manual annotation by experts and crowdsourced validation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Factual Precision
- Factual Recall

**Calculation**: Metrics are evaluated based on the factual capability and information delivery efficiency of model responses compared against ground-truth answers.

**Interpretation**: Higher scores indicate better factual accuracy and efficiency in delivering answers in a multi-turn dialogue context, while lower scores indicate factual degradation and verbosity.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through extensive human-validated automated performance assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
