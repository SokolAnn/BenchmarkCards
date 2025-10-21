# INCLUSIFY A benchmark and a model for gender-inclusive German

## 📊 Benchmark Details

**Name**: INCLUSIFY A benchmark and a model for gender-inclusive German

**Overview**: Presents a dataset and measures for benchmarking tasks related to gender-inclusive language in German. Defines two tasks—flagging exclusive words (sequence labeling) and suggesting inclusive alternatives (sequence-to-sequence / style-transfer)—and provides annotated benchmark data and evaluation metrics to evaluate systems that detect exclusive (generic masculine) language and propose inclusive reformulations.

**Data Type**: text (exclusive-to-inclusive sentence pairs; per-word sequence labeling annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- German

**Resources**:
- [Resource](https://gitlab.com/davidpomerenke/gender-inclusive-german)
- [Resource](https://huggingface.co/diversifix)
- [Resource](https://diversifix.org)
- [Resource](https://tech.4germany.org/project/diversitaetssensible-sprache-bam/)
- [Resource](https://arxiv.org/abs/2212.02564)

## 🎯 Purpose and Intended Users

**Goal**: Provide an evaluation benchmark (data and measures) for tasks related to gender-inclusive German: (1) detecting exclusive words (generic masculine) and (2) suggesting inclusive alternatives, enabling evaluation and comparison of inclusive-language systems.

**Target Audience**:
- Developers of inclusive-language tools
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Sequence Labeling (flagging exclusive words)
- Text Style Transfer / Sequence-to-Sequence (exclusive -> inclusive sentence suggestions)
- Suggestion Ranking (ranked candidate suggestions evaluation)

**Limitations**: 400 annotated sentences; single annotator; dataset sampled and sorted by density of inclusive matches which may bias the benchmark towards texts with lots of potential for inclusive language (e.g., job advertisements); neutral-style texts may be underrepresented.

## 💾 Data

**Source**: GC4 (German Colossal Clean Crawled Corpus) head part (web crawl) 2017-2020, filtered for inclusive texts, plus manual annotation to create parallel exclusive/inclusive sentence pairs.

**Size**: 400 entries (annotated sentences); 305 exclusive phrases; Entries with gender characters allowed: 272; Entries with gender characters used: 119; Crawl date range for source: 2017-2020.

**Format**: JSON

**Annotation**: Single annotator (author). For each inclusive sentence the annotator either discarded it, kept it (no labels), or created an exclusive version by editing the sentence, adapting grammar where needed, and flagging exclusive words. Annotation done via a minimal HTML/JavaScript interface with automatic suggestions for clear cases.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics computed over benchmark data
- Per-word sequence labeling evaluation
- Ranked-suggestions evaluation for suggestion generation
- Ablation studies for pipeline components

**Metrics**:
- Recall
- Precision
- F1 Score
- Top-k accuracy (Correct in candidates)
- Top-5 accuracy (Correct in 5 best candidates)
- Top-1 accuracy (Correct in 1 best candidate)
- Suggestion score (generalized logistic function; continuous 0–1)
- Lemma-based match metrics (lemma-level matching for suggestion evaluation)

**Calculation**: Labeling task: per-word comparison of system-assigned label vs. benchmark label; compute Recall, Precision, F1. Suggestion task: check whether the benchmark target sentence is present among system suggestions (any position), among top-5, or at top-1; compute corresponding rates. Additionally compute a continuous suggestion score s(r) based on a generalized logistic function mapping the rank r to [0,1] (paper proposes using B=1 and v=0.01 and aggregating example scores by mean). Lemma-based variants of suggestion matching are also computed.

**Interpretation**: Higher Recall/Precision/F1 indicate better detection of exclusive words. For suggestions, presence of the target sentence among candidates and higher suggestion score indicate better suggestion quality and ranking (score 1 if target is first suggestion, 0 if absent). Metrics are aggregated by mean across examples.

**Baseline Results**: Labeling: Recall 0.888, Precision 0.818, F1 0.852. Suggestion task (words / lemmas): Correct in candidates 0.537 / 0.610; Correct in 5 best candidates 0.441 / 0.497; Correct in 1 best candidates 0.051 / 0.051; Suggestion score 0.492 / 0.559.

**Validation**: Evaluated on the 400 annotated entries sampled from GC4 head part; ablation studies performed by disabling pipeline components and data subsets; metrics aggregated by mean. Processing-time measurements reported on random samples from German Wikipedia.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Privacy**: Data privacy rights alignment
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Gender-based exclusion in language (the benchmark aims to detect and reduce gender-exclusive language)', 'Reduced accessibility for visually impaired users due to gender-character rendering by screen readers (explicitly discussed as a concern)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Benchmark data format and license: JSON, License CC0 1.0 (as stated in paper). Source corpus (GC4) has its own license; original texts sampled one sentence per document to mitigate copyright issues.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
