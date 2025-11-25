# Masked Sentence Prediction (MSP)

## 📊 Benchmark Details

**Name**: Masked Sentence Prediction (MSP)

**Overview**: This paper investigates the ability of large language models (LLMs) to predict masked sentences across various domains, evaluating their performance on fidelity and cohesiveness.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the limitations of large language models in predicting masked sentences accurately and coherently across different domains.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Masked Sentence Prediction

**Limitations**: The study is based on a limited number of samples (400) and focuses solely on three types of text domains.

## 💾 Data

**Source**: The datasets used are ROCStories, Recipe1M, and Wikipedia.

**Size**: 400 documents per dataset

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-1
- Semantic similarity metrics (BLEURT, SBERT)

**Calculation**: Metrics are calculated based on similarity between generated sentences and original sentences.

**Interpretation**: A higher BLEU or ROUGE score indicates better fidelity in matching the original sentence.

**Validation**: Evaluation is conducted through automated metrics as well as blind human preference tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: The models may generate plausible but incorrect sentences, leading to misinformation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used were publicly available and compliant with their licenses.

**Data Licensing**: ROCS TORIES is under CC BY 4.0, RECIPE 1M is used under terms permitting non-commercial research, and Wikipedia articles adhere to CC BY-SA.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All datasets and models used are compliant with their respective terms of service.
