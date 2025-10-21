# IRSC: A Zero-shot Evaluation Benchmark for Information Retrieval through Semantic Comprehension in Retrieval-Augmented Generation Scenarios

## 📊 Benchmark Details

**Name**: IRSC: A Zero-shot Evaluation Benchmark for Information Retrieval through Semantic Comprehension in Retrieval-Augmented Generation Scenarios

**Overview**: The IRSC benchmark aims to evaluate the performance of embedding models in multilingual Retrieval-Augmented Generation (RAG) tasks across five retrieval tasks: query retrieval, title retrieval, part-of-paragraph retrieval, keyword retrieval, and summary retrieval. It introduces new metrics, the Similarity of Semantic Comprehension Index (SSCI) and the Retrieval Capability Contest Index (RCCI), to address the need for comprehensive testing and effective comparison methods for embedding models in RAG scenarios.

**Data Type**: query-paragraph pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MIRACL
- RGB
- MTEB
- MKQA

**Resources**:
- [GitHub Repository](https://github.com/Jasaxion/IRSC_Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing the performance of embedding models in RAG tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Query Retrieval
- Title Retrieval
- Part-of-Paragraph Retrieval
- Keyword Retrieval
- Summary Retrieval

**Limitations**: The benchmark primarily focuses on English and Chinese, which limits its applicability to other languages.

## 💾 Data

**Source**: Datasets used include MsMARCO, XQuAD, Xtreme, MLQA, zhihu, New-Title-Chinese, Arxiv-Abstract, Sci-Docs, nfcorpus, AG News, and XSum.

**Size**: 5,000 query-content pairs for each of the five tasks.

**Format**: Various formats depending on the dataset.

**Annotation**: Crowdsourced and expert-annotated based on existing benchmark standards.

## 🔬 Methodology

**Methods**:
- Standard retrieval metrics
- New evaluation metrics (SSCI and RCCI)

**Metrics**:
- nDCG@10
- MRR@10
- MAP@10
- precision@3
- recall@10
- Similarity of Semantic Comprehension Index (SSCI)
- Retrieval Capability Contest Index (RCCI)

**Calculation**: Standard metrics are calculated based on the ranking of the retrieved documents. SSCI and RCCI are calculated based on the difference in semantic understanding and retrieval capabilities between models.

**Interpretation**: Higher values in metrics denote better performance in retrieval capabilities. SSCI measures consistency of semantic understanding across queries.

**Baseline Results**: BGE-M3 model outperformed others across all tasks in various metrics.

**Validation**: Results compared against ground truth using a standardized evaluation approach.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes multilingual aspects but does not provide extensive demographic breakdowns.

**Potential Harm**: Potential performance gaps in cross-lingual retrieval tasks may lead to inaccurate retrieval results.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
