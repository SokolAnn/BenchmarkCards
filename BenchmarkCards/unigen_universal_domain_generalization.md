# UNIGEN (Universal Domain Generalization)

## 📊 Benchmark Details

**Name**: UNIGEN (Universal Domain Generalization)

**Overview**: UNIGEN proposes a method for universal domain generalization using zero-shot dataset generation to create a domain-invariant training dataset, allowing small task-specific models to generalize across various domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/c-juhwan/unigen)

## 🎯 Purpose and Intended Users

**Goal**: To achieve universal domain generalization for sentiment classification without the need for labeled data from multiple domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Sentiment Analysis
- Text Classification

**Limitations**: The primary limitation of UNIGEN is its relatively weaker in-domain performance than those of baselines trained with domain-specific datasets.

## 💾 Data

**Source**: Generated using a pre-trained language model and a universal prompt.

**Size**: 1,000,000 examples

**Format**: CSV

**Annotation**: Automatically generated with pseudo-labels.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the average performance results across different random seeds.

**Interpretation**: Higher scores indicate better performance of the Task-specific models trained using UNIGEN compared to baseline models.

**Baseline Results**: UNIGEN's TAM significantly outperformed baseline models that use domain-specific training.

**Validation**: Results were validated through extensive experiments on multiple sentiment classification datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: The generated data may contain biased sentences, reflecting the potential biases of the pre-trained language models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
