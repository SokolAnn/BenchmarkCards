# AMALGUM – A Free, Balanced, Multilayer English Web Corpus

## 📊 Benchmark Details

**Name**: AMALGUM – A Free, Balanced, Multilayer English Web Corpus

**Overview**: We present a freely available, genre-balanced English web corpus totaling 4M tokens and featuring a large number of high-quality automatic annotation layers, including dependency trees, non-named entity annotations, coreference resolution, and discourse trees in Rhetorical Structure Theory.

**Data Type**: text (web documents with multilayer linguistic annotations: tokenization, POS, lemmas, dependency parses, entity and coreference annotations, RST discourse trees)

**Domains**:
- Natural Language Processing
- Corpus Linguistics

**Languages**:
- English

**Similar Benchmarks**:
- GUM (Georgetown University Multilayer corpus)
- OntoNotes
- RST Discourse Treebank (RST-DT)
- Penn Discourse Treebank (PDTB)
- WaCky corpora
- COW corpora

**Resources**:
- [GitHub Repository](https://github.com/gucorpling/amalgum)
- [Resource](https://arxiv.org/abs/2006.10677)

## 🎯 Purpose and Intended Users

**Goal**: Presenting a genre-balanced, richly-annotated web corpus (AMALGUM) as a more sizable alternative to smaller manually created annotated data sets, and evaluating the accuracy of the resulting resource.

**Target Audience**:
- Academic researchers
- Corpus linguists
- Natural Language Processing researchers and practitioners
- Model developers

**Tasks**:
- Tokenization
- Part-of-Speech Tagging
- Dependency Parsing
- Named Entity Recognition (including nested/non-named entities)
- Coreference Resolution
- Discourse Parsing (Rhetorical Structure Theory)

**Limitations**: AMALGUM annotations are automatically produced and contain errors; discourse-level annotations (coreference resolution and discourse parsing) achieve only modest accuracy compared to gold standards; Reddit raw text cannot be distributed directly (stand-off annotations used).

**Out of Scope Uses**:
- Testing applications such as active learning, cross-tagger validation, human-in-the-loop/crowdsourcing, and pre-training are outside the scope of the current paper.

## 💾 Data

**Source**: Web data sampled to match GUM composition: MDPI (academic), Wikipedia (biography), Project Gutenberg (fiction), Reddit (forum discussions, distributed as stand-off annotations), wikiHow (how-to), Wikinews (news, interviews), Wikivoyage (travel). Sampling frame modeled on the GUM corpus.

**Size**: 4,002,929 tokens (approximately 4 million tokens) across 4,960 documents (approximately 500,000 tokens per genre subset as reported in Table 1).

**Format**: Stand-off annotations for Reddit are explicitly mentioned; formats for the distributed annotations for other sources are not specified in the paper.

**Annotation**: Tokenization, multiple POS tagsets and ensemble POS tagging, lemmas, Universal Dependencies parses and morphological features, sentence splits and sentence types, document structure (headings, paragraphs, figures, lists), nested named and non-named entity recognition, coreference resolution (including singletons), and full RST discourse parses.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (Precision / Recall / F1, Accuracy, UAS, LAS, CoNLL coreference metrics)
- Evaluation on gold GUM test set
- Evaluation on a manually corrected AMALGUM sample (16 documents, ~2,000 tokens)
- Model retraining on in-domain data, model stacking/ensembling, cross-layer feature incorporation

**Metrics**:
- Precision
- Recall
- F1 Score (micro-averaged as stated in the paper)
- Accuracy
- Unlabeled Attachment Score (UAS)
- Labeled Attachment Score (LAS)
- Average F1 of MUC, B3 and CEAF (coreference evaluation; paper notates CEAF as CEAF 􏰀4)

**Calculation**: Standard definitions as used in CoNLL shared tasks and common evaluation practice: tokenization reported with Precision/Recall/F1; POS tagging reported as Accuracy; dependency parsing evaluated with UAS and LAS as in the CoNLL UD parsing shared task; coreference evaluated using average F1 of MUC, B3 and CEAF (micro-averaged F1 scores as noted).

**Interpretation**: Higher metric values indicate closer agreement with gold standard annotations. Authors interpret improvements over out-of-the-box baselines (e.g., retrained models and ensemble methods) as higher NLP quality for the corpus, while noting that discourse-level tasks still show modest accuracy and remain challenging.

**Baseline Results**: Selected results reported in the paper: Tokenization (GUM test) StanfordNLP (EWT) P/R/F1 = 98.41 / 99.97 / 99.19; StanfordNLP (GUM) = 99.93 / 99.91 / 99.92; this paper = 99.87 / 99.90 / 99.89. POS Tagging (Accuracy on GUM test): StanfordNLP (EWT) 93.07%; StanfordNLP (GUM) 95.85%; XGBoost (4 models ensemble) 97.04% (AMALGUM snippet accuracy up to 97.37%). Dependency Parsing (GUM test UAS/LAS): StanfordNLP (EWT) 86.89 / 83.66; StanfordNLP (GUM) 89.32 / 85.49; this paper 89.47 / 85.89. Coreference (average F1 of MUC, B3, CEAF) on GUM test: Joshi et al. (2019) 41.4; xrenner 51.4; xrenner + S&H types 51.2. Coreference on AMALGUM snippets: Joshi et al. (2019) 64.4; xrenner 79.3; xrenner + S&H types 78.1. Discourse parsing (GUM test span/nuclearity/relation): J&E14 baseline 67.62 / 43.94 / 24.17; J&E14+multilayer 77.98 / 61.79 / 44.07.

**Validation**: Validation performed by evaluating automatic annotations against the gold standard GUM test set and against a manually corrected AMALGUM sample consisting of 16 documents (two snippets per genre) totaling ~2,000 tokens; comparisons to out-of-the-box and retrained baseline systems are reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Reddit raw text cannot be distributed directly; the authors distribute stand-off annotations for Reddit along with a script to recover plain text via the Reddit API. No other anonymization procedures are specified.

**Data Licensing**: Documents were scraped from sites that provide data under open licenses (in most cases, Creative Commons licenses). Reddit is handled as an exception via stand-off annotations.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
