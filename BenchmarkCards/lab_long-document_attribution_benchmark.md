# LAB (Long-document Attribution Benchmark)

## 📊 Benchmark Details

**Name**: LAB (Long-document Attribution Benchmark)

**Overview**: LAB is a benchmark consisting of 6 long document datasets with diverse tasks related to attribution, evaluating models on their ability to attribute responses and evidence extraction.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal
- Computer Science
- Government

**Languages**:
- English

**Similar Benchmarks**:
- QASPER
- Natural Questions
- Evidence Inference
- Wice
- ContractNLI
- GovReport

**Resources**:
- [GitHub Repository](https://github.com/UKPLab/LAB)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models in the context of long document attribution tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering
- Classification
- Fact Checking
- Natural Language Inference
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Compiles datasets from existing benchmarks focusing on tasks requiring attribution in long documents.

**Size**: Approximately 234,340 instances across multiple datasets

**Format**: Various formats including CSV and JSON

**Annotation**: Manually annotated evidence by experts and automated evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Attributability
- Unanswerable F1
- F1 Score
- ROUGE-L

**Calculation**: Metrics are calculated using standard formulas based on model predictions and ground truth labels.

**Interpretation**: High scores indicate improved model performance in generating attributed responses.

**Baseline Results**: Benchmarks include existing datasets like QASPER and Natural Questions.

**Validation**: Validated through comparative analysis against established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Various licenses including CC BY 4.0 and MIT for datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
