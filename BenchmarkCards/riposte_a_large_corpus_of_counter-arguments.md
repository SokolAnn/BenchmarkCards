# Riposte! A Large Corpus of Counter-Arguments

## 📊 Benchmark Details

**Name**: Riposte! A Large Corpus of Counter-Arguments

**Overview**: We cast providing constructive feedback as a natural language processing task and create Riposte!, a corpus of counter-arguments (CAs) for fallacious micro-level arguments. Produced by crowdworkers, Riposte! contains over 18k CAs. Workers were instructed to identify common fallacy types and produce a CA which identifies the fallacy; we analyze how workers create CAs and construct a baseline generation model.

**Data Type**: text (counter-arguments and claim-premise pairs)

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- Argument Reasoning Comprehension (ARC)

**Resources**:
- [Resource](https://arxiv.org/abs/1910.03246)
- [Resource](https://www.mturk.com/)
- [Resource](https://spacy.io/)

## 🎯 Purpose and Intended Users

**Goal**: Create a large-scale corpus of crowdworker-produced counter-arguments to enable research on automatic generation of CAs for fallacious micro-level arguments and to cast constructive feedback as an NLP text-generation task.

**Target Audience**:
- Educators
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Text Generation (Counter-argument generation)
- Text Classification (Fallacy type classification)

**Limitations**: Challenges noted: the corpus must contain a variety of topics to generalize to unseen topics; many fallacies in an argument may be not easily identifiable; producing CAs is costly and time-consuming.

## 💾 Data

**Source**: Counter-arguments collected via Amazon Mechanical Turk for the 1,263 unique topic-claim-premise pairs from the Argument Reasoning Comprehension (ARC) dataset (Habernal et al., 2018b; 172 unique topics and 264 unique claims).

**Size**: 18,887 counter-arguments (CAs); ARC: 1,263 unique topic-claim-premise pairs

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk; 5 workers were asked to produce a CA per argument (one task per fallacy type). Workers selected a fallacy type and produced CAs using provided templates; unsure/no-fallacy workers could provide a CA or reason. Majority vote was used to select CAs and fallacy types. Responses failing criteria (blank, not a sentence, direct copy, or not English) were manually rejected.

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU)
- Automated similarity (Jaccard similarity)
- Human evaluation (crowdsourced annotation of Strength, Persuasiveness, Relevance)
- Baseline model evaluation (Simple Overlap baseline, seq2seq in-domain and out-of-domain)

**Metrics**:
- BLEU
- Jaccard similarity
- Strength (annotator score)
- Persuasiveness (annotator score)
- Relevance (annotator score)
- Krippendorff's alpha (agreement)
- F1 Score (4-way fallacy classification reported for LSTM encoder: 36.02% F1)

**Calculation**: BLEU scores were calculated between each worker-produced CA and the original argument (claim and premise). Average Jaccard similarity scores were computed between CAs for a single argument after tokenization and removal of stop words and punctuation. Human evaluation used 3 annotators per CA (50 arguments shown) rating Strength, Persuasiveness, and Relevance; Krippendorff's alpha reported for agreement. Data splits: unsure instances filtered out; majority vote used; split into 80% train / 10% dev / 10% test ensuring no unique claim-premise pairs are shared across splits.

**Interpretation**: BLEU and overlap analyses indicate workers mainly used premise and claim keywords to create CAs. Seq2seq in-domain models perform substantially better than out-of-domain, indicating simple models struggle on unseen topics. Human evaluation found generated CAs to be more relevant but weaker and less persuasive than gold CAs.

**Baseline Results**: BLEU (selected values from Table 4): Simple Overlap (P+C) = 13.76 overall; Simple Overlap (overall column) = 18.16. Seq2seq in-domain (overall) = 16.57; Seq2seq out-of-domain (overall) = 5.53. Human evaluation mean scores (Table 5) — Strength: gold 2.3 (α=0.20), generated 1.98 (α=0.20); Persuasiveness: gold 2.26 (α=0.71), generated 1.94 (α=0.15); Relevance: gold 2.74 (α=0.20), generated 2.84 (α=0.72).

**Validation**: Filtered out 'unsure' instances; majority vote applied for selecting CAs and fallacy types; 80/10/10 train/dev/test split with no shared claim-premise pairs across splits. Human evaluation: 3 annotators per CA on 50 arguments to compare gold vs generated CAs. Similarity and agreement statistics (BLEU, Jaccard, Krippendorff's alpha) were reported.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
