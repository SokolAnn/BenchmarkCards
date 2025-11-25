# MultiLegalPile: A 689GB Multilingual Legal Corpus

## 📊 Benchmark Details

**Name**: MultiLegalPile: A 689GB Multilingual Legal Corpus

**Overview**: We curate and release MULTI LEGAL PILE, a 689GB corpus in 24 languages from 17 jurisdictions, consisting of diverse legal data sources and allowing pretraining of NLP models under fair use, with most of the dataset licensed very permissively.

**Data Type**: text (legal documents: caselaw, legislation, contracts)

**Domains**:
- Legal
- Natural Language Processing

**Languages**:
- Bulgarian
- Czech
- Danish
- German
- Greek
- English
- Spanish
- Estonian
- Finnish
- French
- Irish
- Croatian
- Hungarian
- Italian
- Lithuanian
- Latvian
- Maltese
- Dutch
- Polish
- Portuguese
- Romanian
- Slovak
- Slovene
- Swedish

**Similar Benchmarks**:
- LEXTREME
- LexGLUE

**Resources**:
- [Resource](https://huggingface.co/datasets/mc4)
- [Resource](https://eur-lex.europa.eu/content/legal-notice/legal-notice.html)
- [Resource](https://huggingface.co/datasets/lener_br)
- [Resource](https://tinyurl.com/ycysvtbm)
- [Resource](https://www.theverge.com/2022/11/8/23446821/)
- [GitHub Repository](https://github.com/togethercomputer/RedPajama-Datamation)

## 🎯 Purpose and Intended Users

**Goal**: To curate and release MULTI LEGAL PILE, a 689GB corpus in 24 languages from 17 jurisdictions, to enable pretraining of NLP models (legal PLMs) and improve performance in legal language understanding tasks.

**Target Audience**:
- ML Researchers
- Legal professionals
- General public

**Tasks**:
- Single-label Text Classification
- Multi-label Text Classification
- Named Entity Recognition
- Multiple Choice Question Answering

**Limitations**: We did not perform deduplication; we were not able to pretrain a large generative model due to limited compute; we do not claim completeness and were unable to perform quality analysis for all available languages; some sources do not explicitly state licenses.

## 💾 Data

**Source**: Compiled from four subsets: (a) Native Multi Legal Pile (scraped legal sources across jurisdictions), (b) Eurlex Resources (downloaded via the eurlex R package / SPARQL), (c) Legal mC4 (filtered from the multilingual C4 web crawl using regular expressions for legal citations), and (d) Pile of Law (integrated from Henderson et al., 2022). Native subset aggregated data from 29 sources (see paper Table 9).

**Size**: 689GB total (Native Multi Legal Pile 112 GB; Eurlex Resources 179 GB; Legal mC4 106 GB; Pile of Law 292 GB).

**Format**: xz compressed JSON Lines (JSONL)

**Annotation**: No supervised annotation for downstream labels (corpus intended for pretraining). Filtering/curation: automatic filtering using regular expressions to detect legal citations; manual precision evaluation by legal experts for German, English, Spanish, French, and Italian during filtering and iterative regex refinement.

## 🔬 Methodology

**Methods**:
- Fine-tuning on downstream benchmarks (LEXTREME and LexGLUE)
- Automated metrics evaluation (macro-F1 / micro-F1)
- Hierarchical transformer evaluation for long documents
- Multiple random-seed runs for reliability (see per-benchmark procedures)

**Metrics**:
- Macro-F1
- Micro-F1
- Harmonic mean (aggregate score)
- Evaluation loss (used for model selection)

**Calculation**: All scores are reported as macro-F1 (equally weighting each class) except where micro-F1 is specified for particular tasks. For Tables 4 and 5 results: harmonic mean of results of 3 random seeds (1-3). For Table 6 (LexGLUE): five repetitions with seeds 1-5 and report test scores from the best-performing seed on development data. Dataset and language aggregate scores are computed via successive harmonic means across configurations/datasets/languages.

**Interpretation**: Higher macro-F1 (or micro-F1 where used) indicates better performance. Aggregate scores computed via harmonic mean summarize performance across datasets and languages; state-of-the-art (SotA) is determined by achieving the highest aggregate score.

**Baseline Results**: On LEXTREME: Legal-XLM-R-large achieves a dataset aggregate score of 59.5 versus 59.4 for Legal-XLM-R-base and 59.3 for XLM-R large (reported as new SotA). On LexGLUE: Legal-en-R-large achieves the highest aggregate score of 72.7 (reported as SotA on multiple tasks).

**Validation**: Manual precision evaluation by legal experts during mC4 filtering with iterative regex refinement; evaluation follows original benchmark experimental setups (Niklaus et al., 2023; Chalkidis et al., 2022) with multiple seeds and established hyperparameter settings; no hyperparameter tuning was performed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Legal Compliance
- Intellectual Property
- Data Laws
- Accuracy
- Transparency

**Atlas Risks**:
- **Legal Compliance**: Legal accountability, Generated content ownership and IP
- **Intellectual Property**: Copyright infringement, Data usage rights restrictions
- **Data Laws**: Data usage restrictions
- **Accuracy**: Data contamination, Unrepresentative data
- **Transparency**: Lack of training data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Overall release under CC BY-NC-SA 4.0 depending on upstream licenses. Eurlex Resources: CC BY 4.0. Legal mC4: ODC-BY. Pile of Law: CC BY-NC-SA 4.0 (unchanged). Native Multi Legal Pile sources: mixed (ranging from CC0, CC BY-NC 4.0, CC BY 4.0, some sources 'not protected by copyright law', and some sources without explicit license statements).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The authors state they assume the fair use doctrine allows employing the data for pretraining and note that copyright issues in generative AI remain unresolved; no explicit claims of regulatory compliance (e.g., GDPR/CCPA) are made.
