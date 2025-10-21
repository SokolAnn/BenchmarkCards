# DAWT: Densely Annotated Wikipedia Texts across multiple languages

## 📊 Benchmark Details

**Name**: DAWT: Densely Annotated Wikipedia Texts across multiple languages

**Overview**: The DAWT dataset contains densely annotated Wikipedia texts where annotations include labeled text mentions mapping to entities (represented by their Freebase machine ids) as well as the type of the entity. The dataset contains a total of 13.6M articles, 5.0B tokens, 13.8M mention-entity co-occurrences, spans multiple languages (English, Spanish, Italian, German, French, Arabic), and densifies Wikipedia anchor links by 4.8× compared to original Wikipedia markup.

**Data Type**: text (densely annotated Wikipedia articles with mention-entity mappings and entity types)

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- English
- Spanish
- Italian
- German
- French
- Arabic

**Similar Benchmarks**:
- A cross-lingual dictionary for English Wikipedia concepts
- ClueWeb Freebase annotations

**Resources**:
- [GitHub Repository](https://github.com/klout/opendata/tree/master/wiki_annotation)
- [Resource](http://nlp.stanford.edu/data/glove.6B.zip)
- [GitHub Repository](https://github.com/stanfordnlp/GloVe)
- [Resource](http://www.fit.vutbr.cz/~imikolov/rnnlm/word-test.v1.txt)
- [Resource](https://developers.google.com/freebase#freebase-wikidata-mappings)
- [Resource](http://lemurproject.org/clueweb09/FACC1/)

## 🎯 Purpose and Intended Users

**Goal**: Create a large-scale, high-precision, densely annotated Wikipedia dataset mapping text mentions to Freebase machine ids across multiple languages and provide derived datasets (mention/entity counts, co-occurrence counts, entity embeddings, Freebase-to-Wikidata mappings) to support NLP and IR research.

**Target Audience**:
- Natural Language Processing researchers
- Information Retrieval researchers

**Tasks**:
- Named Entity Recognition
- Entity Disambiguation and Linking

**Limitations**: KB restricted to approximately 1,000,000 selected Freebase machine ids (subset of Freebase) due to resource and usefulness constraints; entity embeddings trained on 2.2B entity tokens (noted as less than GloVe's 6B tokens) which the paper cites as a possible reason for degraded performance at larger vector sizes.

## 💾 Data

**Source**: Wikipedia Data Dumps (January 20th 2017) annotated and linked to a Freebase-based knowledge base of approximately 1,000,000 Freebase machine ids; derived datasets produced from these annotated Wikipedia texts include mention occurrence counts, entity occurrence counts, mention-entity co-occurrence counts, entity embeddings, and Freebase-to-Wikidata id mappings.

**Size**: 13.6M articles; 5.0B tokens; 13.8M mention-entity co-occurrences; KB: ~1,000,000 Freebase machine ids; entity occurrences: 2.2B total entity occurrences and 1.8M unique entities in documents; entity embeddings generated for ~1.6M entities; Freebase->Wikidata mapping counts (Same: 2,048,531; Different: 24,638; DAWT Only: 2,362,077; Google Only: 26,413).

**Format**: JSON (annotated articles in JSON format); derived datasets available as counts/co-occurrence tables and embedding vector files.

**Annotation**: Automatically generated mappings from mentions to Freebase machine ids and entity types by enriching Wikipedia markup using candidate dictionaries (from Wikipedia and Freebase), semantic alignment pruning (Jaccard, edit distance, LCS), co-occurrence statistics, and resolution heuristics; original Wikipedia hyperlinks replaced with Freebase ids.

## 🔬 Methodology

**Methods**:
- Automated dataset generation via candidate dictionary creation and semantic alignment pruning
- Co-occurrence-based resolution of entity candidates using directly linked entities and co-occurrence frequencies
- Derived dataset generation (mention/entity counts, mention-entity co-occurrences, Freebase-to-Wikidata mappings, entity embeddings via GloVe)
- Evaluation of entity embeddings using a semantic analogy test set (Mikolov word-test.v1.txt) mapped to Freebase ids

**Metrics**:
- Accuracy
- Mention and entity occurrence counts
- Mention-entity co-occurrence counts
- Link density increase factor

**Calculation**: Accuracy computed as percentage correct on the semantic analogy test set after mapping words to Freebase ids; raw counts are computed as frequency counts from the annotated corpus; link density increase measured as average number of links per article compared to original Wikipedia markup (reported as 4.8×).

**Interpretation**: Higher accuracy on the semantic analogy task indicates better entity embeddings; a 4.8× increase in anchor links indicates denser annotation coverage; mention/entity counts and co-occurrence probabilities provide priors for candidate selection in NER/EDL.

**Baseline Results**: Entity embedding accuracy (semantic analogy average): 70.23% (50-dim), 69.73% (300-dim), 65.87% (1000-dim). GloVe word embeddings average accuracy: 53.21% (50-dim), 68.61% (100-dim), 76.91% (200-dim), 78.98% (300-dim). Link density: 4.8× more links than original Wikipedia. Dataset totals: 13.6M articles; 5.0B tokens; 13.8M mention-entity co-occurrences.

**Validation**: Validated by reporting dataset statistics and increased link density (4.8×) and by evaluating entity embeddings on the semantic analogy task (using Mikolov test set after mapping to Freebase ids); also validated mappings by comparing Freebase->Wikidata mappings against Google's mappings.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
