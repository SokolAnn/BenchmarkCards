# GutenQA

## 📊 Benchmark Details

**Name**: GutenQA

**Overview**: GutenQA is a benchmark consisting of 3000 question-answer pairs derived from 100 public domain narrative books sourced from Project Gutenberg. It aims to evaluate the impact of LumberChunker on retrieval in question answering tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/joaodsmarques/LumberChunker)
- [Resource](https://www.gutenberg.org/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of the LumberChunker method in segmenting documents for improved retrieval in question answering tasks.

**Target Audience**:
- ML Researchers
- Developers in Natural Language Processing

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 100 public domain narrative books from Project Gutenberg

**Size**: 3,000 question-answering pairs

**Format**: N/A

**Annotation**: Manually generated questions from texts using ChatGPT and filters for quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Recall
- DCG (Discounted Cumulative Gain)

**Calculation**: Metrics are calculated based on the retrieval performance of the LumberChunker method compared to baseline methods.

**Interpretation**: Higher DCG and Recall scores indicate better retrieval effectiveness and quality of question answering.

**Baseline Results**: LumberChunker outperformed all baseline methods on retrieval performance.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is sourced from public domain texts, ensuring no privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
