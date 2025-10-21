# ConvQuestions

## 📊 Benchmark Details

**Name**: ConvQuestions

**Overview**: ConvQuestions is a crowdsourced benchmark with 11,200 distinct conversations from five domains for evaluating conversational question answering over knowledge graphs. Answers in the benchmark are grounded in Wikidata entities to enable fair comparison across diverse methods.

**Data Type**: conversational question-answering pairs (questions and answers grounded to Wikidata entities)

**Domains**:
- Books
- Movies
- Soccer
- Music
- TV Series

**Similar Benchmarks**:
- WebQuestions
- SimpleQuestions
- WikiMovies
- ComplexWebQuestions
- ComQA
- CSQA
- QBLink
- CoQA
- ShARC
- SQA

**Resources**:
- [Resource](http://qa.mpi-inf.mpg.de/convex/)
- [Resource](http://bit.ly/2QhsSDC)
- [Resource](https://www.mturk.com/help#what_are_masters)

## 🎯 Purpose and Intended Users

**Goal**: Provide a realistic benchmark (ConvQuestions) to evaluate conversational question answering over knowledge graphs, with conversations grounded in Wikidata.

**Tasks**:
- Question Answering
- Conversational Question Answering

**Limitations**: N/A

**Out of Scope Uses**:
- Opinionated questions (e.g., "best film by this actor?")
- Non-factoid questions (causal, procedural, etc.)

## 💾 Data

**Source**: Crowdsourced from Amazon Mechanical Turk (AMT) Master Workers. Turkers created conversations (questions and answers), provided textual surface forms and Wikidata links for seed entities and answers, and paraphrases; answers are grounded in Wikidata entities.

**Size**: 11,200 conversations (35,840 questions); originally 350 seed conversations produced by 70 AMT workers (350 × 32 = 11,200).

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk (AMT) Master Workers; Turkers provided questions, paraphrases, textual surface forms and Wikidata links for seed entities and answers. Authors performed manual quality control and spam prevention and verified random utterances and alignments.

## 🔬 Methodology

**Methods**:
- Automated metrics (P@1, MRR, Hit@5)
- Baseline comparisons (QAnswer, Platypus, Naive, Star/Chain models, Oracle, D2A)
- Model-based evaluation (Convex applied as an enabler to stand-alone KG-QA systems)

**Metrics**:
- Precision at top rank (P@1)
- Mean Reciprocal Rank (MRR)
- Hit@5

**Calculation**: P@1: Precision at the top rank. MRR: Mean Reciprocal Rank. Hit@5: fraction of times a correct answer was retrieved within the top-5 positions.

**Interpretation**: N/A

**Baseline Results**: As reported: QAnswer alone scores about 0.011–0.064 (MRR) on follow-up incomplete utterances; QAnswer + Convex improves to approximately 0.172–0.264 (MRR) across domains. Similar improvements reported for Platypus when augmented with Convex.

**Validation**: A random 20% of the 11k conversations was held out for tuning model parameters (development set), and the remaining 80% was used for testing. The development set was generated from a separate set of seed conversations to prevent leakage.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
