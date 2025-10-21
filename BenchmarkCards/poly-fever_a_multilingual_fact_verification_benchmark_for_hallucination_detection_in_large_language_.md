# Poly-FEVER (A Multilingual Fact Verification Benchmark for Hallucination Detection in Large Language Models)

## 📊 Benchmark Details

**Name**: Poly-FEVER (A Multilingual Fact Verification Benchmark for Hallucination Detection in Large Language Models)

**Overview**: Poly-FEVER is a large-scale multilingual fact verification benchmark specifically designed for evaluating hallucination detection in LLMs. It comprises 77,973 labeled factual claims spanning 11 languages, enabling systematic evaluation of LLMs and analysis of hallucination patterns across languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Mandarin Chinese
- Hindi
- Arabic
- Bengali
- Japanese
- Korean
- Tamil
- Thai
- Georgian
- Amharic

**Similar Benchmarks**:
- FEVER
- Climate-FEVER
- SciFact

**Resources**:
- [Resource](https://huggingface.co/datasets/HanzhiZhang/Poly-FEVER)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multilingual benchmark for fact verification and hallucination detection in large language models, enabling the evaluation of model performance across language-specific biases.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Fact Verification
- Hallucination Detection

**Limitations**: The variability in self-detection capabilities across different languages poses challenges for standardizing hallucination detection.

## 💾 Data

**Source**: Derived from existing datasets like FEVER, Climate-FEVER, and SciFact.

**Size**: 77,973 labeled factual claims

**Format**: N/A

**Annotation**: Annotated veracity labels indicating whether the claims align with established factual evidence.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation via comparisons against ground truth

**Metrics**:
- Accuracy
- Factual consistency

**Calculation**: Metrics are calculated by comparing generated content against verified ground-truth data.

**Interpretation**: Higher accuracy indicates better model performance in detecting hallucinations.

**Validation**: Tested and validated using various LLMs including ChatGPT and LLaMA series.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
