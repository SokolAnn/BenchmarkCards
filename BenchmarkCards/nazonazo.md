# Nazonazo

## 📊 Benchmark Details

**Name**: Nazonazo

**Overview**: Nazonazo is a cost-effective and extensible benchmark built from Japanese children's riddles to test insight-based reasoning. The benchmark measures the reasoning capabilities of large language models (LLMs) using riddles that require minimal domain knowledge and can be generated at scale.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- RiddleSense

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.17019050)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable evaluation of insight problem-solving abilities in LLMs using japanese riddles to address benchmark saturation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Insight-based reasoning

**Limitations**: Nazonazo is language and culture-dependent, making generalization to other languages challenging.

## 💾 Data

**Source**: Japanese children's riddles from Nazonazo Gakuen

**Size**: 201 items

**Format**: N/A

**Annotation**: Items are primarily generated and reviewed by authors.

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct responses from total attempts.

**Interpretation**: Scores closer to human performance indicate better reasoning capabilities.

**Baseline Results**: Human mean accuracy is 52.9%.

**Validation**: Through repeated testing and adjusting against human responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No Personally Identifiable Information (PII) was collected.

**Data Licensing**: The benchmark is available under a research-friendly license.

**Consent Procedures**: Human experiments were approved by Knowledge Science Ethics Council.

**Compliance With Regulations**: Not Applicable
