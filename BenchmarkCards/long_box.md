# LONG BOX

## 📊 Benchmark Details

**Name**: LONG BOX

**Overview**: LONG BOX is a collection of seven medical datasets in text-to-text format, designed to investigate model performance on long sequences, particularly for clinical tasks requiring the evaluation of long electronic health records (EHR).

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Mihir3009/LongBoX)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of LONG BOX is to facilitate the development of long sequence handling techniques tailored to the clinical domain by providing a benchmark that investigates LLM performance on long medical texts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification
- Relation Extraction
- Multi-label Classification

**Limitations**: LONG BOX is currently limited in task variety as it primarily consists of different types of classification tasks.

## 💾 Data

**Source**: Seven curated clinical datasets from the n2c2 NLP Research Datasets.

**Size**: 85,470 samples in total across different datasets each with varied lengths

**Format**: text

**Annotation**: Annotated based on clinical notes, discharge summaries, and longitudinal records.

## 🔬 Methodology

**Methods**:
- Benchmarking with multiple large language models (LLMs)
- Evaluation of long sequence handling techniques

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: For classification tasks, accuracy is calculated, while F1 Score is used for multi-label classification tasks.

**Interpretation**: Lower accuracy scores indicate challenges in handling long sequences, with an overall indication of model struggle as they achieve average scores of approximately 52%.

**Baseline Results**: Achieved an average score of ∼52% across the benchmarked models.

**Validation**: Results were validated through extensive comparison across multiple LLMs and techniques for long sequence handling.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
