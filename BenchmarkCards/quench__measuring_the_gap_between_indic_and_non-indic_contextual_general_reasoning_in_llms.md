# QUENCH: Measuring the gap between Indic and Non-Indic Contextual General Reasoning in LLMs

## 📊 Benchmark Details

**Name**: QUENCH: Measuring the gap between Indic and Non-Indic Contextual General Reasoning in LLMs

**Overview**: QUENCH is a novel text-based English Quizzing Benchmark manually curated from YouTube quiz videos that assesses world knowledge and deduction capabilities of large language models (LLMs) via a zero-shot, open-domain quizzing setup.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- SuperGLUE
- HELM

**Resources**:
- [GitHub Repository](https://github.com/aflah02/QUENCH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the deductive reasoning capabilities of LLMs using a novel quiz trivia dataset.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Entity Prediction
- Rationale Generation

**Limitations**: N/A

## 💾 Data

**Source**: Manually annotated YouTube quiz videos.

**Size**: 400 questions

**Format**: N/A

**Annotation**: Manual annotation by expert annotators

## 🔬 Methodology

**Methods**:
- Evaluation with zero-shot prompting
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L
- BERTScore

**Calculation**: Scores are calculated based on predicted entities and their corresponding rationales across various models.

**Interpretation**: Higher scores indicate better performance in predicting masked entities and generating accurate rationales.

**Baseline Results**: GPT-4-Turbo yields the highest performance based on multiple metrics.

**Validation**: Evaluation against seven different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Evaluation includes both Indic and Non-Indic subsets.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Publicly sourced content from YouTube quiz videos.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
