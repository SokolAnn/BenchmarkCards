# MEDHALU (Medical Hallucination Detection Benchmark)

## 📊 Benchmark Details

**Name**: MEDHALU (Medical Hallucination Detection Benchmark)

**Overview**: MEDHALU is a medical hallucination detection benchmark featuring diverse healthcare queries and corresponding LLM responses, annotated with hallucination types and text spans.

**Data Type**: question-answer pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2409.19492)

## 🎯 Purpose and Intended Users

**Goal**: To study LLM hallucinations in real-world healthcare queries from patients and improve detection mechanisms.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Hallucination Detection

**Limitations**: N/A

## 💾 Data

**Source**: Derived from HealthQA, LiveQA, and MedicationQA datasets, featuring healthcare questions answered by LLMs.

**Size**: 2,077 examples

**Format**: JSON

**Annotation**: Labeled by medical experts annotating hallucination types and text spans.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the performance of LLMs and medical experts in identifying hallucinations.

**Interpretation**: A higher F1 Score indicates better performance in hallucination detection.

**Validation**: Expert annotators provided evaluations, achieving a high Cohen’s Kappa score, confirming reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants provided informed consent prior to their participation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Ethics committee approval was received for this research.

**Compliance With Regulations**: Not Applicable
