# Time-LongQA Dataset

## 📊 Benchmark Details

**Name**: Time-LongQA Dataset

**Overview**: The Time-LongQA Dataset is designed to test temporal reasoning across evolving knowledge using real-world corporate annual reports. It consists of 2,292 question-answer pairs covering various temporal constraints.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of RAG methods in handling long-text question answering tasks with temporal knowledge bases.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from corporate annual reports of Audi from 2012 to 2023.

**Size**: 2,292 question-answer pairs

**Format**: CSV

**Annotation**: QA pairs were generated through an automated process and manually validated.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual validation

**Metrics**:
- Accuracy

**Calculation**: The accuracy is calculated by majority voting of judgments made by multiple LLM evaluations.

**Interpretation**: A result is deemed correct if at least two out of three evaluations by the model agree on its correctness.

**Validation**: QA pairs were manually validated to avoid temporal conflicts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
