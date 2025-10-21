# COMBO: A Complete Benchmark for Open KG Canonicalization

## 📊 Benchmark Details

**Name**: COMBO: A Complete Benchmark for Open KG Canonicalization

**Overview**: COMBO is a complete benchmark for open KG canonicalization that provides gold annotations for entity-level noun phrase canonicalization (NPC-E), relation-phrase canonicalization (RPC), and ontology-level noun phrase canonicalization (NPC-O). Compared with existing datasets, COMBO additionally provides gold canonicalization for relation phrases, gold ontology-level canonicalization for noun phrases, as well as source sentences from which triples are extracted. The paper also proposes metrics for evaluating each type of canonicalization and releases the dataset, baselines, and evaluation scripts.

**Data Type**: text (open KG triples: subject, relation, object) with source sentences

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- ReVerb-Base
- ReVerb-Ambiguous
- ReVerb45K
- CanonicNELL

**Resources**:
- [GitHub Repository](https://github.com/jeffchy/COMBO/tree/main)
- [Resource](https://arxiv.org/abs/2302.03905)
- [Resource](https://stanfordnlp.github.io/CoreNLP/)
- [GitHub Repository](https://github.com/SuLab/WikidataIntegrator)
- [Resource](https://www.wikidata.org/wiki/Q5)
- [Resource](https://www.wikidata.org/wiki/Property:P19)

## 🎯 Purpose and Intended Users

**Goal**: Provide a complete benchmark and evaluation metrics for open KG canonicalization covering entity-level NP canonicalization (NPC-E), ontology-level NP canonicalization (NPC-O), and relation-phrase canonicalization (RPC); construct the dataset and provide baselines and evaluation scripts.

**Target Audience**:
- ML Researchers
- Model Developers
- NLP Researchers

**Tasks**:
- Entity-level Noun Phrase Canonicalization (NPC-E)
- Relation Phrase Canonicalization (RPC)
- Ontology-level Noun Phrase Canonicalization (NPC-O)

**Limitations**: The size of the dataset (18K triples) is relatively small compared to previous datasets. The work performs clustering for the three subtasks and evaluates them independently, although canonicalization of head NP, tail NP and RP are closely correlated; jointly canonicalization and evaluation is left as future work.

## 💾 Data

**Source**: Constructed from the revised Wiki20 dataset (Wikipedia aligned with Wikidata) for source sentences and gold NPC-E, Stanford OpenIE extractions on Wiki20 sentences to obtain relation phrases, Wikidata SPARQL queries to obtain ontology-level classes (NPC-O), and human revision/inspection for RP correction and validation.

**Size**: 18,000 triples; 16,500 unique noun phrases; 3,200 distinct relation phrases; 13,800 NPC-E clusters; 2,946 NPC-O (ontological) clusters; 79 RPC (relation) clusters; average triple length 8.12 words; 100% of triples have source sentence context.

**Format**: JSON (the paper describes forming 79 json files during annotation and shows JSON-like data examples)

**Annotation**: NPC-E: using Wiki20 entity linking (distant supervision) as gold; RPC: Stanford OpenIE extractions followed by per-instance manual human revision and standardization; NPC-O: obtained by querying Wikidata via SPARQL and applying pattern-based corrections; annotators were paid and cross-checked (human revision described in Appendix B).

## 🔬 Methodology

**Methods**:
- Automated clustering evaluation using macro, micro and pairwise clustering metrics
- Jaccard-based evaluation (Jg!p and Jp!g) for overlapping NPC-O clusters
- Dev/test split-based threshold tuning (HAC distance threshold tuned on dev set)

**Metrics**:
- Macro Precision
- Macro Recall
- Micro Precision
- Micro Recall
- Pairwise Precision
- Pairwise Recall
- Jaccard index (used in Jg!p and Jp!g for overlapping NPC-O clusters)

**Calculation**: Classic clustering metrics (macro, micro, pairwise) compare gold and predicted non-overlapping clusters; for RPC only micro and pairwise metrics are used; for NPC-O (overlapping gold clusters) use macro/pairwise and a modified micro metric if predicted clusters are non-overlapping, and Jg!p and Jp!g (average best-match Jaccard) when predicted clusters are overlapping. HAC distance threshold is tuned on the dev set (20% dev, 80% test).

**Interpretation**: Higher metric values indicate better canonicalization quality. HAC distance thresholds are selected on the dev set by maximizing the average of the chosen metrics. Different metrics are used depending on whether gold/predicted clusters are overlapping or non-overlapping.

**Baseline Results**: PLM-based baselines outperform previous methods in most cases. Example results (averaged metrics): BERT-base: NPC-E (Subject) 86.93, NPC-E (Object) 86.91, RPC 54.47; BERT-base with triple-level pretraining (Bert-base-triple) RPC 58.45. Full detailed results are provided in Tables 5, 8 and 9 of the paper.

**Validation**: Data split into dev (20%) and test (80%); HAC distance threshold tuned on the dev set; deterministic methods run once and methods involving random initialization run multiple times (four) as described.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias

**Potential Harm**: The authors note that using pretrained language models as encoders can potentially create biased clustering results and that how to de-bias PLM embeddings is worth further investigation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Wiki20 is under the MIT License; Wikidata is under the Creative Commons CC0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
