# LegalScore

## 📊 Benchmark Details

**Name**: LegalScore

**Overview**: LegalScore is a benchmark designed for evaluating the performance of generative AI models on Brazilian legal career exams, assessing their ability to answer complex legal questions in a local context.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Portuguese

**Similar Benchmarks**:
- LawBench
- LegalBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the performance of AI models in legal examinations in Brazil, promoting localized training.

**Target Audience**:
- ML Researchers
- Legal Professionals
- Education Researchers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Brazilian legal career examination datasets

**Size**: 10,000 questions

**Format**: CSV

**Annotation**: Annotated by legal professionals and educators in the field.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Performance measured by the percentage of correct answers out of total questions for each model tested.

**Interpretation**: Higher scores indicate better alignment with Brazilian legal knowledge and understanding.

**Baseline Results**: Performance benchmarks established against human candidates who took the exams.

**Validation**: Cross-validated with multiple rounds of testing across various AI models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
