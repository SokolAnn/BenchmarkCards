# Identifying civilians killed by police with distantly supervised entity-event extraction

## 📊 Benchmark Details

**Name**: Identifying civilians killed by police with distantly supervised entity-event extraction

**Overview**: From a news corpus, extract names of persons who have been killed by police. The paper presents a newly collected police fatality corpus (released publicly) and models using EM-based distant supervision with logistic regression and convolutional neural network classifiers to populate or update an entity-event database of police fatalities.

**Data Type**: text (news articles; sentence-level person mention instances)

**Domains**:
- Natural Language Processing
- Media and Journalism

**Languages**:
- English

**Similar Benchmarks**:
- Fatal Encounters (FE)
- The Counted (The Guardian)
- Gun Violence Database

**Resources**:
- [Resource](http://slanglab.cs.umass.edu/PoliceKillingsExtraction/)

## 🎯 Purpose and Intended Users

**Goal**: Extract names of persons killed by police from a corpus of news articles to populate or update an entity-event database.

**Target Audience**:
- Natural Language Processing researchers
- Practitioners maintaining police fatality databases
- Journalists

**Tasks**:
- Cross-document Entity-Event Extraction
- Entity-Event Database Population
- Entity Classification (binary: person killed by police)

**Limitations**: The news corpus coverage limits achievable recall (data upper bound AUPRC = 0.57) because Google News accesses a subset of relevant web news; reported model performance needs improvement for reliable real-world usage.

**Out of Scope Uses**:
- Historical fatalities (entities killed before the test period) are excluded from evaluation

## 💾 Data

**Source**: Web news articles downloaded via Google News queries throughout 2016 (queries combining police-related and killing-related keywords); Fatal Encounters (FE) publicly available database used as the gold-standard knowledge base (version downloaded Feb. 27, 2017).

**Size**: Fatal Encounters gold entities (G): 17,219 (historical), 452 (test). News dataset: train documents (Jan 2016–Aug 2016): 866,199 documents; test documents (Sep 2016–Dec 2016): 347,160 documents. Total mentions: 132,833 (train), 68,925 (test). Positive mentions (M+): 11,274 (train), 6,132 (test). Total entities (E): 49,203 (train), 24,550 (test). Positive entities (E+): 916 (train), 258 (test). Scraped web pages total: 1,162,300.

**Format**: N/A

**Annotation**: Mention extraction via spaCy named entity recognizer and HAPNIS name parser; training labels imputed via distant supervision aligning Fatal Encounters entries to mentions using heuristics (name-only and name-and-location) and EM-based soft (latent) labeling.

## 🔬 Methodology

**Methods**:
- Distant supervision (hard distant labels: name-only and name-and-location)
- EM-based soft (latent-variable) training
- Feature-based Logistic Regression
- Convolutional Neural Network (sentence-level CNN)
- Bootstrap resampling for significance testing
- Manual error analysis

**Metrics**:
- Area Under Precision-Recall Curve (AUPRC)
- F1 Score
- Precision
- Recall

**Calculation**: Entity-level probabilities computed via noisy-or aggregation: P(ye=1|xM(e)) = 1 - product_i (1 - P(zi=1|xi)). AUPRC computed using a trapezoidal rule over ranked entity probabilities. F1 reported is the maximum F1 value from the precision-recall curve.

**Interpretation**: AUPRC measures ranking quality of retrieved entities; higher AUPRC and higher precision at given recall indicate better utility for practitioners. The paper notes a data coverage upper bound (AUPRC upper bound = 0.57) due to limited news corpus coverage, which constrains achievable recall.

**Baseline Results**: Model results on test set (entity prediction): hard-LR (all features) AUPRC 0.142, F1 0.266; hard-CNN AUPRC 0.130, F1 0.252; soft-CNN (EM) AUPRC 0.164, F1 0.267; soft-LR (EM) AUPRC 0.193, F1 0.316. Data upper bound AUPRC 0.57, F1 0.73. Off-the-shelf event extractors: RPI-JIE (best rule R3) precision 0.172, recall 0.168, F1 0.170 (Table 6).

**Validation**: Bootstrap resampling was used to estimate standard errors and test significance (resampling entities, resampling documents, and resampling documents with deduplication; B=10,000 samples). Manual error analysis of false positives was performed. Pairwise significance testing between models used bootstrap-based p-values.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
