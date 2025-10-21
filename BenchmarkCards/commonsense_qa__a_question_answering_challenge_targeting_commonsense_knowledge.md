# COMMONSENSE QA: A Question Answering Challenge Targeting Commonsense Knowledge

## 📊 Benchmark Details

**Name**: COMMONSENSE QA: A Question Answering Challenge Targeting Commonsense Knowledge

**Overview**: A challenging new dataset for commonsense question answering. Questions are generated from ConceptNet by sampling a source concept and multiple target concepts with the same ConceptNet relation, and crowd-workers author multiple-choice questions that require commonsense/background knowledge. The dataset contains 12,247 questions and is intended to investigate question answering that requires prior knowledge.

**Data Type**: question-answering pairs (multiple-choice, text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SWAG
- VCR
- Winograd Schema Challenge
- COPA
- Story Cloze Test (ROC Stories)
- SQUABU

**Resources**:
- [Resource](https://www.tau-nlp.org/commonsenseqa)
- [GitHub Repository](https://github.com/jonathanherzig/commonsenseqa)
- [Resource](https://arxiv.org/abs/1811.00937)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset that tests commonsense knowledge in question answering and to investigate question answering that requires prior/background knowledge (commonsense) beyond a provided context.

**Target Audience**:
- Natural Language Processing researchers
- Machine Learning researchers

**Tasks**:
- Question Answering
- Multiple-choice Question Answering
- Commonsense Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from ConceptNet triplets (ConceptNet) by selecting subgraphs with one source concept and three target concepts sharing the same relation, followed by crowdsourced question generation and verification via Amazon Mechanical Turk. Web snippets (Google search result snippets) were retrieved as additional context for each question.

**Size**: 12,247 examples

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk: workers authored three questions per ConceptNet subgraph, added two distractors per question (one from ConceptNet, one authored), and a disjoint group of trained workers verified each question (each question verified by 2 workers); only questions verified by at least one worker who answered correctly were retained. Annotator qualification: workers whose ≥75% of formulated questions passed verification were accepted.

## 🔬 Methodology

**Methods**:
- Automated evaluation of models (baseline and fine-tuned models)
- Reading comprehension evaluation using web snippets as context
- Human evaluation (majority vote over 5 workers for sampled questions)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of examples for which the model's prediction is correct (reported on the test set).

**Interpretation**: Higher Accuracy indicates better performance. Human performance (majority vote) is 88.9%. Random guessing accuracy is 20%. The best model (BERT-LARGE) achieves 55.9% on the random split, substantially lower than human performance, indicating that closer-to-human performance is desired.

**Baseline Results**: Selected test set results (random split): BERT-LARGE: 55.9% accuracy; GPT: 45.5% accuracy; VECSIM+NUMBERBATCH: 29.1%; BIDAF++: 32.0%. Human (majority vote on sampled questions): 88.9%. (Full table of baselines and SANITY mode results reported in paper.)

**Validation**: Data split into training/development/test with an 80/10/10 split; two split types used (random split and question concept split). Question quality verification: each question was verified by 2 workers and only questions with at least one correct verifier were retained (this filtering removed 15% of formulated questions). Human evaluation for accuracy measured on 100 random questions with 5 workers each (workers not involved in generation).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
