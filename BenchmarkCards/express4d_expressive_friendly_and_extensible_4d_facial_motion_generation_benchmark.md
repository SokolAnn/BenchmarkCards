# Express4D (Expressive, Friendly, and Extensible 4D Facial Motion Generation Benchmark)

## 📊 Benchmark Details

**Name**: Express4D (Expressive, Friendly, and Extensible 4D Facial Motion Generation Benchmark)

**Overview**: Express4D is a facial motion dataset and baseline benchmark, comprising 1205 diverse sequences performed by 18 participants, featuring LLM-based natural language instruction labels which are performed and recorded.

**Data Type**: 3D facial motion sequences

**Domains**:
- Computer Graphics

**Languages**:
- English

**Resources**:
- [Resource](https://jaron1990.github.io/Express4D/)

## 🎯 Purpose and Intended Users

**Goal**: To enable automatic facial motion generation from natural language.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Facial Motion Generation

**Limitations**: The expressions are based on non-professional actors, potentially missing some complex expressions.

## 💾 Data

**Source**: Collected using ARKit framework via the Live Link Face app

**Size**: 1205 sequences

**Format**: CSV

**Annotation**: LLM-generated natural language descriptions

## 🔬 Methodology

**Methods**:
- Automated metrics
- Quantitative comparisons

**Metrics**:
- Fréchet Inception Distance (FID)
- R-Precision
- Diversity
- Multimodal distance

**Calculation**: Metrics computed by comparing generated sequences with real sequences via learned feature embeddings.

**Interpretation**: Lower scores indicate better model performance in generating realistic and diverse motion sequences.

**Validation**: Evaluated using initial performances of two baseline models trained on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Nonconsensual use, Spreading disinformation

**Demographic Analysis**: The dataset covers emotions from diverse participants but may not fully represent ethnic diversity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under a license prohibiting malicious applications including deep-fake generation.

**Consent Procedures**: Participants provided consent for their expressions to be recorded.

**Compliance With Regulations**: Not Applicable
