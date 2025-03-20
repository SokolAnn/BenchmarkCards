# REDDIT BIAS

## 📊 Benchmark Details

**Name**: REDDIT BIAS

**Overview**: The first conversational data set grounded in actual human conversations from Reddit, allowing for bias measurement and mitigation across four important bias dimensions: gender, race, religion, and queerness.

**Data Type**: Text

**Domains**:
- Conversational AI
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- CrowS-Pairs

**Resources**:
- [GitHub Repository](https://github.com/umanlp/RedditBias)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate bias in conversational language models.

**Target Audience**:
- Researchers
- AI developers

**Tasks**:
- Bias evaluation
- Debiasing methods application

**Limitations**: Limited to measuring specific biases in conversational AI.

**Out of Scope Uses**:
- General bias evaluation outside of conversational models

## 💾 Data

**Source**: Reddit comments

**Size**: 10,000 comments

**Format**: CSV

**Annotation**: Binary annotation for the presence of bias.

## 🔬 Methodology

**Methods**:
- Language Model Debiasing Loss (LMD)
- Attribute Distance Debiasing (ADD)
- Hard Debiasing Loss (HD)
- Counterfactual Augmentation (CDA)

**Metrics**:
- F1 score for Dialog State Tracking
- Bleu-4 score for Conversational Response Generation

**Calculation**: Statistical significance tests (t-tests) and mean perplexity differences.

**Interpretation**: Assess bias reduction while maintaining model performance.

**Baseline Results**: Original DialoGPT scores without debiasing.

**Validation**: Inter-annotator agreement of .65 on comment level.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias amplification
- Ethical concerns

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities, Impact on education: plagiarism
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Bias measured across multiple demographics: gender, race, religion, and queerness.

**Potential Harm**: Potential exacerbation of existing societal biases through biased model predictions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Comments were anonymized to protect user identities.

**Data Licensing**: Data sourced from publicly available Reddit comments.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Research conducted in compliance with ethical research standards.
