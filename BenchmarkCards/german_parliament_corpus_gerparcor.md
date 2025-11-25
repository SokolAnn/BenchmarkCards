# German Parliament Corpus (GERPARCOR)

## 📊 Benchmark Details

**Name**: German Parliament Corpus (GERPARCOR)

**Overview**: GERPARCOR is a genre-specific corpus of (predominantly historical) German-language parliamentary protocols from three centuries and four countries, including state and federal level data. It contains conversions of scanned protocols (including Fraktur) via an OCR process based on TESSERACT, and all protocols were preprocessed with the spaCy3 NLP pipeline and automatically annotated with metadata (session date, location, title). GERPARCOR is provided in the XMI format of the UIMA project and intended as a large corpus of historical texts in the field of political communication for various tasks in Natural Language Processing.

**Data Type**: text (parliamentary plenary protocols; OCR-converted scanned pages; annotated XMI documents)

**Domains**:
- Natural Language Processing
- Political Communication

**Languages**:
- German

**Similar Benchmarks**:
- GermaParl
- ParlSpeech V2
- DeuParl
- Parlat beta corpus

**Resources**:
- [GitHub Repository](https://github.com/texttechnologylab/GerParCor)
- [Resource](https://tesseract-ocr.github.io/)
- [Resource](https://spacy.io/)

## 🎯 Purpose and Intended Users

**Goal**: To create a large, genre-specific corpus of predominantly historical German-language parliamentary protocols (covering three centuries and multiple countries/levels) to fill a gap in uniformly accessible annotated parliamentary corpora and to enable time-related analyses and studies of political language for various tasks in Natural Language Processing.

**Target Audience**:
- Natural Language Processing researchers
- Researchers studying political language and language change

**Tasks**:
- Part-of-Speech Tagging
- Lemmatization
- Named Entity Recognition
- Morphological Analysis
- Dependency Parsing
- Time-related language change analysis
- Political language analysis / text analysis

**Limitations**: Not all parliamentary document types are included (corpus focuses on plenary protocols). Some protocols were not available online or could not be digitized (e.g., Niedersachen State Parliament 1st to 9th legislative periods). OCR of historical/Fraktur scans is challenging and required preprocessing steps; OCR quality varies by source.

## 💾 Data

**Source**: Plenary protocols (parliamentary minutes) from Austria, Germany (including Reichstag, Bundestag, Bundesrat and German regional parliaments), Liechtenstein and Switzerland; collected via parliamentary APIs, direct downloads from parliamentary websites, and provided/digitized documents from stenographic services.

**Size**: N/A

**Format**: XMI (UIMA CAS serialization)

**Annotation**: Automatically annotated via spaCy3 (tokenization, sentence segmentation, Part-of-Speech tagging, lemmatization, named entity recognition, morphological features, dependency parsing) and enriched with metadata (session date, location, title). OCRed documents processed with TESSERACT and post-processed/quality-checked with SymSpell.

## 🔬 Methodology

**Methods**:
- Automated data retrieval from parliamentary APIs and downloads
- Optical Character Recognition (TESSERACT) for scanned and Fraktur documents
- Preprocessing and linguistic annotation using spaCy3 via TEXTIMAGER (tokenization, sentence recognition, PoS tagging, lemmatization, named entity recognition, morphology recognition, dependency parsing)
- OCR post-processing and quality checking with SymSpell
- Distributed processing via TEXTIMAGER

**Metrics**:
- Percentage of correct tokens (OCR quality measured via SymSpell)
- Percentage of wrong tokens (OCR quality measured via SymSpell)
- Percentage of unknown tokens (OCR quality measured via SymSpell)

**Calculation**: OCR quality metrics (percent correct, wrong, unknown) are computed based on tokens that are not skipped by SymSpell. SymSpell outputs were categorized as: input equals output (correct), input differs from output (wrong), or output empty (unknown). Percentages are reported per parliament in Table 2.

**Interpretation**: OCR quality outputs are reported around ~94% correct tokens for many sources; the authors state that OCR quality is sufficiently good to support NLP based on GERPARCOR.

**Validation**: OCR output quality was checked using the spellchecker SymSpell; results (percentages of correct, wrong and unknown words per parliament) are reported in Table 2. The authors used these checks to conclude the OCR quality is sufficient for NLP tasks.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
