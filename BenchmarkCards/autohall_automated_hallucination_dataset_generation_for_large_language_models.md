# AutoHall (Automated Hallucination Dataset Generation for Large Language Models)

## 📊 Benchmark Details

**Name**: AutoHall (Automated Hallucination Dataset Generation for Large Language Models)

**Overview**: AutoHall is an approach for automatically constructing model-specific hallucination datasets based on existing fact-checking datasets, addressing the challenge of manual annotation in hallucination detection.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Halueval

**Resources**:
- [Resource](https://arxiv.org/abs/2310.00259)

## 🎯 Purpose and Intended Users

**Goal**: To generate hallucination detection datasets automatically to improve the accuracy of hallucination detection methods.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Hallucination Detection

**Limitations**: The current version of AutoHall has a possibility of leading to false positives which can affect detection accuracy.

## 💾 Data

**Source**: Existing fact-checking datasets like Climate-fever, PUBHEALTH, and WICE.

**Size**: 13144 examples

**Format**: N/A

**Annotation**: Automatically generated through a zero-resource approach.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the classification of hallucinations against ground truth labels.

**Interpretation**: Higher F1 scores indicate better hallucination detection performance.

**Validation**: Validated against human evaluation with a classification accuracy of 92%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
