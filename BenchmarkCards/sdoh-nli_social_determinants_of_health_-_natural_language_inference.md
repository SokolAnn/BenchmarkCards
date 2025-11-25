# SDOH-NLI (Social Determinants of Health - Natural Language Inference)

## 📊 Benchmark Details

**Name**: SDOH-NLI (Social Determinants of Health - Natural Language Inference)

**Overview**: SDOH-NLI is a dataset for inferring social determinants of health from clinical notes, formulated as a natural language inference task with binary textual entailment labels.

**Data Type**: text

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/SDOH-NLI)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality entailment dataset for extracting social determinants of health from clinical notes and to support broader NLI research.

**Target Audience**:
- ML Researchers
- Healthcare Providers
- NLP Researchers

**Tasks**:
- Natural Language Inference

**Limitations**: The dataset is English-only and reflects the American healthcare system.

## 💾 Data

**Source**: Data was based on medical reports from MTSamples.com, consisting of social history snippets collected from clinical notes.

**Size**: 29,635 examples

**Format**: CSV

**Annotation**: Annotated by human raters using majority voting for binary entailment labels.

## 🔬 Methodology

**Methods**:
- Fine-tuning experiments
- Zero/few-shot prompting
- Retrieval-based evaluations

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the predicted and true labels across the dataset.

**Interpretation**: Higher scores indicate better model performance in accurately identifying SDOH factors from clinical note snippets.

**Validation**: The dataset was split into training, validation, and test sets using a ratio of 70:15:15.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Dataset reflects U.S. norms for social determinants of health, may not generalize to other populations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Uses public and non-identifiable data for study, minimizing privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
