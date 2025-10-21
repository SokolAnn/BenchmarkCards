# SAFEWORLD

## 📊 Benchmark Details

**Name**: SAFEWORLD

**Overview**: SAFEWORLD is a benchmark specifically designed to evaluate LLMs' ability to generate responses that are culturally sensitive and legally compliant across diverse global contexts, comprising 2,342 test user queries grounded in cultural norms and legal policies from 50 countries.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Safer-Instruct
- BeaverTail
- ToxicChat

**Resources**:
- [GitHub Repository](https://github.com/PlusLabNLP/SafeWorld)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' responses to geo-diverse safety topics and enhance their alignment with cultural norms and legal standards globally.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Generated from cultural-legal guidelines across 50 countries and 493 regions/races, validated through machine and human evaluations.

**Size**: 2,342 examples

**Format**: JSON

**Annotation**: Human-verified with cultural norms and legal policies.

## 🔬 Methodology

**Methods**:
- Multi-dimensional evaluation framework
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Faithfulness
- Coverage

**Calculation**: Metrics include evaluating response type matching, faithfulness to ground-truth guidelines, and comprehensive coverage of relevant norms.

**Interpretation**: Higher scores indicate better alignment and appropriateness of responses concerning cultural and legal contexts.

**Baseline Results**: Outperforms leading models like GPT-4o across multiple dimensions.

**Validation**: Multi-round validation involving both machine and human evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
