# SMARTFinRAG

## 📊 Benchmark Details

**Name**: SMARTFinRAG

**Overview**: SMARTFinRAG is an interactive evaluation platform specifically engineered for financial Retrieval-Augmented Generation (RAG) systems that dynamically accommodates various retrieval mechanisms, language models, and prompt strategies. It features a document-centric evaluation paradigm generating domain-specific question-answer pairs and provides an intuitive interface for visualizing performance metrics.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinQA
- FiQA
- FinBen
- PIXIU

**Resources**:
- [GitHub Repository](https://github.com/JonathanZha47/SMARTFinRAG)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for evaluating financial RAG systems, enabling continuous assessment with current information and facilitating research and practical applications in the finance sector.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Due to time and compute constraints, only a small subset (10 out of 317 QA pairs) was used for response evaluation.

## 💾 Data

**Source**: Financial documents, specifically 10-K filings from major companies.

**Size**: 317 question-answer pairs

**Format**: JSON

**Annotation**: Generated using an LLM to analyze document nodes and create diverse question types.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Hit Rate
- Mean Reciprocal Rank (MRR)
- Precision
- Recall
- Normalized Discounted Cumulative Gain (NDCG)
- Faithfulness
- Relevancy

**Calculation**: Metrics are calculated based on the ranking and relevance of retrieved documents and the alignment of generated responses with user queries.

**Interpretation**: Scores are compared against configurable thresholds to flag low-quality responses.

**Validation**: Evaluation conducted through automated generation of question-answer pairs from financial documents to ensure currency and domain relevance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
