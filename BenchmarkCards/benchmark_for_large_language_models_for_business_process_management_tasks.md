# Benchmark for Large Language Models for Business Process Management Tasks

## 📊 Benchmark Details

**Name**: Benchmark for Large Language Models for Business Process Management Tasks

**Overview**: This paper addresses the gap in benchmarking LLM performance in the Business Process Management (BPM) domain by systematically comparing LLM performance on four BPM tasks, focusing on small open-source models.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Business Process Management

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/KiriBu10/openLLMinBPM-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To systematically compare the performance of LLMs on BPM tasks and understand their practical applications in organizations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Activity Recommendation
- Identifying RPA Candidates
- Process Question Answering
- Mining Declarative Process Models

**Limitations**: The results cannot be generalized to other domains or LLMs.

## 💾 Data

**Source**: Data derived from multiple real-world BPM task datasets tailored for specific tasks.

**Size**: 288 test samples for activity recommendation task, 424 samples for RPA candidate identification, and 60 samples for process question answering.

**Format**: Various formats per task.

**Annotation**: Datasets were constructed and filtered from existing BPM model collections and created based on process descriptions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Average cosine similarity
- Precision
- Recall
- F1 Score
- ROUGE-L

**Calculation**: Metrics are calculated based on model performance on respective BPM tasks.

**Interpretation**: Performance results are interpreted through comparisons of precisions and scores across tasks.

**Baseline Results**: Comparison against established benchmarks from prior studies.

**Validation**: Validation of model performance conducted via systematic testing against created benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
