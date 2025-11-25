# MIRAGE

## 📊 Benchmark Details

**Name**: MIRAGE

**Overview**: MIRAGE is a Question Answering dataset specifically designed for Retrieval-Augmented Generation (RAG) evaluation, consisting of 7,560 curated instances mapped to a retrieval pool of 37,800 entries, enabling efficient and precise evaluation of both retrieval and generation tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/nlpai-lab/MIRAGE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the performance of Retrieval-Augmented Generation systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark may not be sufficiently challenging for oracle setups as some state-of-the-art models achieve high performance.

## 💾 Data

**Source**: Publicly available datasets including PopQA, TriviaQA, IfQA, DROP, and Natural Questions.

**Size**: 7,560 QA pairs

**Format**: JSON

**Annotation**: Automated labeling with human validation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Performance is measured using exact match accuracy between the system’s output and the correct answer label.

**Interpretation**: Model performance is assessed based on its ability to leverage external context and filter out noise.

**Validation**: Human validation through random sampling to ensure labeling accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis not explicitly mentioned.

**Potential Harm**: Risk of data contamination exists due to the use of publicly available datasets.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
