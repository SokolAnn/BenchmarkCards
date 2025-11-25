# Transparency at the Source: Evaluating and Interpreting Language Models with Access to the True Distribution

## 📊 Benchmark Details

**Name**: Transparency at the Source: Evaluating and Interpreting Language Models with Access to the True Distribution

**Overview**: We present a setup for training, evaluating and interpreting neural language models, that uses artificial, language-like data derived from a large natural language corpus, allowing us to compute exact lower bounds on perplexity and assess model behaviour.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/clclab/pcfg-lm)

## 🎯 Purpose and Intended Users

**Goal**: To provide a controlled environment for training and evaluating language models with synthetic data that approximates natural language complexity.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Language Modelling
- Interpretability

**Limitations**: N/A

## 💾 Data

**Source**: Generated from a state-split Probabilistic Context-Free Grammar (PCFG) that is derived from a large natural language corpus.

**Size**: 7.5 million sentences

**Format**: N/A

**Annotation**: Automatically generated from a parsed corpus.

## 🔬 Methodology

**Methods**:
- Language modelling
- Interpretability probing

**Metrics**:
- Perplexity
- Spearman's ρ
- R²

**Calculation**: Perplexity is computed based on the log probabilities from the language model compared to the true distribution.

**Interpretation**: A lower perplexity indicates better alignment with the true data distribution.

**Validation**: The model's performance is validated against the perplexity of the underlying PCFG.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
