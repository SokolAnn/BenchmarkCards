# IMPLEX CONV

## 📊 Benchmark Details

**Name**: IMPLEX CONV

**Overview**: IMPLEX CONV is a large-scale dataset designed to evaluate implicit reasoning in long-term personalized conversations, consisting of 2,500 examples with approximately 100 sessions each and 600 thousand persona traits.

**Data Type**: multi-session dialogue examples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MSC
- DailyDialog
- CC
- LoCoMo

**Resources**:
- [GitHub Repository](https://github.com/Kaylee0501/ImplexConv)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating implicit reasoning in personalized conversational AIs.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: Some conversations in IMPLEX CONV are synthetically generated, leading to potential inconsistencies due to reliance on LLM responses.

## 💾 Data

**Source**: Generated using LLM prompting and persona extraction from Persona Hub.

**Size**: 2,500 examples (∼100 sessions each)

**Format**: N/A

**Annotation**: Automated generation with human verification for implicit reasoning scenarios.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Retrieval Accuracy

**Calculation**: For retrieval accuracy, the formula is defined as: Retrieval Accuracy = (2 × |Cr∩Cg|) / (|Cr| + |Cg|).

**Interpretation**: Higher F1 scores indicate better retrieval efficiency and accuracy of responses to implicit reasoning tasks.

**Baseline Results**: TACITREE achieves 55.18% F1 score on supportive IMPLEX CONV and 14.84% on opposed scenarios.

**Validation**: Evaluated through comparison with baseline models and human evaluation for response accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
