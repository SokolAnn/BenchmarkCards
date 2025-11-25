# FreshStack

## 📊 Benchmark Details

**Name**: FreshStack

**Overview**: FreshStack is a holistic framework for constructing realistic information retrieval (IR) evaluation benchmarks by sourcing community-asked questions and answers. It generates challenging datasets aimed at improving retrieval systems and retrieval-augmented generation (RAG) capabilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CQADupstack
- CodeSearchNet
- COIR
- Neural Code Search
- SWE-Bench

**Resources**:
- [Resource](https://fresh-stack.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the construction of challenging datasets for evaluating retrieval systems realistically.

**Target Audience**:
- ML Researchers
- Information Retrieval Researchers
- Systems Developers

**Tasks**:
- Information Retrieval
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Community-asked questions and answers sourced from Stack Overflow, along with code snippets and documents from GitHub repositories.

**Size**: 5 datasets on niche topics

**Format**: N/A

**Annotation**: Nuggets are generated using GPT-4o on community-asked questions and answers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- α-nDCG@10
- Coverage@20
- Recall@50

**Calculation**: Metrics are calculated based on retrieval and RAG performance on the constructed datasets.

**Interpretation**: Higher α-nDCG@10 indicates better relevance and diversity in the retrieved documents.

**Baseline Results**: Existing retrieval models show significant headroom for improvement in retrieval accuracy compared to oracle performance.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Robustness**
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data sourced from Stack Overflow and GitHub repositories, following their respective licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
