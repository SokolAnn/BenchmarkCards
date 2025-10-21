# EXECUTE: A Multilingual Benchmark for LLM Token Understanding

## 📊 Benchmark Details

**Name**: EXECUTE: A Multilingual Benchmark for LLM Token Understanding

**Overview**: EXECUTE benchmark tests token understanding in a variety of languages, revealing challenges in character and word processing across different writing systems. It is designed for easy expansion to new languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Amharic
- Arabic
- Chinese
- English
- Hindi
- Japanese
- Korean
- Russian

**Similar Benchmarks**:
- CUTE

**Resources**:
- [GitHub Repository](https://github.com/Leukas/EXECUTE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and advance understanding of how multilingual LLMs manipulate tokens in various languages and writing systems.

**Target Audience**:
- ML Researchers
- Model Developers
- Linguists

**Tasks**:
- Token manipulation
- Character understanding
- Word understanding

**Limitations**: Limited to 8 languages; the performance of languages not tested may vary.

## 💾 Data

**Source**: An updated subset of 5000 stories from the TinyStories dataset, translated using Google Translate.

**Size**: 5,000 examples

**Format**: JSON

**Annotation**: Automatic translation with verification by fluent speakers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are computed based on task performance evaluations.

**Interpretation**: Higher scores indicate better performance in token manipulation tasks.

**Validation**: Results compared across multiple LLMs to validate performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark explicitly analyzes performance across different language groups to evaluate fairness.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
