# Multi-CPR: A Multi Domain Chinese Dataset for Passage Retrieval

## 📊 Benchmark Details

**Name**: Multi-CPR: A Multi Domain Chinese Dataset for Passage Retrieval

**Overview**: We present Multi-CPR, a novel multi-domain Chinese dataset for passage retrieval collected from three different domains (E-commerce, Entertainment video and Medical). Each domain contains around one million passages and human-annotated query-passage related pairs. The dataset is intended to benchmark Chinese passage retrieval in specific domains and to support further research.

**Data Type**: text (query-passage pairs)

**Domains**:
- Information Retrieval
- Natural Language Processing
- E-commerce
- Entertainment
- Medical

**Languages**:
- Chinese

**Similar Benchmarks**:
- MS MARCO
- DuReader
- Sogou-QCL

**Resources**:
- [GitHub Repository](https://github.com/Alibaba-NLP/Multi-CPR)
- [Resource](https://doi.org/10.1145/3477495.3531736)
- [Resource](https://arxiv.org/abs/2203.03367)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, multi-domain Chinese passage retrieval dataset (covering E-commerce, Entertainment video and Medical) to benchmark Chinese passage retrieval in specific domains and to advance future studies.

**Target Audience**:
- Academic researchers
- Industry practitioners

**Tasks**:
- Passage Retrieval
- Passage Reranking

**Limitations**: N/A

## 💾 Data

**Source**: Queries and passages sampled from search logs of Alibaba Group search systems: Taobao search (E-commerce), Youku search (Entertainment video), Quark search (Medical). A converted general-domain dataset is constructed from DuReader (Baidu). Positive query-passage pairs are human-annotated.

**Size**: E-commerce: 100,000 train queries, 1,000 test queries, 1,002,822 passages; Entertainment video: 100,000 train queries, 1,000 test queries, 1,000,000 passages; Medical: 99,999 train queries, 1,000 test queries, 959,526 passages; General-domain (converted from DuReader): 245,897 train queries.

**Format**: N/A

**Annotation**: Manual annotation by human annotators. Each sample annotated by at least 5 independent annotators; samples with >80% agreement retained. Annotators passed a pre-annotation test (100–200 samples) reviewed by expert examiners. Expert examiners sample 20% of annotators' data and require an acceptability ratio >=95%.

## 🔬 Methodology

**Methods**:
- Human annotation for relevance labels
- Baseline model evaluation (BM25, Doc2Query, DPR variants)
- Dense retrieval evaluation (DPR and variants)
- Retrieval-then-rerank experiments with BERT reranker
- Automated metric evaluation

**Metrics**:
- Mean Reciprocal Rank at 10 (MRR@10)
- Recall at 1000 (Recall@1000)

**Calculation**: Following previous work, retrieval performance is evaluated by MRR@10 and Recall@1000. For passage reranking, results are reported using MRR@10. Reranker is trained with a contrastive objective aggregating one positive and multiple negatives per query (contrastive loss formula provided in paper).

**Interpretation**: Higher MRR@10 and Recall@1000 indicate better retrieval performance. The authors interpret relative improvements in these metrics (e.g., in-domain DPR vs. general-domain DPR, and reranking improvements) as evidence of the value of in-domain labeled data and of reranking.

**Baseline Results**: Key results reported in the paper (Table 5 & Table 6): Sparse baselines: BM25 MRR@10 — E-commerce 0.2253, Entertainment video 0.2252, Medical 0.1869; Doc2Query MRR@10 — E-commerce 0.2385, Entertainment video 0.2378, Medical 0.2095. Dense baselines: DPR (General BERT) MRR@10 — E-commerce 0.2106, Entertainment video 0.1950, Medical 0.2133. DPR-1 (In-domain BERT) MRR@10 — E-commerce 0.2704, Entertainment video 0.2537, Medical 0.3270. DPR-2 (In-domain BERT-CT) MRR@10 — E-commerce 0.2894, Entertainment video 0.2627, Medical 0.3388. Average MRR@10 over three datasets: BM25 0.2124, DPR-1 0.2837. Reranking (Table 6): BM25 + BERT reranker MRR@10 — E-commerce 0.2784, Entertainment video 0.3212, Medical 0.2673; DPR-1 + BERT reranker MRR@10 — E-commerce 0.3624, Entertainment video 0.3772, Medical 0.3855.

**Validation**: Annotation quality control: annotators pass pre-annotation tests reviewed by experts; at least 5 annotators per sample and samples with >80% agreement are retained. Experts check 20% of annotators' data and require an acceptability ratio >=95% (annotators revise if below threshold).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
