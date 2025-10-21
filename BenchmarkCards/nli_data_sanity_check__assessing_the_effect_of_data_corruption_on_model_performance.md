# NLI Data Sanity Check: Assessing the Effect of Data Corruption on Model Performance

## 📊 Benchmark Details

**Name**: NLI Data Sanity Check: Assessing the Effect of Data Corruption on Model Performance

**Overview**: We propose a new diagnostics test suite which allows to assess whether a dataset constitutes a good testbed for evaluating the models’ meaning understanding capabilities.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MNLI
- ANLI

**Resources**:
- [GitHub Repository](https://github.com/Helsinki-NLP/nli-data-sanity-check)

## 🎯 Purpose and Intended Users

**Goal**: To contribute a new suite of diagnostic tests that can be used to assess the quality of an NLU benchmark.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: MNLI and ANLI datasets with controlled corruption transformations applied.

**Size**: 433,000 sentence pairs

**Format**: N/A

**Annotation**: The MNLI dataset includes human-written sentence pairs.

## 🔬 Methodology

**Methods**:
- Controlled transformations
- Evaluation of model performance

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on model predictions on original and corrupted datasets.

**Interpretation**: A decrease in accuracy indicates a reliable dataset, while high accuracy on corrupted data indicates biases.

**Baseline Results**: BERT achieved an accuracy of 83.74% on the original MNLI matched development set.

**Validation**: Tests the performance of models fine-tuned on original vs. corrupted data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
