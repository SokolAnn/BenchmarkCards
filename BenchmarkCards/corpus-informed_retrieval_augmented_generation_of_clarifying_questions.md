# Corpus-informed Retrieval Augmented Generation of Clarifying Questions

## 📊 Benchmark Details

**Name**: Corpus-informed Retrieval Augmented Generation of Clarifying Questions

**Overview**: This study aims to develop models that generate corpus informed clarifying questions for web search, ensuring the questions align with the available information in the retrieval corpus. The paper addresses challenges in current datasets and proposes methods for augmenting them to support better clarifying question generation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2409.18575)

## 🎯 Purpose and Intended Users

**Goal**: Generate Corpus-informed Clarifying Questions end-to-end.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MIMICS dataset and augmented data.

**Size**: N/A

**Format**: N/A

**Annotation**: Crowdsourced for clarifying questions and intents based on search system usage.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Term Overlap
- Exact Match
- Set-BERT
- Set-BLEU

**Calculation**: Metrics are calculated based on comparing generated facets to ground truth.

**Interpretation**: High scores indicate better alignment of generated clarifying questions with users' intents.

**Baseline Results**: Various models compared including BART and state-of-the-art ensemble methods.

**Validation**: Results validated through comparative analysis against existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
