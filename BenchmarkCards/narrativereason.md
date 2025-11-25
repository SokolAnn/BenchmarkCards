# NarrativeReason

## 📊 Benchmark Details

**Name**: NarrativeReason

**Overview**: The paper introduces NarrativeReason, a novel dataset focused on temporal relations among sequential events within narratives, which enhances the capabilities of Large Language Models (LLMs) for the task of timeline summarisation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the quality of timeline summarisation by combining temporal reasoning with the understanding of sequences of events in narratives.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Timeline Summarisation

**Limitations**: The dataset may contain bias based on the narratives selected, affecting its applicability across different contexts.

## 💾 Data

**Source**: Extracted and reconstructed from the NarrativeTime dataset, which is based on annotations from the TimeBankNT corpus.

**Size**: 19,614 question-answering pairs

**Format**: N/A

**Annotation**: Manually annotated temporal relations among a series of events.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Knowledge Distillation

**Metrics**:
- Factual Consistency
- Evidence Appropriateness

**Calculation**: Metrics calculated based on generated summarisation's alignment with factual data and human-written summaries.

**Interpretation**: Higher scores indicate improved accuracy and reliability of generated summaries.

**Validation**: The model was validated through experimental results demonstrating improved performance on timeline summarisation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential biases in the dataset could lead to inaccurate representations of narratives.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ethics institutional review board approval was obtained to analyze user generated content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
