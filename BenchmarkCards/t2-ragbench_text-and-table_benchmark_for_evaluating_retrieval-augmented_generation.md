# T2-RAGBench (Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: T2-RAGBench (Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation)

**Overview**: T2-RAGBench is a benchmark comprising 32,908 question-context-answer triples, designed to evaluate Retrieval-Augmented Generation methods on real-world financial data involving both text and tables.

**Data Type**: question-context-answer triples

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinQA
- ConvFinQA
- TAT-DQA

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate existing Retrieval-Augmented Generation methods on text-table retrieval and numerical reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Numerical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Existing financial documents and QA datasets restructured for context independence.

**Size**: 32,908 triples

**Format**: CSV

**Annotation**: Reformulated by language models with qualitative checks by financial experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Number Match

**Calculation**: Calculated based on the relevance of the retrieved documents against the ground truth.

**Interpretation**: Scores indicate the effectiveness of RAG methods in retrieving accurate financial data.

**Baseline Results**: N/A

**Validation**: Expert validation of question reformulation and numerical accuracy.

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
