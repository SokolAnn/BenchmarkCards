# Social Intelligence QA (SOCIAL IQA)

## 📊 Benchmark Details

**Name**: Social Intelligence QA (SOCIAL IQA)

**Overview**: We introduce SOCIAL IQA, the first large-scale benchmark for commonsense reasoning about social situations. SOCIAL IQA contains 38,000 multiple choice questions for probing emotional and social intelligence in a variety of everyday situations.

**Data Type**: question-answering pairs (text; three-way multiple-choice)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- COPA (Choice of Plausible Alternatives)
- Winograd Schema Challenge
- DPR (Rahman and Ng, 2012)
- CommonsenseQA
- SWAG

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Measure the social and emotional intelligence of computational models through multiple choice question answering (QA) about social situations.

**Tasks**:
- Question Answering
- Commonsense Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Seeded from the ATOMIC knowledge graph and collected via crowdsourcing on Amazon Mechanical Turk (MTurk).

**Size**: 37,588 examples (33,410 train, 1,954 dev, 2,224 test)

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk in a multi-stage pipeline: event rewriting of ATOMIC events, context/question/answer creation (workers provided contexts and two potential correct answers), collection of negative answers via Handwritten Incorrect Answers (HIA) and Question-Switching Answers (QSA), and final QA tuple validation via majority human voting (3 workers for train; 5 workers for dev/test). Adversarial filtering using a deep stylistic classifier was applied to remove easier examples on dev and test.

## 🔬 Methodology

**Methods**:
- Fine-tuning of pretrained language models (OpenAI-GPT, BERT-base, BERT-large)
- Human evaluation (crowd workers selecting correct answer)
- Sequential fine-tuning for transfer learning to downstream commonsense tasks
- Ablation studies (removing context and/or question)

**Metrics**:
- Accuracy
- Effect size (Cohen's d) for valence/arousal/dominance comparisons between answer types

**Calculation**: Accuracy is computed as the percentage of examples where the model-selected answer (the triple with highest softmax-normalized probability) matches the majority-voted correct answer. Human performance measured as percent correct by crowd workers on sampled subsets. Cohen's d calculated to compare VAD means between answer types.

**Interpretation**: Higher Accuracy indicates better social commonsense reasoning. Human performance on sampled subsets is reported as 86.9% (dev) and 84.4% (test) as an approximate upper bound; model accuracies substantially lower (e.g., BERT-large: 66.0% dev, 64.5% test) indicate the task remains challenging for current models.

**Baseline Results**: Random baseline: 33.3% (dev/test). GPT: 63.3% (dev), 63.0% (test). BERT-base: 63.3% (dev), 63.1% (test). BERT-large: 66.0% (dev), 64.5% (test). Ablations for BERT-large: w/o context 52.7% (dev), w/o question 52.1% (dev), w/o context and question 45.5% (dev). Human: 86.9% (dev subset), 84.4% (test subset).

**Validation**: Training QA tuples validated by 3 crowd workers; dev and test QA tuples validated a second time with 5 workers. Correct answers determined by human majority voting; cases without majority vote were discarded. Adversarial filtering applied on dev/test using a stylistic classifier to remove easier examples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
