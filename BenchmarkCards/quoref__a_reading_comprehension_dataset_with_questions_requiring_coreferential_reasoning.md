# QUOREF: A Reading Comprehension Dataset with Questions Requiring Coreferential Reasoning

## 📊 Benchmark Details

**Name**: QUOREF: A Reading Comprehension Dataset with Questions Requiring Coreferential Reasoning

**Overview**: A crowd-sourced dataset containing more than 24K span-selection questions that require resolving coreference among entities in over 4.7K English paragraphs from Wikipedia, designed to evaluate coreference-aware reading comprehension.

**Data Type**: question-answering pairs (span-selection answers)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- DROP
- RACE
- TriviaQA
- MS MARCO
- Natural Questions
- MCTest

**Resources**:
- [Resource](https://allennlp.org/quoref)
- [Resource](https://arxiv.org/abs/1908.05803v2)

## 🎯 Purpose and Intended Users

**Goal**: A focused reading comprehension benchmark that evaluates the ability of models to resolve coreference.

**Tasks**:
- Reading Comprehension
- Question Answering
- Coreference Resolution

**Limitations**: The notion of coreference captured is less comprehensive than traditional coreference datasets (it focuses on coreference between a few spans rather than complete coreference clusters); the dataset may contain predictive/annotation artifacts.

## 💾 Data

**Source**: Paragraphs scraped from English Wikipedia articles about English movies, art and architecture, geography, history, and music; crowdsourced questions written by Mechanical Turk workers.

**Size**: 24,354 questions (Train: 19,399; Dev: 2,418; Test: 2,537); 4,702 paragraphs (Train: 3,771; Dev: 454; Test: 477)

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk; workers wrote questions and selected one or more answer spans in the paragraph. An adversary model (uncased base BERT QA trained on SQuAD 1.1) ran during collection to filter questions that the model could answer.

## 🔬 Methodology

**Methods**:
- Automated metrics (Exact Match and F1)
- Baseline model evaluation (reading comprehension models and heuristic baselines)
- Human evaluation (authors answered a sample of test questions to estimate human performance)

**Metrics**:
- Exact Match (EM)
- F1 Score (macro-averaged F1 as used in DROP)

**Calculation**: EM implemented the same way as SQuAD. F1 measures overlap between a bag-of-words representation of the gold and predicted answers, employing the F1 metric used for DROP (macro-averaged).

**Interpretation**: Higher EM and F1 indicate better reading comprehension. State-of-the-art models perform substantially worse than humans on QUOREF (best model F1 ~70.5 vs. estimated human F1 ~93.4), indicating the dataset is challenging for coreferential reasoning.

**Baseline Results**: Test set F1: XLNet QA 70.51, BERT QA 66.39; Test set EM: XLNet QA 61.88, BERT QA 59.28. Human performance (estimated on 400 test questions): F1 93.41, EM 86.75. (See paper Table 3 for additional baselines including QANet, QANet+BERT, and passage-only heuristics.)

**Validation**: Manual analysis of a random sample of 100 paragraph-question pairs (found 78% require coreference resolution). Human performance estimated from authors' answers to 400 test questions scored with the same metrics used for systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
