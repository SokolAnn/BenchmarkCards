# XWikis

## 📊 Benchmark Details

**Name**: XWikis

**Overview**: A cross-lingual summarisation corpus with long documents in a source language associated with multi-sentence summaries in a target language. The corpus covers twelve language pairs and directions for four European languages (Czech, English, French, German). Cross-lingual document-summary instances are derived from Wikipedia by combining lead paragraphs and article bodies from language-aligned Wikipedia titles.

**Data Type**: Document-summary pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- Czech
- English
- French
- German

**Similar Benchmarks**:
- WikiLingua
- MultiLing’13
- MultiLing’15
- Global Voices
- MLSUM
- SumeCzech

**Resources**:
- [GitHub Repository](https://github.com/lauhaide/clads)
- [Resource](https://www.wikipedia.org/)
- [Resource](http://voxeurop.eu)
- [Resource](https://voxeurop.eu/en/legal-notice-privacy/)
- [Resource](https://dumps.wikimedia.org)
- [Resource](https://en.wikipedia.org/wiki/Help:Interlanguage_links)
- [GitHub Repository](https://github.com/attardi/wikiextractor)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale cross-lingual summarisation dataset (XWikis) derived from Wikipedia to support research on cross-lingual and monolingual abstractive summarisation, and to enable evaluation in supervised, zero-shot, few-shot, and out-of-domain scenarios.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Cross-Lingual Summarization
- Abstractive Summarization
- Monolingual Summarization

**Limitations**: The paper focuses on four European languages (Czech, English, French, German) in this release and plans to release further languages in the future. The dataset construction assumes the lead paragraph can serve as a summary; human validation shows this assumption is imperfect (sentence-level support proportions: 66.2% for German-English, 77.4% for French-English, 60.5% for Czech-English).

## 💾 Data

**Source**: Wikipedia articles (lead paragraphs and article bodies) aligned via Wikipedia Interlanguage Links for English, German, French, and Czech (June 2020 dumps). An out-of-domain news dataset was extracted from Voxeurop (professional journalists/translators).

**Size**: XWikis-comparable: 213,911 document-summary pairs; XWikis-parallel (intersection across languages): 7,000 document-summary pairs. Per-paper table entries (Table 1) reported as: en row: 425,279, 468,670, 148,519; de row: 376,803, 252,026, 109,467; fr row: 312,408, 213,425, 91,175; cs row: 64,310, 53,275, 51,578. Out-of-domain Voxeurop extraction: 2,666 summary-article pairs (2,000 used for evaluation). Monolingual Den!en dataset: 300,000 instances (90/5/5 train/validation/test).

**Format**: Preserved raw text with section mark-ups (e.g., <h2>); text normalized with a variant of NFKC and tokenized using SentencePiece. (Data and code made available via the GitHub repository listed in Resources.)

**Annotation**: Automatically extracted (lead paragraph and body aligned via Interlanguage Links). A human validation study was conducted on samples: bilingual judges (3 per language pair) evaluated 20 instances per pair for overall adequacy and sentence-level support.

## 🔬 Methodology

**Methods**:
- Automated metrics (ROUGE-1/ROUGE-2/ROUGE-L)
- Extractive characterization metrics (Coverage, Density, Compression, % new n-grams per Narayan et al. (2018) and Grusky et al. (2018))
- Human evaluation with bilingual judges (yes/no overall adequacy and sentence-level support)
- Model evaluations: Supervised, Zero-shot, Few-shot (LF-MAML, FT, CVT) using pre-trained models (mBART, mBART50)
- Extractive baselines (EXT-ORACLE, LEAD, LEXRANK)

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- Coverage
- Density
- Compression
- % new unigrams / bigrams / trigrams / 4-grams
- Fleiss's Kappa (inter-annotator agreement)

**Calculation**: ROUGE (1/2/L) F1 scores reported for model evaluation. Coverage and Density follow Grusky et al. (2018): Coverage measures average number of tokens in the summary that are part of extractive fragments; Density measures average length of extractive fragments. % new n-grams computed as percentage of n-grams in the summary not present in the input (Narayan et al., 2018). Human evaluation: yes/no answers for 'Does the summary provide a general overview of the Wikipedia title?' and per-sentence 'Does the sentence contain facts that are supported by the document?'.

**Interpretation**: Higher ROUGE scores indicate better overlap/quality relative to references. High Coverage with low Density suggests summaries overlap in content but are phrased differently (abstractive behavior). LEAD performing below EXT-ORACLE indicates no lead bias in documents. Human evaluation proportions and Fleiss's Kappa indicate validity but imperfect agreement (reported kappa values).

**Baseline Results**: Selected results reported in the paper (ROUGE-L F1): mBART50 Supervised on XWikis (Table 8) — en: 32.53; de-en: 32.95; fr-en: 31.84; cs-en: 33.72. mBART50 Zero-shot ROUGE-L F1 (Table 8) — de-en: 31.70; fr-en: 30.97; cs-en: 31.14. Extractive baselines (Table 8) — EXT-ORACLE ROUGE-L F1: en 31.33, de-en 23.75, fr-en 25.01, cs-en 25.09; LEAD ROUGE-L F1: en 25.45 (see Tables 6, 8 for full results).

**Validation**: Human validation: for de-en, fr-en, cs-en, three bilingual judges per pair judged 20 instances each for overall adequacy and sentence support; overall adequacy proportions reported (Table 4) and Fleiss's Kappa reported (0.48 de-en, 0.55 fr-en, 0.59 cs-en). Dataset splits: XWikis-comparable split into training (95%) and validation (5%); XWikis-parallel subset (7,000 titles) used for evaluation comparability. Monolingual Den!en: 300,000 instances split 90/5/5 for train/validation/test.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authorisation obtained from Voxeurop SCE publishers for use of Voxeurop data (https://voxeurop.eu/en/legal-notice-privacy/). No other specific privacy/anonymity procedures are described in the paper.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
