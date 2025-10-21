# DBpedia NIF: Open, Large-Scale and Multilingual Knowledge Extraction Corpus

## 📊 Benchmark Details

**Name**: DBpedia NIF: Open, Large-Scale and Multilingual Knowledge Extraction Corpus

**Overview**: We present DBpedia NIF - a large-scale and multilingual knowledge extraction corpus. The aim of the dataset is two-fold: to dramatically broaden and deepen the amount of structured information in DBpedia, and to provide large-scale and multilingual language resource for development of various NLP and IR task. The dataset provides the content of all articles for 128 Wikipedia languages.

**Data Type**: text (Wikipedia article texts with sections, paragraphs, and annotated links)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Semantic Web

**Languages**:
- English
- Cebuano
- Swedish
- German
- French
- Dutch
- Russian
- Italian
- Spanish
- Polish

**Similar Benchmarks**:
- Linked Hypernyms Dataset (LHD)
- Lector
- Polyglot-NER
- DBpedia Spotlight
- Wikify!

**Resources**:
- [Resource](http://wiki.dbpedia.org/nif-abstract-datasets)
- [GitHub Repository](https://github.com/dbpedia/extraction-framework/)
- [Resource](http://persistence.uni-leipzig.org/nlp2rdf/)
- [Resource](http://nlp2rdf.aksw.org/dbpedia-nif-examples/)

## 🎯 Purpose and Intended Users

**Goal**: To dramatically broaden and deepen the amount of structured information in DBpedia, and to provide large-scale and multilingual language resource for development of various NLP and IR task.

**Target Audience**:
- Semantic Web community
- Natural Language Processing researchers
- Information Retrieval researchers
- Participants of the TextExt knowledge extraction challenge

**Tasks**:
- Knowledge Extraction
- Fact Extraction
- Relation Extraction
- Named Entity Recognition
- Part-of-Speech Tagging
- Dependency Parsing
- Coreference Resolution
- Entity Typing
- Ontology Extraction
- Information Retrieval

**Limitations**: Only the English subset of the dataset is published according to the Linked Data principles with dereferenceable URIs; publishing of other language versions will be considered only if there is requirement within the community. Enrichment was not applied to the "See also", "Notes", "Bibliography", "References" and "External Links" sections.

## 💾 Data

**Source**: Extracted from Wikipedia article texts (Wikipedia XML dumps) rendered via MediaWiki and processed with the DBpedia Extraction Framework; content semantically modeled using the NLP Interchange Format (NIF).

**Size**: Over 9 billion RDF triples (the DBpedia NIF dataset provides over 9 billion triples; overall DBpedia triples count brought up to 23 billion).

**Format**: RDF/OWL using the NLP Interchange Format (NIF) version 2.1; published as Linked Data (English subset published with dereferenceable URIs).

**Annotation**: Links, anchor texts and offsets automatically extracted from rendered HTML; dataset further enriched with automatically generated links via a string-matching enrichment process; enrichment validated via crowdsourced human evaluation (three judgments per annotation).

## 🔬 Methodology

**Methods**:
- Automated extraction from Wikipedia dumps using MediaWiki rendering and the DBpedia Extraction Framework
- Automated enrichment of links via full string-matching (anchors sorted by length) applied across article text
- Automated syntactic validation (Raptor RDF parser, iconv, wc)
- RDFUnit validation against the NIF ontology
- Crowdsourced human evaluation of enrichment (multiple annotators, three judgments per item)

**Metrics**:
- Number of RDF triples (over 9 billion)
- Articles, Paragraphs, Links per language (per-table statistics for top languages)
- Mean and median number of annotations per article
- Fraction of correct anchors (annotated correctness)
- Fraction of correct links (annotated correctness)
- Fraction of correct anchors and links combined
- Inter-annotator agreement measured with Fleiss' kappa
- Five-star dataset classification (Tim Berners-Lee five-star dataset)

**Calculation**: A link is considered correct if at least two out of three annotators provided the same judgment. Inter-annotator agreement computed using Fleiss' kappa. Dataset statistics (articles, paragraphs, links, mean and median annotations) are reported per language as raw counts and summary statistics.

**Interpretation**: Fleiss' kappa values interpreted according to Landis and Koch: reported values classified as "substantial agreement" (0.61-0.80) for links and "moderate agreement" (0.41-0.60) for anchors and anchors+links combined. Higher fractions indicate better enrichment accuracy; results reported per-language (English and German).

**Validation**: Syntactic validation with Raptor RDF parsing, iconv and wc for unicode correctness, and RDFUnit tests ensuring adherence to NIF format (including checks that nif:anchorOf matches substring between begin and end offsets). Semantic validation via crowdsourced evaluation: top-10 PageRank articles for English and German, 30 random links per article, ten annotators, three judgments per annotation; results reported as fractions correct and Fleiss' kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Governance

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Governance**: Lack of data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
