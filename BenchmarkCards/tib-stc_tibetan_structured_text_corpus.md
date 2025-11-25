# TIB-STC (Tibetan Structured Text Corpus)

## 📊 Benchmark Details

**Name**: TIB-STC (Tibetan Structured Text Corpus)

**Overview**: TIB-STC is the first large-scale, expert-curated, and multi-domain dataset designed for the development and evaluation of LLMs for the Tibetan language, covering over 11 billion tokens across various domains.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Tibetan

**Similar Benchmarks**:
- TLUE (Tibetan Language Understanding Evaluation)

**Resources**:
- [GitHub Repository](https://github.com/Vicentvankor/sun-shine)

## 🎯 Purpose and Intended Users

**Goal**: To support the development and evaluation of large language models for low-resource languages like Tibetan.

**Target Audience**:
- ML Researchers
- Language Model Developers
- Domain Experts

**Tasks**:
- Language Modeling
- Instruction Tuning

**Limitations**: N/A

## 💾 Data

**Source**: Expert-curated corpus sourced from literature, religion, medicine, law, and daily communication.

**Size**: 11 billion tokens

**Format**: Raw text files

**Annotation**: Manually curated by domain experts

## 🔬 Methodology

**Methods**:
- Evaluation on TLUE Benchmark
- Human evaluation

**Metrics**:
- Response Rate
- Accuracy
- Conditional Accuracy

**Calculation**: Metrics are calculated based on the proportion of valid responses and correctness.

**Interpretation**: Higher metrics indicate better model performance on Tibetan-specific tasks.

**Baseline Results**: Sun-Shine model is evaluated against existing models like GPT-4o and DeepSeek-R1, demonstrating strong performance.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
