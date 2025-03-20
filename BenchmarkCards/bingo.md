# Bingo

## 📊 Benchmark Details

**Name**: Bingo

**Overview**: The Bingo benchmark is designed to evaluate and shed light on the two common types of hallucinations in visual language models: bias and interference.

**Data Type**: images and text prompts

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English
- Chinese
- Arabic
- French
- Japanese

**Similar Benchmarks**:
- LLaV A
- Bard

**Resources**:
- [GitHub Repository](https://github.com/gzcch/Bingo)

## 🎯 Purpose and Intended Users

**Goal**: To analyze hallucinations in vision-language models, specifically focusing on GPT-4V(ision).

**Target Audience**:
- Researchers
- Developers
- AI practitioners

**Tasks**:
- Evaluating hallucination responses
- Identifying bias and interference in AI models

**Limitations**: None

## 💾 Data

**Source**: Curated dataset from various cultural and linguistic contexts.

**Size**: 190 failure instances and 131 success instances

**Format**: Images paired with text prompts

**Annotation**: Human annotated for correctness

## 🔬 Methodology

**Methods**:
- Human evaluation
- Comparative analysis
- Statistical evaluation

**Metrics**:
- Accuracy
- Error rates

**Calculation**: Accuracy is calculated as the percentage of correct responses versus total responses.

**Interpretation**: Evaluates performance based on bias and interference categories.

**Validation**: Validated through human annotators

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Interference

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not specifically addressed but caution noted regarding biases.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
