# InsQABench (Insurance Question Answering Benchmark)

## 📊 Benchmark Details

**Name**: InsQABench (Insurance Question Answering Benchmark)

**Overview**: InsQABench is a benchmark dataset for the Chinese insurance sector structured into three categories: Insurance Commonsense Knowledge, Insurance Structured Database, and Insurance Unstructured Documents, reflecting real-world insurance question-answering tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://arxiv.org/abs/2501.10943)

## 🎯 Purpose and Intended Users

**Goal**: To establish a comprehensive benchmark dataset for insurance-related question answering.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Commonsense Question Answering
- Database Question Answering
- Clause Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collection of insurance-related information from various insurance company official websites and public online resources.

**Size**: 44,000 questions

**Format**: N/A

**Annotation**: QA pairs generated through a combination of automated methods and manual input from domain experts.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning (SFT)
- SQL-ReAct
- RAG-ReAct

**Metrics**:
- Accuracy
- Precision
- F1 Score
- ROUGE-L

**Calculation**: Evaluation metrics calculated comparing model output against benchmark standards.

**Interpretation**: Higher scores indicate a more accurate and professional response related to insurance questions.

**Validation**: Two-stage evaluation assessing model performance before and after fine-tuning on benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
