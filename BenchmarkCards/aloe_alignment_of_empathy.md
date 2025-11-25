# ALOE (Alignment of Empathy)

## 📊 Benchmark Details

**Name**: ALOE (Alignment of Empathy)

**Overview**: ALOE is a new dataset introduced for studying empathetic alignment in therapeutic conversations, featuring 9,284 appraisals and 3,262 alignments from Reddit conversations.

**Data Type**: span-level annotations

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jessicayjm/modeling_empathy_alignment)
- [GitHub Repository](https://github.com/jessicayjm/span_alignment_annotation_tool)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on cognitive and emotional empathy through appraisals and their alignment in text-based conversations.

**Target Audience**:
- ML Researchers
- Model Developers
- Mental Health Professionals

**Tasks**:
- Empathetic Alignment Recognition
- Appraisal Classification

**Limitations**: N/A

## 💾 Data

**Source**: Reddit conversations across various subreddits focusing on mental health and emotional support.

**Size**: 29,385 Target-Observer pairs

**Format**: N/A

**Annotation**: Manual annotation by trained annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on model predictions compared to annotated spans.

**Interpretation**: Higher F1 scores indicate better accuracy in identifying appraisals and their alignments.

**Baseline Results**: Random predictions were used as a baseline for comparison.

**Validation**: Models were validated through annotation review and adjudication processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is sourced from public posts on Reddit; measures were taken to mitigate risks of re-exposure to distressing events.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
