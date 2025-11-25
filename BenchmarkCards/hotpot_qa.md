# HOTPOT QA

## 📊 Benchmark Details

**Name**: HOTPOT QA

**Overview**: HOTPOT QA is a new dataset with 113k Wikipedia-based question-answer pairs with four key features: (1) the questions require finding and reasoning over multiple supporting documents to answer; (2) the questions are diverse and not constrained to any pre-existing knowledge bases or knowledge schemas; (3) sentence-level supporting facts required for reasoning are provided, allowing QA systems to reason with strong supervision and explain predictions; (4) includes a new type of factoid comparison questions to test ability to extract relevant facts and perform necessary comparison.

**Data Type**: text (question-answering pairs with sentence-level supporting facts)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- TriviaQA
- SearchQA
- QAngaroo
- COMPLEX WEBQUESTIONS
- MS MARCO

**Resources**:
- [Resource](https://HotpotQA.github.io)
- [Resource](https://arxiv.org/abs/1809.09600)

## 🎯 Purpose and Intended Users

**Goal**: Facilitating the development of QA systems capable of performing explainable, multi-hop reasoning over diverse natural language; providing sentence-level supporting facts and comparison questions to enable explainable predictions and test multi-hop reasoning.

**Tasks**:
- Question Answering
- Supporting Fact Prediction
- Information Retrieval

**Limitations**: Authors note that approximately 6% of sampled questions can be answered with one paragraph (single-hop) and 2% unanswerable; supporting facts have lower annotator agreement and can be subjective. The authors also note that train-medium contains examples that models could answer with sufficient training and that incorporating supporting-fact supervision in their model is likely suboptimal.

## 💾 Data

**Source**: Collected by crowdsourcing (Amazon Mechanical Turk) based on English Wikipedia articles (Wikipedia dump of October 1, 2017) using a Wikipedia hyperlink graph and curated candidate paragraph pairs.

**Size**: 112,779 examples

**Format**: Extracted text and hyperlinks (WikiExtractor output) with sentence boundaries from Stanford CoreNLP

**Annotation**: Crowdsourced via Amazon Mechanical Turk; workers provided questions, answer spans, and sentence-level supporting facts (supporting fact sentences)

## 🔬 Methodology

**Methods**:
- Model-based evaluation (baseline neural QA model with multi-task supporting-fact supervision)
- Automated retrieval evaluation (bigram tf-idf retrieval and inverted-index filtering for full wiki setting)
- Human evaluation (additional Turkers to establish human performance and supporting facts)

**Metrics**:
- Exact Match (EM)
- F1
- Supporting facts Exact Match (EM)
- Supporting facts F1
- Joint Exact Match (Joint EM)
- Joint F1
- Mean Average Precision (MAP)
- Mean Rank
- Hits@k

**Calculation**: Answer EM and F1 follow SQuAD-style evaluation. Supporting-fact EM and F1 evaluate predicted supporting fact sentences against gold set. Joint metrics computed per example as: P(joint)=P(ans) * P(sup); R(joint)=R(ans) * R(sup); Joint F1 = 2 * P(joint) * R(joint) / (P(joint) + R(joint)). Joint EM is 1 only if both answer and supporting facts achieve exact match; otherwise 0. All metrics are evaluated example-by-example and averaged over examples.

**Interpretation**: Joint metrics penalize systems that perform poorly on either answer prediction or supporting-fact prediction, emphasizing both correctness and explainability. Lower performance in the full wiki setting indicates greater retrieval difficulty; human performance is substantially higher than baseline models, indicating room for improvement.

**Baseline Results**: Distractor test (model with strong supervision): Answer EM 45.46, Answer F1 58.99; Supporting-fact EM 22.24, Supporting-fact F1 66.62; Joint EM 12.04, Joint F1 41.37. Full wiki test (model): Answer EM 25.23, Answer F1 34.40; Supporting-fact EM 5.07, Supporting-fact F1 40.69; Joint EM 2.63, Joint F1 17.85. Human (sample of 1,000): Human EM 83.60, Human F1 91.40; Supporting-fact EM 61.50, Supporting-fact F1 90.04; Joint EM 52.30, Joint F1 82.55. (Numbers taken from Tables 4 and 8 in the paper.)

**Validation**: Data splits created using sampling and three-fold cross validation on multi-hop examples; train-easy identified by sampling top-contributing Turkers and labeling examples that overwhelmingly required single-paragraph reasoning; train-medium identified by model correctly answering 60% of multi-hop examples in cross-validation; remaining hard examples divided into train-hard, dev, test-distractor, and test-fullwiki. Human validation: for 1,000 sampled examples, at least three additional Turkers provided answers and supporting facts to establish human performance and inter-annotator agreement.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
