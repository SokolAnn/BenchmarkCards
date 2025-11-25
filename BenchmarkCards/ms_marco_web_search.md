# MS MARCO Web Search

## 📊 Benchmark Details

**Name**: MS MARCO Web Search

**Overview**: MS MARCO Web Search is the first large-scale information-rich web dataset, featuring millions of real clicked query-document labels, aimed at facilitating research in various areas of information retrieval and machine learning.

**Data Type**: query-document pairs

**Domains**:
- Information Retrieval

**Languages**:
- English

**Similar Benchmarks**:
- MS MARCO
- Natural Questions

**Resources**:
- [GitHub Repository](https://github.com/microsoft/MS-MARCO-Web-Search)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale dataset for research on web information retrieval and facilitate innovations in both machine learning and information retrieval system research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Information Retrieval Researchers

**Tasks**:
- Benchmarking retrieval systems
- Testing embedding models

**Limitations**: N/A

## 💾 Data

**Source**: ClueWeb22 corpus and Bing search engine logs

**Size**: 10 billion web pages and 10 million unique queries

**Format**: N/A

**Annotation**: Labeled based on user clicks from search engine logs

## 🔬 Methodology

**Methods**:
- Evaluation of embedding models
- Quality assessment of retrieval systems

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Recall

**Calculation**: Metrics calculated based on the quality of retrieval results and the number of relevant documents returned.

**Interpretation**: Higher MRR and recall indicate better model performance.

**Baseline Results**: Initial benchmark results provided for various embedding models.

**Validation**: Benchmark validated using comparison with existing state-of-the-art models and systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Queries containing personally identifiable information and offensive content were removed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
