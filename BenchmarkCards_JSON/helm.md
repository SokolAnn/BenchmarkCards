# HELM

## 📊 Benchmark Details

**Name**: HELM

**Overview**: A benchmark for evaluating hallucination detection across multiple LLMs, featuring diverse LLM outputs and the internal states of LLMs during their inference process.

**Data Type**: Text

**Domains**:
- Natural Language Processing
- Hallucination Detection

**Languages**:
- N/A

**Similar Benchmarks**:
- WikiBio GPT3
- SelfCheckGPT
- HaluEval

**Resources**:
- [GitHub Repository](https://github.com/oneal2000/MIND/tree/main)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for hallucination detection in large language models.

**Target Audience**:
- Researchers
- Practitioners in NLP
- AI developers

**Tasks**:
- Detect hallucinations in LLM outputs
- Evaluate hallucination detection methods

**Limitations**: N/A

**Out of Scope Uses**:
- Fact verification tasks
- Applications without LLMs

## 💾 Data

**Source**: Wikipedia

**Size**: 3582 sentences

**Format**: Text

**Annotation**: Annotated for truthfulness with hallucination labels

## 🔬 Methodology

**Methods**:
- Unsupervised training data generation
- Hallucination classifier training using MLP

**Metrics**:
- AUC (Area Under the Curve)
- Pearson correlation coefficient

**Calculation**: AUC calculated at both sentence-level and passage-level.

**Interpretation**: Higher AUC values indicate better detection performance.

**Baseline Results**: MIND outperforms existing state-of-the-art methods in hallucination detection.

**Validation**: Evaluation conducted on HELM dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias in training data
- Inaccurate detection of hallucinations
- Over-reliance on annotations

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information used.

**Data Licensing**: Publicly available data, e.g., Wikipedia.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Focused on ethical considerations in development.
