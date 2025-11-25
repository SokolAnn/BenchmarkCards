# Sentence-path paired dataset

## 📊 Benchmark Details

**Name**: Sentence-path paired dataset

**Overview**: A novel dataset of sentence and commonsense knowledge path pairs (sentence-path pairs) created to train CoSe-Co, a generative model that produces commonsense inference paths conditioned on natural language sentences. The dataset is constructed by sampling multi-hop paths from a commonsense knowledge graph and retrieving & filtering semantically similar sentences from a sentence corpus to pair with each path.

**Data Type**: sentence-path pairs (text)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- CommonsenseQA (CSQA)
- ARC
- QASC
- OBQA
- OpenCSR (Open-ended CommonSense Reasoning)

**Resources**:
- [Resource](https://linktr.ee/coseco)
- [Resource](https://arxiv.org/abs/2206.05706)

## 🎯 Purpose and Intended Users

**Goal**: To create sentence-commonsense path pairs to train a generative CommonSense Contextualizer (CoSe-Co) that, given a natural language sentence, generates relevant commonsense inference paths for augmenting downstream tasks.

**Tasks**:
- Multi-Choice Question Answering
- Open-ended Commonsense Reasoning
- Paraphrase Generation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from a subset of Wikipedia (used as the sentence corpus) and ConceptNet knowledge graph (used as the source of commonsense paths).

**Size**: ≈290,000 sentence-path pairs (sampled ≈28M paths from ConceptNet; Wikipedia subset: ≈5M articles yielding ≈92.6M sentences; ConceptNet: ≈8 million nodes, 34 relations, ≈21 million links).

**Format**: N/A

**Annotation**: Automatically created: multi-hop paths sampled from ConceptNet; Apache Solr used to retrieve candidate Wikipedia sentences via templated queries (Q1 and Q2); retrieved sentences ranked by SBERT embedding cosine similarity; heuristics and filtering applied to retain top matches, producing paired sentence-path data.

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU Score for relevance)
- Cosine similarity of SBERT embeddings for dataset pair relevance
- Diversity metric (complement of fractional entity overlap among generated paths)
- Novelty measurement (fraction of entities in generated paths not present in training paths)
- Human evaluation (pairwise comparison of generated paths)
- Downstream task evaluation (Multi-Choice QA on CommonsenseQA, OpenCSR on ARC/QASC/OBQA, Paraphrase Generation on MRPC)

**Metrics**:
- BLEU Score
- Cosine similarity
- Diversity (1 - intersection-over-union of path entities)
- Novelty (percentage of novel entities)
- Accuracy
- Hits@K
- Recall@K
- BLEU-4
- METEOR
- ROUGE-L
- CIDEr
- SPICE

**Calculation**: Relevance: BLEU score computed by treating each triple in generated and ground-truth paths as unigrams and computing BLEU. Diversity: for top-5 sampled paths per sentence, compute pairwise fractional overlap (intersection over union of entities); diversity = 1 - average overlap. Novelty: fraction of entities in generated path not present in any training path, averaged. Leakage check: n-gram overlap between CSQA questions and training sentences. Hits@K: whether generated and ground truth answer sets have non-empty intersection. Recall@K: fraction of predicted answers matching at least one ground truth answer.

**Interpretation**: Higher BLEU indicates greater relevance to ground-truth paths. Higher diversity score (closer to 1) indicates more diverse generated paths. Higher novelty indicates more entities not present in training data. Higher Hits@K/Recall@K/Accuracy indicate better downstream task performance. The paper highlights a trade-off between relevance and diversity and prefers methods balancing both (their 'diverse-path search').

**Baseline Results**: Multi-Choice QA (CommonsenseQA, IHtest): CoSe-Co (Ours) 72.87% (±0.31) vs PGQA 71.19% and QA-GNN 72.29% (reported in Table 2). OpenCSR (Hits@50): ARC - T5-base 71.01, +CoSe-Co Paths 69.23, +CoSe-Co Concepts 73.37; QASC - T5-base 53.47, +CoSe-Co Paths 56.44, +CoSe-Co Concepts 57.43; OBQA - T5-base 37.88, +CoSe-Co Paths 45.45, +CoSe-Co Concepts 42.42 (reported in Table 4). Paraphrase generation (MRPC): T5-base BLEU-4 43.10 vs +CoSe-Co Paths 44.50 (reported in Table 5).

**Validation**: Leakage analysis via n-gram overlap with CSQA test (1-gram 0.15, 2-gram 0.07, 3-gram 0.002, 4-gram 0.00) indicating negligible leakage; cosine similarity (SBERT) between paths and paired sentences averaged 0.783 indicating semantic relatedness; human evaluation with 150 CSQA samples compared CoSe-Co and PGQA (CoSe-Co preferred in 62 of 100 non-neutral comparisons).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset derived from publicly available Wikipedia corpus and ConceptNet and authors state it does not contain information/text that could potentially lead to risk impacts.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
