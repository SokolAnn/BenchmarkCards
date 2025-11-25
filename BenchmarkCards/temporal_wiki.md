# TEMPORAL WIKI

## 📊 Benchmark Details

**Name**: TEMPORAL WIKI

**Overview**: We introduce TEMPORAL WIKI, a lifelong benchmark for ever-evolving LMs that utilizes the difference between consecutive snapshots of English Wikipedia and English Wikidata for training and evaluation, respectively. The benchmark hence allows researchers to periodically track an LM’s ability to retain previous knowledge and acquire updated/new knowledge at each point in time.

**Data Type**: text (Wikipedia diff sentences) and graph (Wikidata factual triples)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- KILT
- LAMA
- TimeLMs

**Resources**:
- [Resource](https://commons.wikimedia.org/contributions)
- [Resource](https://arxiv.org/abs/2204.14211)

## 🎯 Purpose and Intended Users

**Goal**: To provide a lifelong benchmark (TEMPORAL WIKI) that can be used to automatically train and evaluate ever-evolving language models on each English Wikipedia and English Wikidata snapshot update, enabling periodic tracking of an LM's ability to retain previous knowledge (stability) and acquire updated/new knowledge (plasticity).

**Target Audience**:
- ML Researchers

**Tasks**:
- Language Modeling
- Question Answering
- Slot Filling

**Limitations**: Each Wikipedia and Wikidata update does not ensure an actual update of real-world knowledge. Knowledge deletion is not covered in this work (deleted information is not utilized).

## 💾 Data

**Source**: Consecutive snapshots of English Wikipedia (for training TWIKI-DIFFSETS) and consecutive snapshots of English Wikidata (for evaluation TWIKI-PROBES), using monthly Wikimedia dumps.

**Size**: Training: Wikipedia snapshots (per snapshot) ~6.3M articles and ~4.6B-4.7B tokens; TWIKI-DIFFSETS (per two-snapshot diff) 299.2K–328.9K articles and 346.45M–376.09M tokens (Table 1). Evaluation: a single Wikidata snapshot contains 93 million distinct entities (~2.8 billion factual instances); after categorization and quality control TWIKI-PROBES per month are reduced to the aligned/filtered counts shown in Table 2 (examples: for 08-09: UNCHANGED 6,935 and CHANGED 1,776 after heuristic filtering). The constructed benchmark covers 08.2021 to 12.2021 in this work.

**Format**: N/A

**Annotation**: Automatically generated (no human annotation) via algorithmic differencing of consecutive Wikipedia snapshots and algorithmic categorization of Wikidata triples, followed by automated alignment and heuristic filtering.

## 🔬 Methodology

**Methods**:
- Intrinsic evaluation (perplexity on training corpora: TWIKI-DIFFSETS and NON-TWIKI-DIFFSETS)
- Extrinsic evaluation (zero-shot perplexity on TWIKI-PROBES categorized into UNCHANGED and CHANGED)
- Light-tuning followed by evaluation (500-instance light-tuning sampled from Wikidata)
- Comparative evaluation of continual learning baselines (FULL, DIFF, RECADAM, MIX-REVIEW, LoRA, K-Adapter)

**Metrics**:
- Perplexity
- F1 Score
- Training Time (hours)

**Calculation**: Perplexity measured on proper noun tokens determined by a POS tagger. For intrinsic evaluation, 10,000 input instances of fixed length 512 are sampled from TWIKI-DIFFSETS and NON-TWIKI-DIFFSETS; perplexity on proper noun tokens is computed. For extrinsic evaluation on TWIKI-PROBES, perplexities of UNCHANGED and CHANGED factual instances are measured and averaged with equal weight to assess stability and plasticity. Light-tuning uses 500 sampled Wikidata instances (no overlap) for one epoch before evaluation.

**Interpretation**: Lower perplexity indicates better performance. The average of UNCHANGED and CHANGED perplexities is used to equally weigh stability (retaining previous knowledge) and plasticity (acquiring new knowledge). F1 Score is reported for light-tuned models on TWIKI-PROBES.

**Baseline Results**: Baseline results are provided in Tables 3, 5, and 6. Key reported findings: DIFF and continual learning methods improve perplexity on CHANGED instances compared to INITIAL; DIFF suffers more catastrophic forgetting on UNCHANGED while continual learning methods mitigate forgetting. K-Adapter shows the most robust overall performance and is reported to be ~12 times more computationally efficient than FULL.

**Validation**: Quality control and validation steps include: (1) alignment between Wikidata factual instances and Wikipedia articles via mapping Subject id to article pages; (2) check that OBJECT exists in the aligned article text; (3) heuristic filtering rules: remove instances where SUBJECT or OBJECT is a substring of the other; remove instances where OBJECT contains more than 5 words; limit repetition proportions for SUBJECT, RELATION, and OBJECT (1% for single SUBJECT, 5% for RELATION/OBJECT). Additionally, 0.1% random sampling of factual instances was applied after initial categorization (as stated).

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Value Alignment

**Atlas Risks**:
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy
- **Value Alignment**: Over- or under-reliance

**Potential Harm**: ['Temporal misalignment', 'Catastrophic forgetting', 'Hallucination']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
