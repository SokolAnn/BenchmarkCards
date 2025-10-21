# Swag : A Large-Scale Adversarial Dataset for Grounded Commonsense Inference

## 📊 Benchmark Details

**Name**: Swag : A Large-Scale Adversarial Dataset for Grounded Commonsense Inference

**Overview**: We introduce the task of grounded commonsense inference, unifying natural language inference and commonsense reasoning. We present Swag, a new dataset with 113k multiple choice questions about a rich spectrum of grounded situations.

**Data Type**: text (multiple-choice sentence completion / question-answering pairs: context and candidate sentence endings)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SNLI
- MultiNLI
- COPA
- RocStories
- JOCI
- Visual Madlibs

**Resources**:
- [Resource](https://rowanzellers.com/swag)
- [Resource](https://arxiv.org/abs/1808.05326)

## 🎯 Purpose and Intended Users

**Goal**: To create a large-scale dataset for studying physically grounded commonsense inference and to provide a challenging, de-biased benchmark for evaluating models on grounded commonsense reasoning.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Question Answering
- Natural Language Inference
- Sentence Completion
- Commonsense Reasoning (grounded)

**Limitations**: Adversarial Filtering focuses on reducing stylistic annotation artifacts but may leave subtle artifacts; dataset is not perfect in avoiding gender and racial biases due to biases in movie data; some examples were collected with only a single annotator after validation checks.

## 💾 Data

**Source**: Derived from pairs of consecutive video captions from ActivityNet Captions and the Large Scale Movie Description Challenge (LSMDC).

**Size**: 113,557 multiple-choice questions (reported in paper as 113k), split as 73,000 training, 20,000 validation, 20,000 test; Sentence pairs: ActivityNet 51,439; LSMDC 62,118; Unique contexts 92,221; Unique endings 452,683.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk: workers labeled candidate endings as 'likely', 'unlikely', or 'gibberish' and selected best and second-best endings. Some examples have multiple annotators for validation; remaining examples were collected with one annotator after periodic verification. Annotators were screened and monitored; dataset cost reported as $23,000 (≈ $0.20 per example).

## 🔬 Methodology

**Methods**:
- Automated metrics (model accuracy evaluations using multiple NLI and classification models)
- Human evaluation (Mechanical Turk validation and human baseline measurement)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed as the percentage of examples where the model selects the gold (human-verified) ending (model selects argmax over candidate endings). Human accuracy computed via majority vote among Mechanical Turk workers (reported for 1, 3, and 5 turkers) and expert annotator.

**Interpretation**: Higher Accuracy indicates better ability to pick the most plausible next event/ending given the context. Human performance (five turkers majority vote) is reported as an approximate upper bound (88%). Substantially lower model accuracy compared to humans indicates remaining challenge in grounded commonsense inference.

**Baseline Results**: Best reported model: ESIM + ELMo obtains up to 59.2% accuracy (test) when trained on found+generated data. Unary/binary baselines report lower accuracy (e.g., LSTM+ELMo ≈ 50.4% when context included). Human performance: 1 turker 82.8% (on sampled set), 3 turkers 85.1%, 5 turkers 88.0%, expert 85.0%.

**Validation**: Dataset split into 73k train / 20k validation / 20k test. Adversarial Filtering (AF) used iterative train/test splits (AF uses an 80%/20% split during iterations) with an ensemble of stylistic classifiers to filter negatives. Final candidate endings were verified via Mechanical Turk; periodic verification and worker screening were used to maintain quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Annotation artifacts (stylistic biases)', 'Overestimation of model performance due to dataset artifacts', 'Demographic biases (gender and racial bias stemming from source movie data)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
