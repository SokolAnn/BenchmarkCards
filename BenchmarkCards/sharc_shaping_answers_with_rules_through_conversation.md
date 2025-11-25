# ShARC (Shaping Answers with Rules through Conversation)

## 📊 Benchmark Details

**Name**: ShARC (Shaping Answers with Rules through Conversation)

**Overview**: A dataset for the task of conversational machine reading: given an input question, a supporting rule text snippet, a scenario (context) and a dialog history, predict the answer (YES / NO / IRRELEVANT) or, if necessary, generate a follow-up question. The paper formalises the task, develops a crowdsourcing annotation protocol, and provides a corpus of over 32k conversational machine reading utterances from real-world rules.

**Data Type**: question-answering pairs with supporting rule text, scenarios, and dialog histories (text)

**Domains**:
- Legal
- Public Services

**Similar Benchmarks**:
- SQuAD
- SNLI
- QuAC
- CoQA

**Resources**:
- [Resource](https://sharc-data.github.io)
- [Resource](https://arxiv.org/abs/1809.01494)

## 🎯 Purpose and Intended Users

**Goal**: To introduce the task of conversational machine reading, provide evaluation metrics and an annotation protocol, and release a corpus (ShARC) to study the challenges of interpreting natural language rules in dialog and to benchmark models.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Question Generation
- Natural Language Inference (Entailment)
- Dialog-based Question Answering

**Limitations**: The authors note the dataset size may be insufficient for training end-to-end neural models ("One may argue that the size of the dataset is not sufficient for training end-to-end neural models"). They also state that the data "is biased in the sense that when a scenario is given, at least one of the follow-up questions in a dialog can be answered", and they report measured annotation/noise rates for negative sampling and other sources (see Appendix B and D).

## 💾 Data

**Source**: 264 unique sources from 10 domains (listed in Appendix C). Example source URLs included in the corpus: http://legislature.maine.gov/, https://esd.wa.gov/, https://www.benefits.gov/, https://www.dmv.org/, https://www.doh.wa.gov/, https://www.gov.uk/, https://www.humanservices.gov.au/, https://www.irs.gov/, https://www.usa.gov/, https://www.uscis.gov/.

**Size**: 32,436 utterances; 948 distinct rule-text snippets (trees); 6,637 scenarios; 264 sources. Dataset splits: 21,890 training utterances, 2,270 development utterances, 8,276 test utterances.

**Format**: N/A

**Annotation**: Multi-stage crowdsourced annotation protocol suitable for Amazon Mechanical Turk: Rule Text Extraction, Question Generation (currently by expert annotators), Dialog Generation (annotators interacting with a 'virtual user' producing random YES/NO answers to traverse dialog branches), and Scenario Annotation. Includes qualification tests, re-annotation, back-validation, sampling-based validation, and expert curation of development and test sets. Payment and cost details are reported per annotation stage.

## 🔬 Methodology

**Methods**:
- Automated metrics (micro- and macro- averaged accuracies, BLEU)
- Human evaluation (annotator agreement metrics, user study)
- Baseline machine-learning models (Random Forest, Logistic Regression, Convolutional Neural Network, seq2seq / NMT-Copy)
- Neural QA / entailment models (BiDAF, Decomposed Attention Model trained on SNLI and ShARC)
- Rule-based heuristics

**Metrics**:
- Micro-averaged Accuracy
- Macro-averaged Accuracy
- BLEU-1
- BLEU-2
- BLEU-3
- BLEU-4
- Fleiss' Kappa
- Cohen's Kappa
- Human Accuracy

**Calculation**: For classification tasks the paper uses micro- and macro- averaged accuracies. For follow-up question generation BLEU scores (orders 1,2,3,4) are computed between gold follow-up questions and model-predicted follow-up questions. Annotator agreement is measured with Fleiss' Kappa and Cohen's Kappa. Human accuracy on the classification sub-task is computed using a methodology where the second annotator's answer is considered the prediction and the majority vote is taken as ground truth (following Rajpurkar et al., 2016).

**Interpretation**: Higher micro/macro accuracy indicates better classification performance; higher BLEU indicates closer match to gold follow-up questions. The paper reports a human classification accuracy of 93.9% and notes that baseline models achieve substantially lower scores, indicating substantial room for improvement, especially on macro accuracy and scenario interpretation.

**Baseline Results**: Selected baseline results reported in the paper: Classification (no scenarios) - Random: Micro 0.254 Macro 0.250; Surface LR: Micro 0.555 Macro 0.511; Heuristic: Micro 0.791 Macro 0.779; Random Forest: Micro 0.808 Macro 0.797; CNN: Micro 0.677 Macro 0.681. Follow-up generation (BLEU): First Sentence BLEU-1 0.221; NMT-Copy BLEU-1 0.339; BiDAF BLEU-1 0.450; Rule-based BLEU-1 0.533. Entailment (scenario interpretation): DAM (SNLI) Micro 0.479 Macro 0.362; DAM (ShARC) Micro 0.492 Macro 0.322. Conversational Machine Reading end-to-end: Combined Model Micro 0.619 Macro 0.689 BLEU-1 0.544 BLEU-4 0.344; NMT Micro 0.448 Macro 0.428 BLEU-1 0.340 BLEU-4 0.078. Human accuracy (classification sub-task) reported as 93.9%.

**Validation**: Multiple validation procedures: re-annotation of irregular dialog tree nodes, annotator validation of previous dialog parts, qualification tests for workers, restrict worker location and approval-rate thresholds, validation sampling to compute worker quality scores, expert validation of sampled annotations, and manual curation of development and test instances prone to errors. The paper reports agreement figures and measured noise rates for various negative sampling procedures in Appendix B and D.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
