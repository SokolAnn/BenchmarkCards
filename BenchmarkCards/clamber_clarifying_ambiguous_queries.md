# CLAMBER (Clarifying Ambiguous Queries)

## 📊 Benchmark Details

**Name**: CLAMBER (Clarifying Ambiguous Queries)

**Overview**: CLAMBER presents a benchmark for evaluating LLMs in identifying and clarifying ambiguous user queries through a well-organized taxonomy, providing ∼12K high-quality data.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zt991211/CLAMBER)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs in identifying and clarifying ambiguous queries to enhance user trust and information retrieval.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Ambiguity Identification
- Clarifying Question Generation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from various datasets including ALCUNA, AmbiTask, AmbER, AmbiPun, AmbiCoref, AmbigQA, and Dolly.

**Size**: 12,000 examples

**Format**: JSON

**Annotation**: Manually annotated by linguistic experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of LLMs in identifying ambiguities and generating clarifying questions.

**Interpretation**: High Accuracy and F1 Score indicate effective performance in handling ambiguity.

**Baseline Results**: Results include evaluations against various LLMs including ChatGPT, Llama2, and Vicuna.

**Validation**: Dataset validation involved five linguistic experts reviewing the ambiguity labels and clarifying questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
