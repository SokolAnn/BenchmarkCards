# LLMs for Law: Evaluating Legal-Specific LLMs on Contract Understanding

## 📊 Benchmark Details

**Name**: LLMs for Law: Evaluating Legal-Specific LLMs on Contract Understanding

**Overview**: This paper presents a comprehensive evaluation of 10 legal-specific LLMs on three English-language contract understanding tasks, comparing them with 7 general-purpose LLMs. It identifies model strengths, weaknesses, and challenges, serving as a resource for legal LLM evaluation.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- LEXGLUE
- LexT5

**Resources**:
- [Resource](https://arxiv.org/abs/2508.07849)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark legal-specific LLMs against general-purpose LLMs across contract understanding tasks.

**Target Audience**:
- ML Researchers
- Legal Professionals
- Industry Practitioners

**Tasks**:
- Unfair Contractual Terms Identification
- Contract Provision Topic Classification
- Agent-Specific Deontic Modality Detection

**Limitations**: The limited availability of contract benchmark datasets in languages other than English poses a challenge for multilingual extension.

## 💾 Data

**Source**: Publicly available datasets including UNFAIR-ToS, LEDGAR, and LEXDEMOD.

**Size**: 70,000 examples

**Format**: CSV

**Annotation**: Manual annotation by legal experts.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Zero-shot testing
- Few-shot testing

**Metrics**:
- Micro-F1
- Macro-F1

**Calculation**: Metrics are calculated based on performance across benchmark datasets.

**Interpretation**: Higher F1 scores indicate better performance on contract understanding tasks.

**Baseline Results**: Legal-BERT and Contracts-BERT establish new SOTAs on two tasks, outperforming general-purpose LLMs.

**Validation**: Models were evaluated based on their accuracy on held-out test datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Demographic factors were not explicitly assessed across the evaluated models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used are publicly available and contain no personal data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
