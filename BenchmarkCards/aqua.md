# AQuA

## 📊 Benchmark Details

**Name**: AQuA

**Overview**: A new 100,000-sample dataset of algebraic word problems that includes questions, multiple-choice answer options, correct answer labels, and natural language answer rationales; created to evaluate models that generate answer rationales and induce arithmetic programs via those rationales.

**Data Type**: question-answer-rationale pairs (text)

**Domains**:
- Natural Language Processing
- Mathematics

**Resources**:
- [GitHub Repository](https://github.com/deepmind/AQuA)
- [Resource](https://arxiv.org/abs/1705.04146)

## 🎯 Purpose and Intended Users

**Goal**: To enable learning to solve algebraic word problems by inducing and modeling programs that generate natural language answer rationales and the final answer.

**Tasks**:
- Question Answering
- Text Generation
- Program Induction

**Limitations**: Generating complex rationales correctly is still an unsolved problem; each additional step adds complexity to inference and decoding.

## 💾 Data

**Source**: 34,202 seed problems collected from exam-style math questions (examples include GMAT and GRE sample questions and web sources) plus 70,318 additional problems crowdsourced from Turkers (Amazon Mechanical Turk) with manual quality checks.

**Size**: 100,949 training examples; 250 development examples; 250 test examples (104,519 problems initially collected before filtering).

**Format**: N/A

**Annotation**: Each example includes the problem description (question), multiple-choice answer options, a natural language rationale, and the correct option label. Seed problems contained rationales; additional problems and rationales were written by crowdworkers with manual subset quality control and duplicate filtering.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Perplexity (average sentence-level perplexity)
- BLEU-4
- Accuracy (percentage of questions where chosen option matches correct one)

**Calculation**: Perplexity is computed as average sentence-level perplexity; when a model cannot generate a token for perplexity computation an unknown token is predicted. BLEU-4 computed as in Papineni et al. (2002). Accuracy is the percentage of questions where the chosen option equals the correct label.

**Interpretation**: Lower Perplexity and higher BLEU-4 indicate better rationale generation quality. Higher Accuracy indicates better ability to select the correct answer (baseline models obtain values close to chance ~20%).

**Baseline Results**: Seq2Seq: Perplexity 524.7, BLEU 8.57, Accuracy 20.8; +Copy Input: Perplexity 46.8, BLEU 21.3, Accuracy 20.4; +Copy Output: Perplexity 45.9, BLEU 20.6, Accuracy 20.2; Our Model: Perplexity 28.5, BLEU 27.2, Accuracy 36.4.

**Validation**: Held-out development set of 250 examples and test set of 250 examples. Heldout replicas manually removed by listing for each heldout instance the closest problems in the training set using character-based Levenshtein distance.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
