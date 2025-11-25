# BEHONEST (Benchmarking Honesty in Large Language Models)

## 📊 Benchmark Details

**Name**: BEHONEST (Benchmarking Honesty in Large Language Models)

**Overview**: BEHONEST is designed to assess honesty in LLMs comprehensively, evaluating awareness of knowledge boundaries, avoidance of deceit, and consistency in responses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/GAIR-NLP/BeHonest)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and analyze the honesty of various popular large language models.

**Target Audience**:
- AI Researchers
- Model Developers

**Tasks**:
- Honesty Assessment

**Limitations**: N/A

## 💾 Data

**Source**: SelfAware, UnknownBench, TrustLLM, TruthfulQA, Big-Bench Hard, CommonSenseQA

**Size**: 22,683 examples

**Format**: JSON

**Annotation**: Ethically annotated datasets containing questions and scenarios.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Refusal rate
- Answer rate
- Sycophancy rate
- Lying rate
- Inconsistency rate
- Performance spread
- Agreement rate
- Consistency rate

**Calculation**: Metrics are computed based on defined scenarios and threshold values.

**Interpretation**: Higher rates of refusal and accuracy indicate better honesty performance.

**Validation**: Validated through comparative analysis across nine popular LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Potential Harm**: ['Misinformation spread', 'Potential harm through deception']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
