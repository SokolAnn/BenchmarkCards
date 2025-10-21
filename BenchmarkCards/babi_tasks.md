# bAbI tasks

## 📊 Benchmark Details

**Name**: bAbI tasks

**Overview**: A set of proxy tasks that evaluate reading comprehension via question answering. The tasks measure understanding in several ways (e.g., chaining facts, simple induction, deduction) and are designed as prerequisites for any system that aims to be capable of conversing with a human.

**Data Type**: question-answering pairs (synthetic text stories, statements and questions)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi

**Similar Benchmarks**:
- ARISTO
- MCTest
- Winograd Schema Challenge

**Resources**:
- [Resource](http://fb.ai/babi)
- [GitHub Repository](https://github.com/facebook/bAbI-tasks)
- [Resource](https://arxiv.org/abs/1502.05698)

## 🎯 Purpose and Intended Users

**Goal**: To provide a set of synthetic prerequisite tasks to help develop and evaluate learning algorithms for text understanding and reasoning by measuring reading comprehension via question answering.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension
- Coreference Resolution
- Counting
- List/Set Retrieval
- Negation Handling
- Indefinite Knowledge Handling
- Temporal Reasoning
- Deduction
- Induction
- Spatial Reasoning
- Size Reasoning
- Path Finding
- Commonsense Reasoning
- Yes/No Question Answering
- Argument Role Identification

**Limitations**: Tasks are synthetic and not a substitute for real data; vocabulary size is small (approximately 150 words); sentences are relatively short with little nesting; the provided experiments use a stronger form of supervision (supporting facts) than is typically realistic.

**Out of Scope Uses**:
- Hand-coding solutions or using existing large-scale QA systems (e.g., Cyc) is not the intended use since the tasks are designed to evaluate learning algorithms rather than engineered rule-based solutions.

## 💾 Data

**Source**: Generated from a simulation (text-adventure style) that produces grounded statements, questions and answers; 20 synthetic tasks (bAbI) produced by the simulator described in the paper.

**Size**: 20 tasks; each task: 1,000 training examples and 1,000 test examples (default setting reported in experiments).

**Format**: N/A

**Annotation**: Supervision provided as true answers to questions; optionally provides supporting facts for strong supervision (supporting facts provided in training for 'strong supervision' experiments; weak supervision experiments use only question-answer pairs).

## 🔬 Methodology

**Methods**:
- N-gram classifier baseline
- Long Short-Term Memory (LSTM) networks
- Memory Networks (MemNNs) including extensions (adaptive memory, N-grams, nonlinear matching)
- Structured Support Vector Machine (with external NLP resources: coreference and semantic role labeling)

**Metrics**:
- Accuracy

**Calculation**: Report test accuracy (%) on each task using 1,000 test examples per task. A task is considered successfully passed if ≥95% accuracy is obtained.

**Interpretation**: Tasks are noiseless and humans can potentially achieve 100% accuracy. Models achieving ≥95% test accuracy on a task are considered to have passed that task; lower accuracy indicates failure on that task.

**Baseline Results**: Test accuracy (%) per task for the evaluated methods is provided in Table 3 of the paper (N-gram classifier, LSTM, MemNN variants, Structured SVM). The paper reports per-task accuracies and the minimum number of training examples required to reach ≥95% for successful tasks.

**Validation**: Hyperparameters chosen using the training set; evaluation by reporting accuracy on held-out test set (1,000 test examples per task).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
