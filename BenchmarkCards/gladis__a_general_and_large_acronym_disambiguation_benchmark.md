# GLADIS: A General and Large Acronym Disambiguation Benchmark

## 📊 Benchmark Details

**Name**: GLADIS: A General and Large Acronym Disambiguation Benchmark

**Overview**: To accelerate the research on acronym disambiguation, we construct a new benchmark named GLADIS with three components: (1) a much larger acronym dictionary with 1.5M acronyms and 6.4M long forms; (2) a pre-training corpus with 160 million sentences; (3) three datasets that cover the general, scientific, and biomedical domains.

**Data Type**: text (sentences with acronyms and acronym-long form pairs)

**Domains**:
- Natural Language Processing
- Scientific Research
- Biomedical

**Languages**:
- English

**Similar Benchmarks**:
- SciAD
- MadDog
- UAD
- WikilinksNED Unseen Mentions
- Medmentions

**Resources**:
- [GitHub Repository](https://github.com/tigerchen52/GLADIS)
- [Resource](https://arxiv.org/abs/2302.01860)

## 🎯 Purpose and Intended Users

**Goal**: Construct GLADIS, a General and Large Acronym DISambiguation benchmark that includes a larger dictionary, a pre-training corpus and three datasets covering the general, scientific, and biomedical domains to accelerate research on acronym disambiguation.

**Target Audience**:
- Research community
- NLP Researchers
- Model Developers

**Tasks**:
- Acronym Disambiguation

**Limitations**: The acronym dictionary still contains a small fraction of duplicate/noisy long forms due to typos, morphological changes and nested acronyms (manual evaluation shows 6% noisy long forms in a random sample; frequency-weighted clean forms = 97%). Performance on the Scientific subset still needs improvement and may require more domain-specific pre-training data.

## 💾 Data

**Source**: Pile dataset (Gao et al., 2020) textual sources; Wikidata Alias Table; UMLS Concept Names; adapted datasets: WikilinksNED Unseen Mentions, Medmentions, SciAD. Sources listed in Table 2 of the paper.

**Size**: Dictionary: 1.5M acronyms and 6.4M long forms; Pre-training corpus: ~160 million sentences; Source corpora total: 838.14 GiB (as shown in Table 2); Datasets: General ~45,000 samples, Scientific ~56,000 samples, Biomedical ~12,000 samples.

**Format**: N/A

**Annotation**: Dictionary extracted via rule-based algorithm (Schwartz and Hearst, 2002). Datasets: adapted from human-annotated and crowd-sourced entity disambiguation datasets (Medmentions: professional annotators; SciAD: human-annotated; WikilinksNED Unseen Mentions: crowd-sourced).

## 🔬 Methodology

**Methods**:
- Unsupervised evaluation (no access to train/validation sets)
- Fine-tuned evaluation (models fine-tuned on train sets using triplet loss)
- Pre-training AcroBERT with triplet loss and ambiguous negatives

**Metrics**:
- Precision
- Recall
- Macro F1 (Averaged F1 across classes)
- Accuracy

**Calculation**: Macro F1 is computed as the Averaged F1 across classes: compute F1 for each class and average them (the paper uses Averaged F1 to avoid overweighting popular classes). Precision and Recall definitions follow standard class-wise definitions; details in Appendix A.5.

**Interpretation**: Higher Macro F1 (Averaged F1) and Accuracy indicate better acronym disambiguation. The Averaged F1 is preferred to avoid bias toward popular classes, per the paper.

**Baseline Results**: Unsupervised setting (average across General, Scientific, Biomedical): AcroBERT Avg Macro F1 = 53.1, Avg Accuracy = 57.0 (Table 5). Fine-tuned setting (average): AcroBERT Avg Macro F1 = 54.1, Avg Accuracy = 57.7 (Table 6). Baselines reported include BM25, FastText, MadDog, BERT, BioBERT, SciBERT, and a Popularity-Ours baseline; detailed per-domain results are in Tables 5 and 6.

**Validation**: Datasets are repartitioned with a 6:2:2 ratio ensuring acronyms in the training set do not appear in validation and test sets (to avoid leakage). Manual checks: a random sample of 100 extracted sentences yielded 94% precision for acronym extraction; manual evaluation of 100 randomly chosen long forms from datasets shows 6% noisy long forms (frequency-weighted clean forms = 97%). SciAD was re-split to avoid data leakage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The Pile dataset used as source is under the MIT license (as stated); the three domain-specific datasets are adapted from SciAD, WikilinksNED Unseen Mentions and Medmentions and "allow sharing and redistribution" per the paper. The authors state source datasets and their licenses will be credited on the GitHub page and included in downloads of GLADIS.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
