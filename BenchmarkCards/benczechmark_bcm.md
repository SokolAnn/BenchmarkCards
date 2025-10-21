# BenCzechMark (BCM)

## 📊 Benchmark Details

**Name**: BenCzechMark (BCM)

**Overview**: BenCzechMark (BCM) is the first comprehensive Czech language benchmark designed for large language models, offering diverse tasks, multiple task formats, and multiple evaluation metrics. It encompasses 50 challenging tasks across 8 categories and covers areas like historical Czech news, essays from pupils or language learners, and spoken word.

**Data Type**: question-answering pairs, multiple-choice questions, open-answer questions

**Domains**:
- Natural Language Processing

**Languages**:
- Czech

**Resources**:
- [Resource](https://huggingface.co/spaces/CZLC/BenCzechMark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating few-shot learners in the Czech language.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Question Answering
- Named Entity Recognition
- Sentiment Analysis
- Natural Language Inference
- Reading Comprehension
- Language Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Data is sourced from various Czech educational tests, newspapers, and historical documents, including newly collected datasets.

**Size**: 320GB

**Format**: Multiple formats including MCF, OAF, CF, LMF

**Annotation**: Manual and semi-manual annotation methods are used for datasets.

## 🔬 Methodology

**Methods**:
- Statistical significance testing
- Duel scoring system
- Evaluation across diverse tasks

**Metrics**:
- Accuracy
- Exact Match (EM)
- Area Under ROC Curve (AUROC)

**Calculation**: Metrics are calculated based on task-specific thresholds and statistical significance of model performance.

**Interpretation**: Results are interpreted through statistical tests to ensure robust performance comparisons.

**Baseline Results**: The first Czech-centric language model serves as a baseline for comparisons.

**Validation**: The benchmark includes a leaderboard for model evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Available under non-commercial research purpose licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
