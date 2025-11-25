# UNER dataset (Universal Named Entity Recognition)

## 📊 Benchmark Details

**Name**: UNER dataset (Universal Named Entity Recognition)

**Overview**: We present the UNER dataset, a multilingual and hierarchical parallel corpus annotated for named-entities. We describe in detail the developed procedure necessary to create this type of dataset in any language available on Wikipedia with DBpedia information. The three-step procedure extracts entities from Wikipedia articles, links them to DBpedia, and maps the DBpedia sets of classes to the UNER labels. This is followed by a post-processing procedure that significantly increases the number of identified entities in the final results.

**Data Type**: text (token-level named-entity annotations, IOB format)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Croatian

**Resources**:
- [GitHub Repository](https://github.com/cleopatra-itn/MIDAS)
- [Resource](https://tinyurl.com/y2taxs8b)
- [Resource](https://tinyurl.com/y4tlz4a2)
- [Resource](https://arxiv.org/abs/2212.07429)

## 🎯 Purpose and Intended Users

**Goal**: To parse data from Wikipedia corpora in multiple languages, extract named entities through hyperlinks, align them with entity classes from DBpedia and translate them into UNER types and subtypes; to propose a NERC dataset creation workflow that works for languages covered by both Wikipedia and DBpedia, including under-resourced languages.

**Tasks**:
- Named Entity Recognition
- Named Entity Classification

**Limitations**: Accuracy needs to be enhanced (the final post-processing step requires improvement); the workflow covers basically UNER types and sub-types of the Name category; false negatives due to missing hyperlinks in Wikipedia articles; uneven content of Wikipedia across languages affects results; a manual and more detailed evaluation is necessary to verify precision and recall.

## 💾 Data

**Source**: Wikipedia dumps (text extraction preserving hyperlinks using WikiExtractor) and DBpedia via SPARQL queries to obtain DBpedia classes, mapped to UNER using an UNER/DBpedia mapping schema.

**Size**: English UNER: 3.3 GB (325,395,838 tokens); Croatian UNER: 108 MB (9,388,224 tokens). English: 17,150 files across 172 folders; Croatian: 411 files across 5 folders.

**Format**: Plain text files with token-level UNER annotations in IOB format (post-processed tokenization applied).

**Annotation**: Automatically generated (silver-standard) via DBpedia class extraction and UNER/DBpedia mapping; post-processing scripts apply tokenization improvements, IOB format, entity listing, and automatic annotation expansion (final post-processing applied to Croatian corpus only).

## 🔬 Methodology

**Methods**:
- Automated extraction from Wikipedia dumps (WikiExtractor)
- DBpedia entity linking via SPARQL queries (SPARQLWrapper)
- Mapping DBpedia classes to UNER labels using UNER/DBpedia mapping and DBpedia hierarchy prioritization
- Post-processing: tokenization improvements, IOB conversion, entity listing, automatic annotation expansion
- Qualitative manual evaluation on a random sample of entities

**Metrics**:
- Corpus statistics: Total number of tokens, Number of Non-Entity Tokens, Number of Entity Tokens, Number of Entities, Number of Different Entities (reported per corpus)
- Manual-sample annotation evaluation percentages: Correct (85%), Correct but vague (6%), Incorrect due to DBpedia (7%), Incorrect due to UNER association (3%)

**Calculation**: Corpus statistics are computed by counting tokens and tags after post-processing. Manual evaluation performed on a random sample of 943 entities: DBpedia associated classes and final UNER tag were checked and percentages computed over the sample.

**Interpretation**: From the manual sample, 91% of the entities are correctly tagged with UNER tags (85% correct + 6% correct but vague). Post-processing (final step applied to Croatian corpus) increases annotation coverage (entity tokens percentage increased from 7.1% to 16.2% in Croatian). The authors note remaining errors due to DBpedia class assignment and UNER mapping rules.

**Validation**: Qualitative manual evaluation on 943 randomly selected entities from the English UNER corpus. Post-processing and automatic annotation expansion applied and analyzed (final expansion applied to Croatian corpus).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA 4.0 (English and Croatian UNER corpora as stated in the paper)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
