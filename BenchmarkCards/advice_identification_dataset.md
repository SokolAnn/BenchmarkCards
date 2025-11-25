# Advice Identification Dataset

## 📊 Benchmark Details

**Name**: Advice Identification Dataset

**Overview**: We present a dataset in English from two Reddit advice forums – r/AskParents and r/needadvice – annotated for whether sentences in posts contain advice or not.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- REDDITADVICE

**Resources**:
- [GitHub Repository](https://github.com/venkatasg/Advice-EMNLP2020)

## 🎯 Purpose and Intended Users

**Goal**: This work aims to advance both our understanding of how people give advice, as well as to provide resources for learning to identify advice.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Advice Identification

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from Reddit advice forums r/AskParents and r/needadvice.

**Size**: 18,456 sentences across 684 posts

**Format**: N/A

**Annotation**: Crowdsourced advice annotations from Amazon Mechanical Turk, with DAWID-SKENE aggregated labels.

## 🔬 Methodology

**Methods**:
- Crowdsourced annotation
- Fine-tuning of BERT

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Standard metrics for evaluating binary classification.

**Interpretation**: Scores indicate how well sentences were classified as advice or not.

**Baseline Results**: Rule-based models offered as baselines; BERT-based models performed comparably.

**Validation**: Validated using expert annotations and DAWID-SKENE labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
