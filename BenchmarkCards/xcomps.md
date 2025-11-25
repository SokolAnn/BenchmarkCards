# XCOMPS

## 📊 Benchmark Details

**Name**: XCOMPS

**Overview**: XCOMPS is a multilingual benchmark dataset that evaluates the conceptual understanding of large language models (LLMs) across 17 languages through minimal pairs. It aims to assess whether LLMs' conceptual-property reasoning is consistent across languages while highlighting the challenges faced by models, especially in low-resource languages.

**Data Type**: minimal pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Catalan
- German
- Greek
- Spanish
- Persian
- French
- Hebrew
- Hungarian
- Japanese
- Korean
- Dutch
- Russian
- Turkish
- Ukrainian
- Vietnamese
- Chinese

**Similar Benchmarks**:
- COMPS

**Resources**:
- [GitHub Repository](https://github.com/LinyangHe/XCOMPS)

## 🎯 Purpose and Intended Users

**Goal**: To assess multilingual conceptual understanding in large language models (LLMs) through the evaluation of conceptual minimal pairs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Conceptual Understanding Evaluation

**Limitations**: The dataset does not cover all linguistic families or low-resource languages, which may limit its generalizability.

## 💾 Data

**Source**: Constructed using human-LLM interactive translation combining manual translations and LLMs for generating sentence pairs.

**Size**: 244.3k minimal pairs

**Format**: N/A

**Annotation**: Translation and sentence generation completed by a combination of human experts and large language models.

## 🔬 Methodology

**Methods**:
- Metalinguistic prompting
- Neurolinguistic probing
- Direct probability measurement

**Metrics**:
- F1 Score

**Calculation**: Metrics calculated through performance evaluations based on the generated minimal pair sentences.

**Interpretation**: Results interpreted through comparative performance across languages, especially focusing on low-resource languages.

**Validation**: Validated through experiments on multiple models, including variations of the Llama-3 architecture.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of multilingual performance highlights disparities in concept understanding across different languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
