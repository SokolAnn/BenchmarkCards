# Plutus-ben (Greek Financial Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: Plutus-ben (Greek Financial Evaluation Benchmark)

**Overview**: Plutus-ben is the first Greek financial evaluation benchmark addressing five core financial NLP tasks: numeric and textual named entity recognition, question answering, abstractive summarization, and topic classification, facilitating systematic and reproducible LLM assessments.

**Data Type**: text

**Domains**:
- Finance
- Natural Language Processing

**Languages**:
- Greek

**Similar Benchmarks**:
- FinBen
- INVESTORBENCH
- FinanceBench

**Resources**:
- [Resource](https://huggingface.co/collections/TheFinAI/plutus-benchmarking-greek-financial-llms-67bc718fb8d897c65f1e87db)

## 🎯 Purpose and Intended Users

**Goal**: To advance Greek financial NLP by providing a dedicated evaluation benchmark and datasets tailored to financial tasks in the Greek context.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Numeric Named Entity Recognition
- Textual Named Entity Recognition
- Question Answering
- Abstractive Summarization
- Topic Classification

**Limitations**: N/A

## 💾 Data

**Source**: Curated from real-world Greek financial documents, including annual reports and university exam questions.

**Size**: 2,400 samples

**Format**: JSON

**Annotation**: Manually annotated by expert native Greek speakers with deep financial and linguistic expertise.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Entity F1
- Accuracy
- Rouge-1

**Calculation**: Metrics are calculated based on standard definitions for precision, recall, and overlap comparisons.

**Interpretation**: Higher scores in Entity F1 indicate better entity recognition performance. Higher accuracy reflects correct prediction rates in classification tasks.

**Validation**: Data validation procedures included inter-annotator agreement metrics like F1 score and Cohen's Kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
