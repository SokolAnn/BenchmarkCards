# corpus of 567 radiology reports annotated for recommendation information

## 📊 Benchmark Details

**Name**: corpus of 567 radiology reports annotated for recommendation information

**Overview**: A gold standard corpus of radiology reports annotated with follow-up recommendation information (sentence-level recommendation labels and entity-level spans for reason, recommended test, and time frame) used to train and evaluate deep learning extraction models.

**Data Type**: text (radiology reports; sentence-level recommendation labels and token-level entity spans for reason, test, time frame)

**Domains**:
- Healthcare
- Natural Language Processing

**Similar Benchmarks**:
- 2014 i2b2/UTHealth corpus
- 2010 i2b2/VA challenge
- MIMIC dataset
- i2b2 dataset

## 🎯 Purpose and Intended Users

**Goal**: The goals of our research are to: (1) build a gold standard corpus of radiology reports annotated with recommendation information, (2) build information extraction approaches based on deep learning to automatically identify recommendation information, and (3) apply the trained extractors to a large dataset of 3.3 million radiology reports to analyze follow-up adherence rates.

**Tasks**:
- Text Classification
- Named Entity Recognition
- Information Extraction

**Limitations**: One of the limitations of our study was the size of the training set for recommendations. Some time frame entities could not be normalized by Stanford’s temporal tagger (example: "second trimester"). The analysis did not utilize the extracted test and reason entities and assumed the recommended test would be the same modality as the original test.

## 💾 Data

**Source**: Annotated corpus of 567 radiology reports created from a multi-institutional radiology dataset of 3,301,748 reports from University of Washington Medical Center (1,903,772 reports) and Harborview Medical Center (1,397,976 reports) collected 2008-2018. Pilot corpus of 800 de-identified radiology reports was also created earlier.

**Size**: Annotated corpus: 567 radiology reports; 597 positive recommendation sentences and 11,787 negative sentences. Entity counts in annotated corpus: 735 test entities, 173 time frame entities, 545 reason entities. Multi-institutional dataset: 3,301,748 radiology reports; 47,424,876 sentences in the full dataset.

**Format**: BRAT standoff format for annotations; raw text radiology reports; sentence-tokenized with NLTK sentence tokenizer.

**Annotation**: Manual annotation by clinicians and trained annotators. Pilot annotation: two annotators (one radiologist and one internal medicine specialist) annotated sentences. Main annotation: sentence-level review by one radiologist and one neurologist; entity-level annotation by one neurologist and one medical school student. BIOES token tagging used for NER. Inter-annotator agreement reported (pilot sentence-level F1=0.974; initial sentence-level kappa=0.43 and F1=0.59; entity-level F1: reason 0.78, test 0.88, time frame 0.84).

## 🔬 Methodology

**Methods**:
- Hierarchical Attention Networks (HAN) for sentence-level recommendation classification
- NeuroNER (deep neural named-entity recognition) for entity extraction (reason, test, time frame)
- Word2Vec pretrained word embeddings on the 10-year / 3.3 million radiology corpus
- Character-enhanced token embeddings (as used in NeuroNER)
- BIOES tagging for NER
- Grid search for hyperparameter optimization
- 5-fold cross-validation for evaluation
- 0.9/0.1 train/validation split and early stopping (patience 15 epochs)
- Manual validation of model predictions on sampled recommendations

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics computed primarily using 5-fold cross-validation. Recommendation classifier reported TP/TN/FP/FN counts (true positive: 574, true negative: 11,711, false positive: 75, false negative: 22) and precision/recall/F1. NER evaluated at token level with 5-fold cross-validation. HAN training used a 0.9/0.1 train/validation split with early stopping based on validation F1.

**Interpretation**: The authors state the presented performance results are "very promising" but acknowledge there is room for improvement, particularly given the small size of the labeled training corpus for recommendations.

**Baseline Results**: Previous Max-Ent classifier (prior work) achieved 0.66 precision, 0.88 recall, 0.76 F1 for recommendation detection. A baseline classifier used for sampling had high recall (0.90) and low precision (0.35). Current results: recommendation extraction HAN achieved Precision 0.88, Recall 0.96, F1 Score 0.92 (5-fold cross-validation). Token-level NER 5-fold cross-validation results: Reason Precision 68.53, Recall 62.05, F1 Score 65.10; Test Precision 74.20, Recall 71.48, F1 Score 72.71; Time frame Precision 83.38, Recall 85.05, F1 Score 84.16.

**Validation**: 5-fold cross-validation used for model evaluation. Manual validation: 200 predicted recommendations sampled across top 5 modalities; 178/200 identified as true positives yielding precision 0.89 on that sample. Inter-annotator agreement reported for pilot and annotation iterations (pilot sentence-level F1=0.974; initial sentence-level kappa=0.43 and F1=0.59; entity-level F1: reason 0.78, test 0.88, time frame 0.84).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Potential Harm**: If follow-up recommendations "fall through the cracks", patients may present months later with advanced disease (e.g., metastatic cancer).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Pilot corpus of 800 reports were de-identified. University of Washington Human Subjects Division Institutional Review Board approved retrospective review of the multi-institutional dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: University of Washington Human Subjects Division Institutional Review Board approved retrospective review of the dataset (IRB approval mentioned).
