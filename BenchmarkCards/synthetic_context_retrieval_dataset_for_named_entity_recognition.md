# Synthetic Context Retrieval Dataset for Named Entity Recognition

## 📊 Benchmark Details

**Name**: Synthetic Context Retrieval Dataset for Named Entity Recognition

**Overview**: This paper presents a synthetic context retrieval dataset generated using Alpaca for enhancing named entity recognition (NER) performance in long documents.

**Data Type**: context retrieval pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/CompNet/conivel/tree/gen)

## 🎯 Purpose and Intended Users

**Goal**: To train a neural context retriever for NER using a synthetic dataset that improves context retrieval performance.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using Alpaca from input sentences in an English literary dataset composed of the first chapter of 40 books.

**Size**: 2,716 examples for Alpaca-7B and 2,722 examples for Alpaca-13B

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Neural evaluation
- Retrieval heuristics

**Metrics**:
- F1 Score

**Calculation**: F1 score computed on the performance of various retrieval configurations.

**Interpretation**: Higher F1 scores indicate better performance in NER tasks.

**Baseline Results**: F1 score of 98.01 for the neural retriever on the evaluation portion of the dataset.

**Validation**: Trained on the synthetic retrieval dataset over 3 epochs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: Potential biases in language model generated outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under a free license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
