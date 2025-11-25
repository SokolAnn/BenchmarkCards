# HEALTH -PARIKSHA

## 📊 Benchmark Details

**Name**: HEALTH -PARIKSHA

**Overview**: This study provides an extensive assessment of 24 LLMs on real world data collected from Indian patients interacting with a medical chatbot in Indian English and 4 other Indic languages. It evaluates LLM responses on four metrics curated for healthcare applications, establishing leaderboards for each metric.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English
- Hindi
- Tamil
- Telugu
- Kannada

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To conduct a comprehensive assessment of multilingual models within a real-world healthcare context.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The volume of non-English queries is significantly lower than that of English queries, meaning the results on non-English queries should not be considered definitive.

## 💾 Data

**Source**: Dataset curated from questions sent to HEALTH BOT from patients scheduled for cataract surgery.

**Size**: 749 question and ground truth answer pairs

**Format**: CSV

**Annotation**: Questions and responses were reviewed and validated by medical professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Factual Correctness
- Semantic Similarity
- Coherence
- Conciseness

**Calculation**: Metrics are calculated by comparing LLM responses with ground-truth responses and assessing coherence and conciseness based on specific evaluation criteria.

**Interpretation**: Scores range from 0 to 2, evaluating response quality based on specific metrics.

**Baseline Results**: No specific baseline results mentioned.

**Validation**: Validated by comparing LLM outputs with expert-verified ground truth responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All patient data was anonymized, and ethics approval was granted for the study.

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent was obtained from patients and their family members before participation.

**Compliance With Regulations**: Not Applicable
