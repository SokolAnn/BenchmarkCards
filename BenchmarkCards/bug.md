# BUG

## 📊 Benchmark Details

**Name**: BUG

**Overview**: A large-scale gender bias dataset of 108K diverse real-world English sentences collected using semi-automatic grammatical pattern matching.

**Data Type**: text

**Domains**:
- Wikipedia
- Covid19 research
- PubMed abstracts

**Languages**:
- English

**Similar Benchmarks**:
- WinoGender
- WinoBias
- GAP
- WinoMT

**Resources**:
- [GitHub Repository](https://github.com/SLAB-NLP/BUG)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate gender bias in coreference resolution and machine translation models using a large corpus of real-world sentences.

**Target Audience**:
- NLP researchers
- Machine learning practitioners
- Developers of language models

**Tasks**:
- Gender bias evaluation
- Benchmarking coreference resolution
- Benchmarking machine translation

**Limitations**: N/A

**Out of Scope Uses**:
- Non-gender bias related analyses

## 💾 Data

**Source**: Based on three diverse domains: Wikipedia, Covid19 research, and PubMed abstracts.

**Size**: 108K sentences

**Format**: text

**Annotation**: Each instance is manually verified for quality and marked as stereotypical, anti-stereotypical, or neutral.

## 🔬 Methodology

**Methods**:
- Lexical-syntactic pattern matching
- Semi-automatic sentence collection

**Metrics**:
- Accuracy
- Population bias (ΔG)
- Historical bias (ΔS)

**Calculation**: Metrics are calculated based on F1 scores comparing gender prediction accuracy.

**Interpretation**: Higher values of ΔG or ΔS indicate greater gender bias.

**Baseline Results**: N/A

**Validation**: Results have been validated with human annotators, achieving an 85% accuracy rate for gender assignment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Gender bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

**Potential Harm**: Models may perpetuate harmful gender stereotypes if bias is not addressed.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is publicly available.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
