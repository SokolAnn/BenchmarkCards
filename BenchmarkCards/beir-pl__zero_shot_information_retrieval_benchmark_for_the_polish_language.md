# BEIR-PL: Zero Shot Information Retrieval Benchmark for the Polish Language

## 📊 Benchmark Details

**Name**: BEIR-PL: Zero Shot Information Retrieval Benchmark for the Polish Language

**Overview**: We translated all accessible open IR datasets into Polish, and we introduced the BEIR-PL benchmark – a new benchmark which comprises 13 datasets, facilitating further development, training and evaluation of modern Polish language models for IR tasks.

**Data Type**: question-passage pairs (queries, passages, relevance judgments / qrels)

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- Polish

**Similar Benchmarks**:
- BEIR
- Mr. TyDi
- MS MARCO
- MTEB Benchmark

**Resources**:
- [Resource](https://huggingface.co/clarin-knext)
- [Resource](http://huggingface.co)
- [Resource](https://www.elastic.co/)
- [Resource](https://www.sbert.net/)

## 🎯 Purpose and Intended Users

**Goal**: Our main goal was to create a large scale benchmark dataset for IR in the Polish language, which is especially aimed at zero-shot approaches.

**Target Audience**:
- Research community
- ML Researchers
- Information Retrieval Researchers
- Model Developers

**Tasks**:
- Passage Retrieval
- Passage Re-ranking
- Zero-shot Information Retrieval evaluation

**Limitations**: Translations were produced using Google Translate and while selective manual inspection and automatic LaBSE similarity checks showed most translations were adequate to the IR task, translations are not perfect; errors were particularly noticed in the translation of Named Entities and incorrect phrasing. Full manual verification of the entire resource was not performed due to scale.

## 💾 Data

**Source**: Translated the original BEIR benchmark datasets into Polish using Google Translate; comprises 13 datasets and retains BEIR-compatible format (queries, corpus, qrels).

**Size**: Varies by dataset; corpus sizes listed in Table 1 (examples: MSMARCO: 8.8M documents; TREC-COVID: 171K; NFCorpus: 3.6K; NQ: 2.68M; HotpotQA: 5.2M; FiQA: 57K; ArguAna: 9K; Touche-2020: 382K; CQADupstack: 547K; Quora: 523K; DBPedia: 4.63M; SciDocs: 25K; SciFact: 5K).

**Format**: Queries and corpus: JSONL; qrels: TSV

**Annotation**: Uses original BEIR relevance judgments (qrels) retained; translations produced by Google Translate. Selective manual evaluation: 100 random queries/passages assessed (semantic setting by a researcher; strict setting by a professional linguist). Automated LaBSE similarity scores were also used for validation.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics (MRR, nDCG, Recall)
- Model-based evaluation comparing lexical BM25, unsupervised dense bi-encoder (ICT with HerBERT), multilingual LaBSE, multilingual mMiniLM, HerBERT-based rerankers, plT5-based rerankers, ColBERT late-interaction model
- Two-stage retrieval with BM25 first-stage and neural rerankers second-stage
- Evaluation on BEIR-PL test splits and PolEval 2022 Passage Retrieval competition datasets

**Metrics**:
- Mean Reciprocal Rank (MRR@k)
- Normalized Discounted Cumulative Gain (nDCG@k)
- Recall (Recall@k)

**Calculation**: Metrics computed using standard IR definitions as described in Appendix A: MRR@k is the mean reciprocal rank of the first relevant passage; nDCG@k computed using DCG with binary gain (Gain = 1 if passage relevant, 0 otherwise); Recall@k is proportion of relevant documents retrieved within top-k.

**Interpretation**: Higher MRR, nDCG and Recall indicate better retrieval performance. The authors note BEIR-PL and original BEIR are heterogeneous and recommend examining results of individual datasets rather than relying solely on overall averages.

**Baseline Results**: BM25 baseline on BEIR-PL reported in Table 3 (examples: MSMARCO NDCG@10 PL = 41.9 vs EN = 47.7; Recall@100 MSMARCO PL = 34.6 vs EN = 45.0). Full model comparisons (BM25, ICT, LaBSE, mMiniLM, HerBERT variants, T5 variants, ColBERT) reported in Tables 4-6.

**Validation**: Validation included selective manual evaluation of 100 random queries/passages (strict by professional linguist; semantic by researcher), automated LaBSE similarity checks, and testing trained models on PolEval 2022 Passage Retrieval datasets across three domains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
