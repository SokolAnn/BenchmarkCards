# PeKo (Precondition Knowledge dataset)

## 📊 Benchmark Details

**Name**: PeKo (Precondition Knowledge dataset)

**Overview**: PeKo is a crowd-sourced annotation of preconditions between event pairs in news articles, consisting of 28,948 event pairs annotated with precondition relations.

**Data Type**: event-event relation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ATOMIC
- RED
- CaTeRS
- StoryLine

**Resources**:
- [Resource](https://stonybrooknlp.github.io/PeKo/)

## 🎯 Purpose and Intended Users

**Goal**: To develop a resource that helps models reason about necessary preconditions for events mentioned in text.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Precondition Identification
- Precondition Generation

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced annotation from news articles

**Size**: 28,948 event pairs

**Format**: N/A

**Annotation**: Crowdsourced via Amazon MTurk

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on classification task outcomes.

**Interpretation**: Higher F1 scores indicate better identification of precondition relations.

**Baseline Results**: BERT: 71.91 F1, XLNet: 71.52 F1

**Validation**: Evaluated through pilot studies and expert validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misrepresentation of event relations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
