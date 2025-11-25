# MIZ ¯AN: A Large Persian-English Parallel Corpus

## 📊 Benchmark Details

**Name**: MIZ ¯AN: A Large Persian-English Parallel Corpus

**Overview**: We introduce the biggest Persian-English parallel corpus with more than one million sentence pairs collected from masterpieces of literature. We also present acquisition process and statistics of the corpus, and experiment a base-line statistical machine translation system using the corpus.

**Data Type**: text (parallel sentence pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Persian
- English

**Similar Benchmarks**:
- Europarl
- JRC-Acquis
- TEP
- Shiraz Project

**Resources**:
- [GitHub Repository](https://github.com/omidkashefi/Mizan)
- [Resource](http://sourceforge.net/projects/virastyar)
- [Resource](http://www.isiri.org/portal/files/std/6219.htm)

## 🎯 Purpose and Intended Users

**Goal**: To present MIZ ¯AN, a manually aligned Persian-English parallel corpus of about one million sentence pairs, provide acquisition process and corpus statistics, and evaluate the corpus via a baseline statistical machine translation (SMT) experiment.

**Target Audience**:
- Machine Translation researchers
- Natural Language Processing researchers

**Tasks**:
- Machine Translation
- Parallel Corpus Construction

**Limitations**: N/A

## 💾 Data

**Source**: Collected from translated masterpieces of literature: English texts downloaded from Project Gutenberg and corresponding Persian translations identified via the National Library and Archive of Iran; Persian side manually typewritten from published translations.

**Size**: Table 1 reports 1,011,085 sentences per side; the paper also states '1,021,596 unique Persian-English sentence pairs'; corpus described as 'more than one million sentence pairs' and 'about 25 million terms' (Persian: 12,049,952 words (198,860 distinct); English: 11,667,272 words (153,666 distinct); Overall: 23,717,224 words (352,526 distinct)).

**Format**: Unicode text files; released in two files (one per language); one sentence per line; sentences correspond by line numbers.

**Annotation**: Manual sentence-level alignment by alignment specialists (mostly translators and linguists) assisted by alignment-aiding software that provides break/merge/delete/edit operations; paragraph- and chapter-level automatic pre-alignment was used prior to manual refinement.

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU Score)
- Human expert post-editing (100 randomly selected outputs per test set)
- SMT evaluation using Moses toolkit with KenLM language models

**Metrics**:
- BLEU Score

**Calculation**: BLEU score computed between SMT outputs and reference translations; additionally BLEU computed between outputs and human post-edited translations. Language models built with KenLM of order five. Systems tuned using 5,000 in-domain sentences with minimum error rate training.

**Interpretation**: Authors note BLEU can underestimate translation quality (example of fluent post-edited output with modest BLEU). Post-edited BLEU scores are substantially higher; authors state the SMT system 'could satisfies about 50% of human expectations' based on post-editing results.

**Baseline Results**: Baseline SMT trained on MIZ ¯AN: BLEU ~25.52 (held-out), ~24.26 (EiT out-of-domain). TEP baseline: BLEU ~6.26 (EiT). With added verb entries (+Verb): MIZ ¯AN BLEU ~27.44 (held-out), ~25.08 (EiT). Lemmatized evaluation (Lem): held-out BLEU ~26.05. Lem+Verb: held-out BLEU ~27.86, EiT ~26.78. Post-edited BLEU: Held-out reference 27.84 vs post-edited 51.59; EiT reference 39.86 vs post-edited 57.35.

**Validation**: Evaluation on 1,000 held-out in-domain sentences and 900 out-of-domain sentences from an English in Travel for Persians (EiT) book; tuning with 5,000 in-domain sentences; an expert post-edited 100 randomly selected outputs from each test set for additional evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
