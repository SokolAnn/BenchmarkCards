# FTRACE

## 📊 Benchmark Details

**Name**: FTRACE

**Overview**: We introduce the problem of fact tracing: identifying which training examples taught a language model to generate a particular factual assertion, and present the first quantitative benchmark to evaluate this. We construct two evaluation datasets (FTRACE-TREX and FTRACE-SYNTH) containing ground-truth proponents for facts and a tractable reranking evaluation procedure to compare training data attribution methods (gradient-based and embedding-based) and an information retrieval baseline (BM25).

**Data Type**: text (masked cloze-style question-answer pairs / masked inputs and outputs with fact annotations)

**Domains**:
- Natural Language Processing
- Information Retrieval

**Similar Benchmarks**:
- TREx
- LAMA
- BEIR

**Resources**:
- [GitHub Repository](https://github.com/ekinakyurek/influence)
- [Resource](https://huggingface.co/datasets/ekinakyurek/ftrace)
- [Resource](https://arxiv.org/abs/2205.11482)

## 🎯 Purpose and Intended Users

**Goal**: To provide a quantitative benchmark and datasets for the task of fact tracing: tracing language models' assertions back to the training examples that provided evidence for those predictions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Fact Tracing
- Training Data Attribution
- Retrieval / Reranking of proponent training examples

**Limitations**: Experiments focus on a single representative language model (MT5-base); results using the candidate-set reranking evaluation only upper-bound full retrieval performance; ground truth labels in FTRACE-TREX are extracted from TREx where the fact annotations are semi-automatically annotated and can have labeling errors; the FTRACE dataset includes content from Wikipedia which may not have been vetted for factual accuracy.

**Out of Scope Uses**:
- Using FTRACE as a reliable source of factual information rather than as an evaluation tool (the authors state FTRACE's role is as an evaluation tool, not as a reliable source of information).

## 💾 Data

**Source**: FTRACE-TREX: attribution set constructed from TREx (Elsahar et al., 2018) sentences and query set constructed from LAMA (Petroni et al., 2019). FTRACE-SYNTH: synthetic dataset with made-up entities and relations (relations borrowed from TREx and paraphrased).

**Size**: FTRACE-TREX: Attribution set: 1,560,453 masked examples; Query set: 31,479 examples; Unique Facts (as reported): 552,381 (attribution) and 31,479 (query). FTRACE-SYNTH: Attribution corpus: 3,190,000 masked examples derived from 50,000 individual facts; Query set: 10,000 examples (5,000 facts with 2 surface forms each); 5,000 synthetic entities.

**Format**: Masked cloze-style examples: masked inputs and outputs with fact annotations (cloze-style masked language modeling examples).

**Annotation**: FTRACE-TREX: ground-truth proponents identified by matching TREx sentences that express the same fact and converting sentences into cloze-style masked examples (mask_sub and mask_obj). FTRACE-SYNTH: ground-truth proponents are known by construction because synthetic facts and their attribution examples are created programmatically.

## 🔬 Methodology

**Methods**:
- Gradient-based attribution (TracIn and related gradient-based methods)
- Embedding-based attribution (EMBED: intermediate layer representations with cosine similarity)
- BM25 information retrieval baseline
- Reranking evaluation with a candidate set (union of all true proponents, top-100 BM25 retrievals, 100 examples sharing same target output, and 100 random examples)

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Recall@10
- Precision@10

**Calculation**: MRR is calculated as (1/|Q|) * sum_{q in Q} 1 / rank_q where rank_q is the rank of the first true proponent for query q within the candidate set. The candidate set for each query is the union of: all true proponents P(z_query), top-100 BM25(z_query), 100 examples with same output as the query, and 100 random samples. Recall@10 and Precision@10 are computed over the same candidate set.

**Interpretation**: Higher MRR/Recall@10/Precision@10 indicate better ability to retrieve ground-truth proponents. MRR on the defined candidate set is an upper-bound on MRR over the full attribution set because the candidate set includes all true proponents but fewer distractors.

**Baseline Results**: FTRACE-TREX (Finetune-learned slice, sentence-level retrieval, averages over seeds): BM25: MRR 77.55 ±1.50, Recall@10 60.89 ±2.31. TRACIN (Finetuned): MRR 48.56 ±4.40, Recall@10 56.02 ±0.67. TRACIN (Pretrained): MRR 62.38 ±1.99, Recall@10 57.54 ±1.25. EMBED (Finetuned): MRR 64.29 ±1.32, Recall@10 57.89 ±1.38. TRACIN+EMBED (Finetuned): MRR 58.52 ±3.83, Recall@10 61.72 ±0.08. FTRACE-SYNTH (Finetuned, Finetune-learned slice): BM25: MRR 87.69 ±1.71, Precision@10 52.02 ±2.65, Recall@10 4.20 ±0.21. TRACIN (Finetuned): MRR 100.00 ±0.00, Precision@10 99.50 ±0.14, Recall@10 8.02 ±0.01. EMBED (Finetuned): MRR 99.58 ±0.24, Precision@10 97.12 ±0.53, Recall@10 7.83 ±0.04. TRACIN+EMBED (Finetuned): MRR 100.00 ±0.00, Precision@10 98.07 ±0.18, Recall@10 7.91 ±0.01.

**Validation**: Evaluation uses a reranking candidate set that includes all ground-truth proponents to ensure they are retrievable; experiments report results on 'Finetune-learned' (FL) queries where the model failed before fine-tuning but succeeded after fine-tuning to mitigate saturation effects. A synthetic dataset (FTRACE-SYNTH) is used to control for novelty and lexical overlap and validate attribution methods under controlled conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Governance
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Uncertain data provenance
- **Governance**: Lack of testing diversity
- **Societal Impact**: Impact on affected communities

**Potential Harm**: ['It is possible that by redistributing this content we will propagate misinformation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
