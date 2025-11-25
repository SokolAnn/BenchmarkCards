# DUSK (Do Not Unlearn Shared Knowledge)

## 📊 Benchmark Details

**Name**: DUSK (Do Not Unlearn Shared Knowledge)

**Overview**: DUSK is a benchmark designed to evaluate unlearning methods under realistic data overlap by constructing document sets that describe the same factual content in different styles, enabling controlled attribution.

**Data Type**: document sets with unique and shared knowledge

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MUSE

**Resources**:
- [Resource](https://ai-isl.github.io/dusk)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate machine unlearning in realistic multi-source scenarios where forget data overlaps with retain data.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Unlearning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic dataset constructed from 120 fictional professor profiles with styles for factual content representation.

**Size**: 600 profiles distributed across five documents

**Format**: JSONL

**Annotation**: Automated generation with prompt designs ensuring diversity in attribute representation.

## 🔬 Methodology

**Methods**:
- Verbatim Memorization
- Unique Forget Knowledge
- Shared Knowledge
- Unique Retain Knowledge
- Downstream Capability
- Privacy Leakage
- Retain Deviation

**Metrics**:
- ROUGE-1
- ROUGE-L
- Levenshtein distance
- Cosine similarity

**Calculation**: Metrics are calculated based on the performance of models on designated QA tasks assessing unlearning effectiveness.

**Interpretation**: Lower scores on metrics such as ROUGE indicate effective unlearning of verbatim content.

**Baseline Results**: Retrain model serves as the baseline for comparison in evaluating unlearning methods.

**Validation**: Evaluation conducted through systematic assessment of unlearning performance on synthetic professor data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Unintentional knowledge loss affecting reliability and fairness.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
