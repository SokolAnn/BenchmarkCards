# GGPO NC (German Guideline Program in Oncology NLP Corpus)

## 📊 Benchmark Details

**Name**: GGPO NC (German Guideline Program in Oncology NLP Corpus)

**Overview**: We present GGPO NC (German Guideline Program in Oncology NLP Corpus), a freely distributable German language corpus based on clinical practice guidelines for oncology. This corpus is one of the largest ever built from German medical documents, does not contain patient-related information and can therefore be used without data protection restrictions, and provides a variety of metadata such as literature references and evidence levels.

**Data Type**: text (clinical practice guideline documents; recommendation and background text segments; XML and plain text formats)

**Domains**:
- Natural Language Processing
- Healthcare
- Oncology

**Languages**:
- German

**Similar Benchmarks**:
- CREST corpus
- Yale Guideline Recommendation Corpus (YGRC)
- JSYNCC
- 3000PA

**Resources**:
- [Resource](https://www.leitlinienprogramm-onkologie.de/projekte/ggponc-english/)
- [Resource](https://doi.org/10.5281/zenodo.4067994)

## 🎯 Purpose and Intended Users

**Goal**: To address (1) the lack of available German medical text resources for NLP research, and (2) the need for machine-readable clinical practice guidelines (CPGs), by constructing a corpus based on a set of German CPGs for oncology.

**Target Audience**:
- Natural Language Processing researchers
- Medical and clinical researchers
- Developers of precision medicine search engines
- Developers of clinical decision support systems

**Tasks**:
- Named Entity Recognition
- Information Extraction
- Semantic Search
- Evidence-based medicine summarization
- Temporal tracking of guideline changes

**Limitations**: Gene extraction suffers from a large number of false positives due to lexical overlap with common German words and acronyms; the German UMLS vocabulary is limited (~234k entries) which reduces recall; inconsistent handling of German umlauts and compound words in UMLS and tokenization leads to false negatives and inconsistent entity matches; certain TNM expressions can cause context-dependent semantic ambiguities.

## 💾 Data

**Source**: Semi-structured JSON versions of the guidelines acquired from the REST API of the Content Management System (CMS) that serves the backend for the GGPO mobile app; data were transformed from JSON to an XML format preserving document structure, recommendation metadata and literature references.

**Size**: Full corpus: 8,414 text segments; 4,348 recommendations; 59,672 sentences; 1,340,201 tokens; 76,252 types; 37,928 literature references. Annotated subset: 4,153 text segments; 2,069 recommendations; 29,528 sentences; 664,029 tokens; 50,732 types; 18,585 references.

**Format**: A single XML file including document structure and metadata; a file for the complete literature index; individual plain text versions of text segments, sentences, and tokens; automatically created entity annotations and a subset of manually corrected annotations in standoff format.

**Annotation**: Automated annotations using JCORE (UIMA-based) pipelines, FRAMED models, JUFIT filtering for UMLS terms, and a rule-based TNM extractor implemented with spaCy; a subset was manually reviewed by medical-student annotators using the BRAT annotation tool (manually reviewed subset covers 13 guidelines / ~half of corpus).

## 🔬 Methodology

**Methods**:
- Automated annotation pipelines (JCORE, FRAMED, JUFIT, spaCy rule-based TNM extraction)
- Manual human annotation/review (BRAT)
- Inter-annotator agreement analysis
- Automated named entity extraction evaluation (precision/recall/F1)

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Inter-annotator agreement (IAA) was calculated using the pair-wise average F-score of instances and tokens (Hripcsak and Rothschild, 2005). Micro-averaged precision and recall were computed against the manually reviewed annotations as gold standard.

**Interpretation**: The IAA achieved an average F-score of 0.742 on instances and 0.758 on tokens for the evaluated subset. Precision and recall vary by entity class (see reported per-class results). Gene annotations exhibited a very large number of false positives and were excluded from IAA analysis.

**Baseline Results**: Overall (without Genes): IAA instances average F-score = 0.742 (std = 0.094); IAA token average F-score = 0.758 (std = 0.094); micro-averaged Precision = 0.945; micro-averaged Recall = 0.528.

**Validation**: A manually reviewed subset covering 13 full guidelines (~half the corpus) was used for validation. The IAA calculation used 40 agreement documents (20 high-annotation segments per four guidelines + 20 randomly sampled segments) totaling approx. 19,000 tokens annotated by all annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Clinical practice guidelines (CPGs) in GGPO NC do not contain patient-related information and therefore do not require de-identification; access to the corpus is provided for researchers under conditions of a Data Use Agreement (DUA).

**Data Licensing**: Available under Data Use Agreement (DUA)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
