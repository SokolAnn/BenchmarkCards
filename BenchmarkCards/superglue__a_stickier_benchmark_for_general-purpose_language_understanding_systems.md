# SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems

## 📊 Benchmark Details

**Name**: SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems

**Overview**: SuperGLUE is a new benchmark styled after GLUE with a new set of more difficult language understanding tasks, a software toolkit, and a public leaderboard.

**Data Type**: text: question-answering pairs, sentence/sentence-pair classification, coreference resolution

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SentEval
- DecaNLP

**Resources**:
- [Resource](https://super.gluebenchmark.com)
- [GitHub Repository](https://github.com/nyu-mll/jiant)
- [GitHub Repository](https://github.com/huggingface/transformers)
- [Resource](https://arxiv.org/abs/1905.00537v3)

## 🎯 Purpose and Intended Users

**Goal**: To provide a simple, hard-to-game measure of progress toward general-purpose language understanding technologies for English.

**Target Audience**:
- Machine Learning Researchers

**Tasks**:
- Question Answering
- Natural Language Inference
- Word Sense Disambiguation
- Coreference Resolution
- Reading Comprehension

**Limitations**: Excludes tasks that require domain-specific knowledge (e.g., medical notes or scientific papers); requires tasks to have existing public training data; focuses on English.

**Out of Scope Uses**:
- Tasks requiring domain-specific knowledge (e.g., medical notes or scientific papers)

## 💾 Data

**Source**: Existing public datasets assembled for the benchmark: BoolQ, CommitmentBank (CB), COPA, MultiRC, ReCoRD, RTE (merged RTE1/2/3/5), WiC, and WSC (as listed in Table 1).

**Size**: Per-task sizes as listed in Table 1. Examples: BoolQ: 9,427 train / 3,270 dev / 3,245 test; CB: 250 train / 57 dev / 250 test; COPA: 400 train / 100 dev / 500 test; MultiRC: 5,100 train / 953 dev / 1,800 test; ReCoRD: 101,000 train / 10,000 dev / 10,000 test; RTE: 2,500 train / 278 dev / 300 test; WiC: 6,000 train / 638 dev / 1,400 test; WSC: 554 train / 104 dev / 146 test.

**Format**: N/A

**Annotation**: Original task datasets were annotated by their respective authors/creators. Human performance estimates for the benchmark were collected via crowdsourced annotations on Amazon Mechanical Turk (workers received training, 5 annotations per sampled test example, majority vote).

## 🔬 Methodology

**Methods**:
- Automated metrics (task-specific)
- Human evaluation (crowdsourced estimates for human baselines)
- Baseline model evaluation using BERT and transfer variants
- Public leaderboard evaluation with private test labels

**Metrics**:
- Accuracy
- F1 Score
- Exact Match (EM)
- Matthews Correlation Coefficient (MCC)
- Gender Parity Score
- Average (equal-weighted across tasks)

**Calculation**: Each task is weighted equally in the overall score. For tasks with multiple metrics, those metrics are averaged to produce a per-task score; the benchmark score is the unweighted average of the task scores.

**Interpretation**: Higher scores indicate better task and aggregate performance. Human performance estimates are provided as reference points to indicate headroom; gaps between model and human scores indicate remaining difficulty.

**Baseline Results**: Baselines reported in the paper (test set, scaled by 100): BERT (bert-large-cased) Avg: 69.0; BERT++ Avg: 71.5; Human (est.) Avg: 89.8. Per-task scores are given in Table 3 of the paper.

**Validation**: Tasks were selected via a public call and filtered using BERT-based baselines and human baselines. Human performance was estimated by sampling test examples (typically 100) and collecting 5 annotations per example via Mechanical Turk with a training phase; majority vote used to estimate human accuracy. The leaderboard uses private test labels and limits submissions to reduce overfitting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Transparency
- Data Laws
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Data Laws**: Data usage restrictions
- **Governance**: Incomplete usage definition, Unrepresentative risk testing

**Demographic Analysis**: Includes Winogender diagnostic to measure gender bias; paper notes Winogender used (DNC version) does not cover gender-neutral 'they' or non-binary pronouns.

**Potential Harm**: ['Detection of gender bias in coreference resolution systems', 'Monitoring amplification of social biases in data-driven models']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Task data must be available under licenses that allow use and redistribution for research purposes (as stated in the design criteria).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
