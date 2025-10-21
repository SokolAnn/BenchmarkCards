# C HARBENCH

## 📊 Benchmark Details

**Name**: C HARBENCH

**Overview**: C HARBENCH is a comprehensive benchmark of character-level tasks that evaluates the performance of language models on character-level reasoning tasks. It aims to systematically assess models’ ability to reason over characters, specifically through counting and positional understanding tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/omriuz/CharBencharXiv:2508.02591v2)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of language models on character-level reasoning tasks and to analyze the impact of tokenization on their performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Character Counting
- Position Finding

**Limitations**: Our evaluation is limited to character-level tasks in English, chosen to minimize potential confounders such as frequency in the training data.

## 💾 Data

**Source**: Uniformly sampled over 10,000 words from the MiniPile dataset.

**Size**: 10,000 examples

**Format**: question-answer format

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is defined as the proportion of predictions matching the gold-standard label.

**Interpretation**: Higher accuracy indicates better performance in correctly identifying character occurrences or positions.

**Validation**: Evaluated the performance of multiple models across varying task difficulties.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
