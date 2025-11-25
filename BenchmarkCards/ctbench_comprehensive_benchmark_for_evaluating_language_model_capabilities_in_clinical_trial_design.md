# CTBench (Comprehensive Benchmark for Evaluating Language Model Capabilities in Clinical Trial Design)

## 📊 Benchmark Details

**Name**: CTBench (Comprehensive Benchmark for Evaluating Language Model Capabilities in Clinical Trial Design)

**Overview**: CTBench is a benchmark to assess language models (LMs) in aiding clinical study design, examining how well AI models can determine baseline features of clinical trials.

**Data Type**: clinical trial metadata and baseline features

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/nafis-neehal/CTBench_LLM)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to assess the role of language models in aiding clinical study design by predicting baseline characteristics based on metadata.

**Target Audience**:
- Clinical researchers
- AI researchers
- Healthcare professionals

**Tasks**:
- Baseline feature prediction
- Evaluation of language models

**Limitations**: CTBench consists of only RCTs for 5 chronic diseases with a subset annotated with additional 

## 💾 Data

**Source**: ClinicalTrials.gov API and relevant publications

**Size**: 1,690 clinical trials

**Format**: structured textual data

**Annotation**: Manually collected baseline features by human annotators from clinical publications

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics using ListMatch-LM and ListMatch-BERT

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision and recall are calculated based on the matched pairs and the remaining candidate/reference features.

**Interpretation**: High recall ensures that all relevant baseline features are identified for accurate characterization of study cohorts.

**Validation**: Validated through human-in-the-loop evaluations and expert feedback.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
