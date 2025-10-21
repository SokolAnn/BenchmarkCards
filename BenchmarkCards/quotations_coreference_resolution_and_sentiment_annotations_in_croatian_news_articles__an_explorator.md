# Quotations, Coreference Resolution, and Sentiment Annotations in Croatian News Articles: An Exploratory Study

## 📊 Benchmark Details

**Name**: Quotations, Coreference Resolution, and Sentiment Annotations in Croatian News Articles: An Exploratory Study

**Overview**: This paper presents a corpus annotated for the task of direct-speech extraction in Croatian. The paper focuses on the annotation of the quotation, co-reference resolution, and sentiment annotation in SETimes news corpus in Croatian and on the analysis of its language-specific differences compared to English. From this, a list of the phenomena that require special attention when performing these annotations is derived. The generated corpus with quotation features annotations can be used for multiple tasks in the field of Natural Language Processing.

**Data Type**: text (news articles with quotation spans, verb-cue spans, speaker spans, coreference relations, and sentence-level sentiment annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- Croatian

**Similar Benchmarks**:
- QuoteLi3
- SETimes

**Resources**:
- [Resource](http://www.clarin.si/services/web/query)
- [Resource](http://tubiblio.ulb.tu-darmstadt.de/106270/)

## 🎯 Purpose and Intended Users

**Goal**: Create a corpus of news texts with quotes annotations for the Croatian language to support the task of direct-speech extraction and analysis of language-specific phenomena.

**Tasks**:
- Quote Extraction
- Speaker Identification
- Verb-cue Classification
- Coreference Resolution
- Sentiment Analysis

**Limitations**: Preliminary/gold-standard data; focused only on direct quotes; annotated subset of 140 documents; annotations performed by a Croatian native speaker (single annotator).

**Out of Scope Uses**:
- Processing of indirect quotes
- Processing of mixed quotes (only direct quotations were the primary focus)

## 💾 Data

**Source**: SETimes Croatian corpus (SETimes.com news portal)

**Size**: Full SETimes Croatian corpus: 2.7 million words and 197,559 sentences; Annotated subset: 140 documents; 469 quotes; 875 sentences annotated for sentiment; 2,497 total annotation instances (speakers, spoken-text, verb-cue, relations).

**Format**: INCEpTION annotation format (annotations performed using the INCEpTION tool)

**Annotation**: Manual annotation by a Croatian native speaker using INCEpTION with three custom layers: Quote Fine (span-based: speaker/source, verb-cue, spoken-text), Quote Simple (span-based sentence-level sentiment: positive/neutral/negative), and Quote Co-reference (relations: Anaphoric, Uses-verb, Verb-spoken-text).

## 🔬 Methodology

**Methods**:
- Manual annotation using INCEpTION
- Descriptive corpus analysis and statistics

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: SETimes parallel corpus (CC-BY-SA license) as stated in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
