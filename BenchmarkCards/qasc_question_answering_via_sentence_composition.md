# QASC (Question Answering via Sentence Composition)

## 📊 Benchmark Details

**Name**: QASC (Question Answering via Sentence Composition)

**Overview**: A multi-hop reasoning dataset that requires retrieving facts from a large corpus and composing them to answer multiple-choice questions. QASC provides annotated supporting facts (two facts per question) and their composition, and is designed to emphasize retrieval and sentence-level composition for 2-hop science questions.

**Data Type**: question-answering pairs (text) with annotated supporting facts and a large sentence corpus

**Domains**:
- Natural Language Processing
- Science Education

**Languages**:
- English

**Similar Benchmarks**:
- OpenBookQA
- MultiRC
- WikiHop
- ComplexWebQuestions
- HotPotQA
- DROP
- WorldTree

**Resources**:
- [GitHub Repository](https://github.com/allenai/qasc)
- [Resource](https://arxiv.org/abs/1910.11473)
- [Resource](https://www.ck12.org)
- [Resource](https://spacy.io/)
- [Resource](https://pypi.org/project/spacy-langdetect/)
- [GitHub Repository](https://github.com/LuminosoInsight/python-ftfy)
- [Resource](https://www.elastic.co)

## 🎯 Purpose and Intended Users

**Goal**: To present a dataset focused on sentence-level composition for 2-hop multi-hop question answering: provide 8-way multiple-choice science questions with annotated pairs of supporting facts and composed facts to enable development of retrieval and reasoning models.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Question Answering
- Multi-hop Reasoning
- Information Retrieval
- Entailment (multi-sentence entailment)

**Limitations**: Limited to exactly 2-hop reasoning questions; domain limited to elementary and middle-school level science.

## 💾 Data

**Source**: Questions were crowd-sourced using seed facts FS (selected from WorldTree, a middle-school extension, and CK-12) and a large web-derived corpus FL. Seed facts FS: 928 facts (356 from WorldTree, 123 middle-school extension, 449 from CK-12). Large corpus FL: 17M cleaned sentences produced from processing 73M web documents (281GB) from Clark et al. (2016). Each question is annotated with two supporting facts fS and fL and a composed fact fC.

**Size**: 9,980 questions; 928 seed facts; 17,000,000 sentences (1GB) corpus derived from processing 73,000,000 web documents (281GB). Train/dev/test splits: 8,134 train, 926 dev, 920 test.

**Format**: N/A

**Annotation**: Crowdsourced annotation: supporting facts fS and fL and composed fact fC were created by crowdworkers via a multi-step process with server-side quality checks. Questions were validated by 5 crowdworkers (questions answered incorrectly or deemed unanswerable by >=2 workers were dropped). Adversarial distractor validation: 3 annotators filtered candidate distractors for dev/test sets.

## 🔬 Methodology

**Methods**:
- Two-step information retrieval (IR) over the 17M-sentence corpus
- BERT-based multiple-choice QA fine-tuning (BERT-MCQ)
- Multi-adversary adversarial distractor selection (model-guided)
- Crowdsourcing with automated quality checks

**Metrics**:
- Accuracy
- Recall (retrieval recall of gold supporting facts)

**Calculation**: Accuracy: proportion of questions answered correctly on dev/test splits. Retrieval recall: percentage of questions for which both annotated supporting facts (fS and fL) appear in the top-M retrieved sentences (reported for top-10 sentences).

**Interpretation**: Higher Accuracy indicates better QA performance; authors report a human baseline of 93.0% Accuracy. Two-step retrieval substantially increases retrieval Recall (e.g., 44.4% vs 2.9% for single-step when measuring both facts in top-10) and leads to higher QA Accuracy. A gap of ~20 percentage points to human performance indicates remaining challenge.

**Baseline Results**: Human baseline Accuracy: 93.0%. BERT-MCQ (bert-large-cased) fine-tuned on RACE+SCIquestions with two-step retrieval on FQASC (17M) achieved Dev Accuracy up to 78.0% and Test Accuracy 73.2% (best reported configuration: BERT-LC[WM] two-step, additional fine-tuning on RACE+SCI gave Dev 78.0 / Test 73.2). Simpler non-BERT baselines (GloVe/ESIM variants) performed near random.

**Validation**: Questions were validated by 5 crowdworkers; those answered incorrectly or marked unanswerable by >=2 workers were dropped (reducing collection to 7,660 before adversarial expansion). For adversarial distractors, 3 annotators marked valid distractors; distractors marked valid by at least one annotator were removed. Automated server-side quality checks enforced constraints during crowdsourcing.

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
