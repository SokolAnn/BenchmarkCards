# CREER: A Large-Scale Corpus for Relation Extraction and Entity Recognition

## 📊 Benchmark Details

**Name**: CREER: A Large-Scale Corpus for Relation Extraction and Entity Recognition

**Overview**: We describe the design and use of the CREER dataset, a large corpus annotated with rich English grammar and semantic attributes. The CREER dataset uses the Stanford CoreNLP Annotator to capture rich language structures from Wikipedia plain text. This large supervised dataset can serve as the basis for improving the performance of NLP tasks in the future.

**Data Type**: text (annotated sentences with tokens, parse trees, dependencies, named entities, and relation KBP triplets)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Wet Lab Protocols
- CoNLL-2003
- SemEval-2010 Task8
- OntoNotes 5.0
- Penn Treebank
- OIE2016
- MPQA 3.0
- SemEval-2014 Task4

**Resources**:
- [Resource](https://140.116.82.111/share.cgi?ssid=000dOJ4)
- [Resource](https://dumps.wikimedia.org/)

## 🎯 Purpose and Intended Users

**Goal**: Construct a large corpus (CREER) for Relation Extraction and Entity Recognition containing syntax (parse trees and dependencies) and world knowledge information (entity mentions and relations) annotated from English Wikipedia using Stanford CoreNLP, to serve as a large supervised dataset and a testbed for NLP tasks and pre-training.

**Tasks**:
- Named Entity Recognition
- Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: English Wikipedia Dump dataset annotated using Stanford CoreNLP (Library stanfordcorenlp as a Python wrapper) to produce tokens, parse trees, dependencies, named entities, and relation KBP.

**Size**: 144,732,654 sentences; based on English Wikipedia Dump (2,500M words)

**Format**: N/A

**Annotation**: Annotated using Stanford CoreNLP. Annotations include tokens, parse trees, basic and enhanced dependencies, named entities (PERSON, LOCATION, ORGANIZATION, MISC, MONEY, NUMBER, SET, DATE, TIME, DURATION), and knowledge base population (KBP) relation triplets (slot filling and entity linking).

## 🔬 Methodology

**Methods**:
- Automated annotation using the Stanford CoreNLP pipeline (via the stanfordcorenlp Python wrapper)
- Comparison of dataset statistics to existing corpora

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
