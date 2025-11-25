# CovidQA

## 📊 Benchmark Details

**Name**: CovidQA

**Overview**: We present CovidQA, the beginnings of a question answering dataset specifically designed for COVID-19, built by hand from knowledge gathered from Kaggle’s COVID-19 Open Research Dataset Challenge. To our knowledge, this is the first publicly available resource of its type, and intended as a stopgap measure for guiding research until more substantial evaluation resources become available.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Biomedical

**Similar Benchmarks**:
- BioASQ
- SQuAD
- MS MARCO
- TREC-COVID

**Resources**:
- [Resource](http://covidqa.ai/)
- [Resource](https://arxiv.org/abs/2004.11339)

## 🎯 Purpose and Intended Users

**Goal**: Provide an in-domain test set for questions related to COVID-19 to evaluate zero-shot or transfer capabilities of existing models and to serve as a stopgap evaluation resource until larger efforts are available.

**Target Audience**:
- Natural Language Processing researchers
- Machine Learning researchers
- Model developers

**Tasks**:
- Question Answering
- Passage Retrieval / Sentence Ranking

**Limitations**: The dataset (version 0.1) comprises 124 question–answer pairs and is too small for supervised training of models; the dataset lacks 'no answer' documents; annotators are not domain experts (authors built on Kaggle-curated content).

**Out of Scope Uses**:
- Supervised training of QA models

## 💾 Data

**Source**: Manually created from Kaggle’s COVID-19 Open Research Dataset Challenge literature review and aligned to the COVID-19 Open Research Dataset (CORD-19) (used the version of the corpus from April 10).

**Size**: 124 question–answer pairs (version 0.1 release); 27 questions (topics); 85 unique articles; on average 1.6 annotated answer spans per question–answer pair; annotation took approximately 23 hours.

**Format**: Article full text from CORD-19 in JSON format; answer spans annotated as substrings of the raw JSON article text (constrained to not cross sentence boundaries).

**Annotation**: Manual annotation by five co-authors with a lead annotator responsible for approvals; exact answer spans manually identified as proper substrings of the article text (from CORD-19 raw JSON) and not crossing sentence boundaries; some answers required human judgment when Kaggle entries did not match text verbatim.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation on ranked sentence outputs
- Unsupervised baselines (Okapi BM25, unsupervised BERT variants, SciBERT, BioBERT)
- Out-of-domain supervised transfer evaluation (BioBERT fine-tuned on SQuAD, BERT and T5 fine-tuned on MS MARCO)
- Baseline comparisons across ranking models

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Precision at rank one (P@1)
- Recall at rank three (R@3)

**Calculation**: Models produce a ranked list of sentences for each (question, article) pair; a sentence is deemed correct if it contains the exact answer via substring matching. Reported metrics are micro-averages across question–answer pairs.

**Interpretation**: Higher MRR, P@1, and R@3 indicate better effectiveness at identifying the sentence that contains the answer; evaluation is sentence-level (correct if sentence contains the annotated answer span).

**Baseline Results**: Selected results from Table 1 (natural language question input): Random P@1 0.012 R@3 0.034; BM25 P@1 0.150 R@3 0.216 MRR 0.243; BioBERT (unsupervised) P@1 0.097 R@3 0.142 MRR 0.170; BERT (fine-tuned on MS MARCO) P@1 0.194 R@3 0.315 MRR 0.329; T5 (fine-tuned on MS MARCO) P@1 0.282 R@3 0.404 MRR 0.415.

**Validation**: Evaluation conducted on CovidQA v0.1 using sentence-level substring matching against the ground-truth article full text in JSON; metrics are micro-averaged across question–answer pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency

**Atlas Risks**:
- **Transparency**: Uncertain data provenance
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
