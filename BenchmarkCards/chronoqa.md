# ChronoQA

## 📊 Benchmark Details

**Name**: ChronoQA

**Overview**: ChronoQA is a benchmark dataset for Chinese question answering focused on evaluating temporal reasoning in Retrieval-Augmented Generation (RAG) systems. It contains 5,176 questions derived from over 300,000 news articles published between 2019 and 2024, covering absolute, aggregate, and relative temporal types with both explicit and implicit time expressions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- Natural Questions
- TriviaQA
- CRAG
- DomainRAG

**Resources**:
- [GitHub Repository](https://github.com/czy1999/ChronoQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate temporal-sensitive RAG systems and enhance performance in handling time-sensitive questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from over 300,000 news articles published between 2019 and 2024.

**Size**: 5,176 questions

**Format**: JSON, CSV

**Annotation**: Generated via a robust multi-stage pipeline that includes LLM-based extraction, structured question synthesis, and rigorous validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mean Average Precision (MAP)

**Calculation**: Metrics are calculated based on the performance of models on the dataset.

**Interpretation**: Higher scores indicate better performance in retrieving temporally relevant information.

**Baseline Results**: N/A

**Validation**: Multi-stage validation process combining rule-based checks, LLM evaluations, and manual verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
