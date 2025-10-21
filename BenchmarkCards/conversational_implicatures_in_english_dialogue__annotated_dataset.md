# Conversational implicatures in English dialogue: Annotated dataset

## 📊 Benchmark Details

**Name**: Conversational implicatures in English dialogue: Annotated dataset

**Overview**: In this paper, we introduce a dataset of dialogue snippets with three constituents, which are the context, the utterance, and the implicated meanings. These implicated meanings are the conversational implicatures.

**Data Type**: text (dialogue triplets: context, utterance, implicated meaning)

**Domains**:
- Natural Language Processing
- Linguistics

**Languages**:
- English

**Similar Benchmarks**:
- Potts experimental dataset (215 indirect polar questions)
- SQUINKY!
- CoQA
- Movie-DiC

**Resources**:
- [Resource](https://doi.org/10.6084/m9.figshare.10315505.v3)
- [Resource](https://figshare.com/articles/Implicature_dataset/10315505)
- [Resource](http://www.imsdb.com/)
- [Resource](https://www.microworkers.com/)
- [Resource](https://www.ets.org/toefl)
- [Resource](https://englishteststore.net/)

## 🎯 Purpose and Intended Users

**Goal**: To create and provide a dataset of dialogues annotated with conversational implicatures to aid research on computing implicated meanings of utterances and for identifying and synthesising conversational implicatures in dialogues.

**Target Audience**:
- Researchers in Natural Language Processing
- Researchers in Computational Pragmatics and Linguistics
- Dialogue system developers

**Tasks**:
- Conversational Implicature Identification
- Dialogue Generation / Synthesis

**Limitations**: Primarily focused on polar questions where an indirect answer without an explicit 'Yes' or 'No' generates implicatures; only the single immediate context of an utterance is considered; the dataset collection is ongoing and not yet at a considerable scale with negative samples.

## 💾 Data

**Source**: Dialogues collected from listening comprehension transcripts of TOEFL practice sections (transcribed from English Test Store), movie scripts from IMSDb for 45 animation movies, other dialogues with metaphors/idioms/hyperboles/indirect criticism from the internet, and synthesized dialogues.

**Size**: 500 dialogue narrations transcribed from TOEFL listening comprehension; around 500 dialogue snippets from IMSDb movie scripts (exact total dataset size not stated)

**Format**: N/A

**Annotation**: Manual annotation of implicated meanings. Some data collected via crowdsourcing using MicroWorkers from native English speakers (US, UK, Australia, New Zealand, Canada). An utterance may have one or more implicated meanings. Annotation quality can be verified by computing cosine similarity of annotations by different annotators.

## 🔬 Methodology

**Methods**:
- Transcription of TOEFL listening comprehension narrations
- Scraping movie scripts from IMSDb (animation genre)
- Manual annotation of dialogue triplets <context, utterance, implicature>
- Crowdsourcing via MicroWorkers for generation and annotation of some dialogues
- Preprocessing (removal/replacement of character names with A/B)
- Annotation verification using cosine similarity of annotator annotations
- Manual cleaning to remove explicit yes/no responses and irrelevant entries

**Metrics**:
- Cosine similarity of annotator annotations (used for verification/prioritization of annotations)

**Calculation**: The accuracy of annotated implicatures can be verified by computing the cosine similarity of annotations by different annotators for the same response utterance.

**Interpretation**: Annotations with high cosine similarity scores are prioritized for entry into the dataset; high similarity indicates higher annotator agreement/confidence.

**Validation**: Manual scrutiny and cleaning of scraped snippets; removal of responses containing explicit 'yes'/'no'; annotation verification and prioritization using cosine similarity across annotators.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Crowdsourced contributors (for generation/annotation) were native English speakers from the US, UK, Australia, New Zealand and Canada.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Character names from movie scripts were removed and replaced with 'A' and 'B' in preprocessing. No other privacy or anonymization procedures are explicitly discussed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
