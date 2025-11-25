# SimpleQuestions

## 📊 Benchmark Details

**Name**: SimpleQuestions

**Overview**: A large-scale dataset of 108,442 natural-language questions written by human English-speaking annotators, each paired with a corresponding Freebase (FB2M) fact that provides the answer and explains it. Introduced to study coverage of existing QA systems and the impact of multitask and transfer learning for simple question answering.

**Data Type**: question-answering pairs (questions paired with Freebase facts)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WebQuestions
- Reverb

**Resources**:
- [Resource](http://fb.ai/babi)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale dataset for the task of simple question answering to study coverage of QA systems and to investigate multitask and transfer learning for simple QA.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Knowledge Base Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions written by human English-speaking annotators paired with facts from FB2M (an extract of Freebase).

**Size**: 108,442 questions (examples). Split: 75,910 training; 10,845 validation; 21,687 test.

**Format**: N/A

**Annotation**: Human annotation: annotators were shown selected Freebase facts (from FB2M) and asked to phrase a natural-language question involving the subject and relationship, with the object as the answer.

## 🔬 Methodology

**Methods**:
- Automated metrics (path-level accuracy)
- Automated metrics (F1 Score)

**Metrics**:
- Path-level Accuracy
- F1 Score
- Accuracy

**Calculation**: For WebQuestions: F1-score as defined in Berant and Liang (2014) — the average, over all test questions, of the F1-score of the sets of predicted answers. For SimpleQuestions: path-level accuracy where a prediction is correct if the subject and the relationship were correctly retrieved. For Reverb: accuracy defined as the percentage of questions for which the top-ranked candidate fact is correct (re-ranking task).

**Interpretation**: High path-level accuracy indicates correct retrieval of subject and relationship; for WebQuestions F1 reflects overlap between predicted and gold answer sets. The paper notes that on SimpleQuestions the supporting fact is in the candidate set for about 86% of questions, indicating the task remains challenging and current models are effective at re-ranking but do not fully solve simple QA.

**Baseline Results**: Baseline results reported in the paper (test sets): Random guess: WebQuestions F1 1.9%; SimpleQuestions accuracy 4.9%; Reverb accuracy 35%. Berant et al. (2013): WebQuestions F1 31.3%. Bordes et al. (2014b): WebQuestions F1 29.7%; Reverb accuracy 73%. Bordes et al. (2014a) – using path: WebQuestions F1 35.3%; using path+subgraph: 39.2%. Berant and Liang (2014): WebQuestions F1 39.9%. Yang et al. (2014): WebQuestions F1 41.3%. (See Table 4 in paper for full comparative results and Memory Networks variants.)

**Validation**: Hyperparameters chosen to maximize F1 on the WebQuestions validation set; early stopping performed based on validation F1. The dataset split used for SimpleQuestions is 70% train / 10% validation / 20% test. Training used Adagrad with WARP loss and multi-threaded HogWild!; training time reported as 2-3 hours on 20 threads.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
