# RuBQ: A Russian Dataset for Question Answering over Wikidata

## 📊 Benchmark Details

**Name**: RuBQ: A Russian Dataset for Question Answering over Wikidata

**Overview**: RuBQ is the first Russian knowledgebase question answering (KBQA) dataset. The dataset consists of 1,500 Russian questions of varying complexity, their English machine translations, SPARQL queries to Wikidata, reference answers, as well as a Wikidata sample of triples containing entities with Russian labels. The dataset is intended for evaluation in Semantic Web, natural language processing, and information retrieval, especially for multilingual question answering.

**Data Type**: question-answering pairs

**Domains**:
- Semantic Web
- Natural Language Processing
- Information Retrieval

**Languages**:
- Russian
- English

**Similar Benchmarks**:
- Free917
- WebQuestions
- SimpleQuestions
- ComplexQuestions
- GraphQuestions
- WebQuestionsSP
- SimpleQuestions2Wikidata
- 30M Factoid QA Corpus
- LC QuAD
- ComplexWebQuestions
- ComplexSequentialQuestions
- QALD9
- LC-QuAD 2.0
- FreebaseQA
- MSParS
- CFQ

**Resources**:
- [Resource](http://doi.org/10.5281/zenodo.3835913)
- [GitHub Repository](https://github.com/vladislavneon/RuBQ)
- [Resource](https://zenodo.org/record/3751761)
- [Resource](https://translate.yandex.com/)
- [Resource](https://toloka.yandex.com/)
- [Resource](http://docs.deeppavlov.ai/en/master/features/models/kbqa.html)

## 🎯 Purpose and Intended Users

**Goal**: Provide a high-quality Russian KBQA dataset (RuBQ) for evaluation of knowledge-base question answering and semantic parsing over Wikidata, including Russian questions, English machine translations, SPARQL queries, reference answers, and a Wikidata sample.

**Target Audience**:
- Semantic Web researchers
- Natural Language Processing researchers
- Information Retrieval researchers
- Practitioners working on multilingual question answering

**Tasks**:
- Knowledge Base Question Answering
- Semantic Parsing
- Cross-lingual Question Answering
- Evaluation/testing of KBQA systems

**Limitations**: The dataset is modest in size (1,500 questions) and the authors propose to use it primarily for testing rule-based systems, cross-lingual transfer learning models, and models trained on automatically generated examples. A noted downside is a lower share of literals (dates and numerical values) linked to Wikidata. Wikidata dynamics may change reference answers over time (mitigated by providing a Wikidata snapshot).

## 💾 Data

**Source**: Trivia Q&A pairs mined from several open Russian quiz collections on the Web (e.g., http://baza-otvetov.ru, http://viquiz.ru) and Wikidata (used for SPARQL queries and the RuWikidata8M snapshot).

**Size**: 1,500 questions; initial crawl ~150,000 Q&A pairs; intermediate 14,435 Q&A pairs; 9,655 answers linked to Wikidata candidates; RuWikidata8M sample: about 212M triples with 8.1M unique entities.

**Format**: JSON (dataset entries include: original Russian question, English machine translation, original answer text, SPARQL query, list of entities in the query, list of relations, list of answers, query type tags).

**Annotation**: Entity linking via an IR-based approach over collected Wikidata entities with Russian labels; crowdsourced verification of answer entity candidates on Yandex.Toloka with qualification tests, honeypots, and weighted majority vote; automatic generation of SPARQL paths followed by in-house (author) verification and manual SPARQL construction for complex questions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Baseline system evaluation (DeepPavlov and WDAqua)

**Metrics**:
- precision@1
- Exact Match
- Precision
- Recall
- F1 Score

**Calculation**: An evaluation script is provided that calculates precision@1, exact match, precision, recall, and F1, as well as breakdown of results by query types.

**Interpretation**: Higher precision@1, exact match, and F1 indicate better system performance. The paper reports that WDAqua outperforms DeepPavlov in precision@1 on the answerable subset (16% vs. 13%) but has lower accuracy on unanswerable questions (43% vs. 73%). No explicit performance thresholds for 'good' vs 'poor' are provided.

**Baseline Results**: DeepPavlov (answerable 960): correct 129; WDAqua (answerable 960): correct 153. On unanswerable (240): DeepPavlov empty/not found 175, incorrect 65; WDAqua empty/not found 102, incorrect 138. Detailed breakdown by query types provided in Table 4 of the paper.

**Validation**: Dataset split into development (300) and test (1,200) sets keeping a similar distribution of query types. A RuWikidata8M snapshot is provided to mitigate Wikidata dynamics and ensure reproducibility of answers.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
