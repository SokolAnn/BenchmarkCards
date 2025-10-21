# Leaf Clinical Trials (LCT) corpus

## 📊 Benchmark Details

**Name**: Leaf Clinical Trials (LCT) corpus

**Overview**: In this paper, we introduce the Leaf Clinical Trials (LCT) corpus, a human-annotated corpus of over 1,000 clinical trial eligibility criteria descriptions using highly granular structured labels capturing a range of biomedical phenomena. We provide details of our schema, annotation process, corpus quality, and statistics. Additionally, we present baseline information extraction results on this corpus as benchmarks for future work.

**Data Type**: text (clinical trial eligibility criteria with entity and relation annotations)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- EliIE
- Chia

**Resources**:
- [Resource](https://doi.org/10.6084/m9.figshare.17209610)
- [GitHub Repository](https://github.com/uw-bionlp/clinical-trials-gov-data)
- [GitHub Repository](https://github.com/uw-bionlp/clinical-trials-gov-annotation/wiki)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large, human-annotated corpus of clinical trials eligibility criteria with a highly granular annotation schema to facilitate training and evaluation of NLP methods for transforming eligibility criteria into database queries and to serve as benchmarks for information extraction.

**Target Audience**:
- Natural Language Processing researchers
- Clinical researchers
- Developers of cohort discovery / query generation tools

**Tasks**:
- Named Entity Recognition
- Relation Extraction
- Normalization (mapping entities to coded representations)
- Negation Detection
- Query Generation / Semantic Parsing

**Limitations**: The corpus is largely singly annotated (119 of 1,006 documents double-annotated), roughly half of the corpus (493 documents) were automatically predicted then manually corrected which can potentially lead to data bias if predicted entities are not thoroughly reviewed and corrected, the corpus itself is not composed of queries and thus cannot be directly proven to be more effective for query generation, and the authors do not formally define a quantifiable means for measuring semantic representation within annotations.

## 💾 Data

**Source**: Eligibility criteria text extracted from ClinicalTrials.gov; 1,020 randomly selected clinical trials eligibility descriptions were extracted, 14 were discarded as information-poor, resulting in 1,006 annotated eligibility descriptions.

**Size**: 1,006 annotated eligibility descriptions; 105,816 annotations (as reported in Table 1)

**Format**: Brat standoff format (.txt and .ann)

**Annotation**: Manual annotation by two annotators (a biomedical informatician and a computer scientist) with semi-automated pre-annotation using NeuroNER (biLSTM+CRF) followed by manual correction; resulting corpus included 887 single-annotated and 119 double-annotated documents.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Neural sequence models (biLSTM+CRF for NER)
- Pretrained transformer models (SciBERT, PubMedBERT for NER)
- R-BERT and SciBERT for relation extraction

**Metrics**:
- Precision
- Recall
- F1 Score
- Micro-averaged F1 Score

**Calculation**: Entity annotations were considered matching only if entity types and token start and end indices matched exactly. Relation annotations were considered matching only if relation type and token start and end indices of both the subject and target matched exactly. Metrics reported as Precision / Recall / F1 (micro-averaged at corpus level where indicated).

**Interpretation**: Higher Precision, Recall, and F1 indicate better named entity recognition and relation extraction performance. Corpus-level micro-averaged F1 is used to summarize overall performance.

**Baseline Results**: Highest reported corpus-level micro-averaged F1 for entities: 81.3% using SciBERT. Highest reported corpus-level micro-averaged F1 for relations: 85.2% using R-BERT with SciBERT. (Precision/Recall/F1 per-entity and per-relation reported in Tables 5 and 6.)

**Validation**: Inter-annotator agreement (20 training docs) was 76.1% F1 for entities and 60.3% F1 for relations. After guideline revisions and additional double-annotation (99 documents), agreement improved to 78.1% F1 for entities and 60.9% F1 for relations. Additional experiments comparing manual vs semi-automated annotation portions showed comparable NER performance (F1 78.6% and 80.0%).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
