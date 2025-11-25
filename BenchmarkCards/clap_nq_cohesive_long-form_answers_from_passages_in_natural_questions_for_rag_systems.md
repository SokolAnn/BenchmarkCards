# CLAP NQ (Cohesive Long-form Answers from Passages in Natural Questions for RAG systems)

## 📊 Benchmark Details

**Name**: CLAP NQ (Cohesive Long-form Answers from Passages in Natural Questions for RAG systems)

**Overview**: CLAP NQ is a benchmark Long-form Question Answering dataset for the full RAG pipeline, featuring long answers with grounded gold passages from Natural Questions (NQ). It includes 4946 questions designed for Retrieval Augmented Generation (RAG) systems and assesses their ability to provide coherent, concise, and complete answers based on the context of the gold passages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Natural Questions
- SQuAD
- ELI5

**Resources**:
- [GitHub Repository](https://github.com/primeqa/clapnq)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of Retrieval Augmented Generation (RAG) systems in providing accurate and cohesive long-form answers based on grounded passages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is created from the Natural Questions dataset focusing on questions that have long answers without short answers.

**Size**: 4,946 questions

**Format**: JSON

**Annotation**: Annotated by skilled in-house annotators using two rounds of review for high quality non-consecutive grounded answers.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- RougeL
- Recall

**Calculation**: Metrics are calculated based on the generated responses compared to the gold answers using precision, recall, and F1 scores for RougeL.

**Interpretation**: Higher RougeL and recall scores indicate better performance in maintaining the coherence and completeness of the answers.

**Baseline Results**: Performance metrics shown from State-of-the-Art models and comparison against gold passage results are included in the paper.

**Validation**: The benchmark was validated through human evaluation and comparison of model responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
