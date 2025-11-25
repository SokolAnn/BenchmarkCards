# Detection of Adverse Drug Events in Dutch clinical free text documents using Transformer Models – benchmark study

## 📊 Benchmark Details

**Name**: Detection of Adverse Drug Events in Dutch clinical free text documents using Transformer Models – benchmark study

**Overview**: This study sets a benchmark for adverse drug event (ADE) detection in Dutch clinical free text documents using several transformer models, clinical scenarios, and fit-for-purpose performance measures.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- Dutch

**Resources**:
- [Resource](https://huggingface.co/GroNLP/bert-base-dutch-cased)
- [Resource](https://huggingface.co/pdelobelle/robbert-v2-dutch-base)
- [Resource](https://huggingface.co/CLTL/MedRoBERTa.nl)
- [Resource](https://huggingface.co/numind/NuNER-multilingual-v0.1)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to benchmark various transformer models for adverse drug event detection in Dutch clinical free text documents, particularly clinical notes and discharge letters.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- NLP Practitioners

**Tasks**:
- Named Entity Recognition
- Relation Classification

**Limitations**: The gold standard training corpus is small, containing 102 clinical notes.

## 💾 Data

**Source**: Anonymized clinical free text documents from ICU progress notes and discharge letters in Dutch hospitals.

**Size**: 102 clinical progress notes

**Format**: N/A

**Annotation**: Richly annotated by medical experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro-averaged F1 Score
- Macro-averaged F1 Score
- Precision
- Recall

**Calculation**: Micro and macro averaging metrics provide insights into model performance across different classes of ADEs.

**Interpretation**: Higher F1 scores indicate better performance in detecting ADEs, particularly the macro scores are more indicative in the context of imbalanced data.

**Baseline Results**: Micro-averaged F1 scores of ±0.983 for the best models on the Dutch ADE corpus, with MedRoBERTa.nl performing best overall.

**Validation**: 5-fold cross-validation was utilized for evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymized data used from electronic health records, and no patient consent was required due to the use of anonymous data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent not required for anonymized data use.

**Compliance With Regulations**: Exempt from ethics approval as it did not involve human subjects directly.
