# LoCoV1 (Long-Context Retrieval Benchmark)

## 📊 Benchmark Details

**Name**: LoCoV1 (Long-Context Retrieval Benchmark)

**Overview**: LoCoV1 is a novel benchmark consisting of 12 tasks drawn from law, medicine, science, finance, corporate governance, government reports, and more, designed to measure long-context retrieval performance. It evaluates systems that need to process documents of up to 32K tokens, emphasizing reasoning across long spans of text.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare
- Legal
- Finance
- Government

**Languages**:
- English

**Similar Benchmarks**:
- BEIR

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to establish a reliable evaluation framework for long-context retrieval tasks in machine learning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Long-context Retrieval
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark draws tasks from real-world datasets spanning diverse domains including Tau Scrolls, QASPER, LongBench, and the Legal Case Reports corpus.

**Size**: 12 tasks with varying numbers of queries and documents

**Format**: JSON

**Annotation**: Tasks are expert-annotated.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Normalized Discounted Cumulative Gain at 10 (nDCG@10)

**Calculation**: nDCG@10 is calculated based on the ranking quality of the retrieval systems.

**Interpretation**: Higher nDCG@10 scores indicate better performance in returning relevant documents for given queries.

**Baseline Results**: M2-BERT achieves significantly higher scores compared to existing retrieval models, validating its effectiveness on the LoCoV1 benchmark.

**Validation**: Performance validation through comparative analysis with existing state-of-the-art models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for models to reinforce existing biases present in training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
