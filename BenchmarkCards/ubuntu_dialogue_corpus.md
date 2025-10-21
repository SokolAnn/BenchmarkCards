# Ubuntu Dialogue Corpus

## 📊 Benchmark Details

**Name**: Ubuntu Dialogue Corpus

**Overview**: A dataset containing almost 1 million multi-turn two-person conversations (totaling over 7 million utterances and 100 million words) extracted from Ubuntu chat logs, provided as a large resource for research into building dialogue managers based on neural language models. The corpus preserves multi-turn properties of conversations and the unstructured nature of chat-room interactions; benchmark performance is provided on the task of selecting the best next response.

**Data Type**: multi-turn dialogue text (context, response, flag triples / context-response pairs)

**Domains**:
- Natural Language Processing
- Technical Support
- Dialogue Systems

**Similar Benchmarks**:
- Switchboard
- Dialogue State Tracking Challenge (DSTC) datasets
- Twitter Corpus (Ritter et al.)
- Twitter Triple Corpus
- Sina Weibo
- Ubuntu Chat Corpus

**Resources**:
- [Resource](http://irclogs.ubuntu.com/)
- [GitHub Repository](https://github.com/rkadlec/ubuntu-ranking-dataset-creator)
- [GitHub Repository](http://github.com/npow/ubottu)
- [Resource](https://arxiv.org/abs/1506.08909)

## 🎯 Purpose and Intended Users

**Goal**: Provide a very large corpus of unstructured multi-turn dialogues to enable research into dialogue systems (especially neural-network based dialogue managers) and to provide a benchmark for the task of selecting the best next response.

**Target Audience**:
- Machine Learning Researchers
- Dialogue System Researchers
- Model Developers

**Tasks**:
- Response Selection (Next Utterance Selection)
- Next Utterance Classification
- Multi-turn Dialogue Modeling

**Limitations**: Conversation disentanglement is performed with heuristic rules which may be imperfect; initial questions can appear multiple times across dialogues when multiple users respond; dialogues spanning long time periods are treated as a single dialogue (posting time included so others may filter); conversations longer than five utterances where one user says >80% of utterances are discarded; only extracted dialogues with 3 or more turns are retained; no further preprocessing (e.g., tokenization, stemming) is applied to the released corpus.

## 💾 Data

**Source**: Extracted from Ubuntu Chat Logs (Freenode IRC network) used for Ubuntu-related technical support; logs available for 2004-2015 at http://irclogs.ubuntu.com/.

**Size**: 930,000 dialogues; 7,100,000 utterances; 100,000,000 words (as reported in Table 2).

**Format**: Raw text with extracted (context, response, flag) triples for the test set; posting time included; released without additional preprocessing.

**Annotation**: Automatically derived via extraction heuristics; test set contains (context, response, flag) where flag is a Boolean indicating whether the response is the actual next utterance; negative responses sampled randomly. No human annotation.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation using Recall@k
- Model-based evaluation (TF-IDF baseline, Recurrent Neural Network, Long Short-Term Memory network)
- Train/test split with 2% of conversations set aside as test set; validation set extracted from training for hyper-parameter tuning

**Metrics**:
- Recall@1
- Recall@2
- Recall@5

**Calculation**: Test set constructed by extracting (context, response, flag) triples from dialogues; for each context one correct response (flag=1) and one or more false responses (flag=0) sampled randomly from the test set (experiments used 1 false response and 9 false responses). Recall@k: agent selects k most likely responses and is correct if the true response is among these k candidates.

**Interpretation**: Higher Recall@k indicates better ability to select the true next utterance given a context. Authors note that good performance on response classification is not necessarily a gauge of generation quality, but improvements on classification may lead to generation improvements.

**Baseline Results**: TF-IDF, RNN, LSTM results (Table 4): 1 in 2 R@1 — TF-IDF 65.9%, RNN 76.8%, LSTM 87.8%. 1 in 10 R@1 — TF-IDF 41.0%, RNN 40.3%, LSTM 60.4%. 1 in 10 R@2 — TF-IDF 54.5%, RNN 54.7%, LSTM 74.5%. 1 in 10 R@5 — TF-IDF 70.8%, RNN 81.9%, LSTM 92.6%.

**Validation**: 2% of conversations randomly selected as a test set; a validation set was extracted from the training data for hyper-parameter optimization; training examples created by treating each utterance (from third onward) as a potential response with previous utterances as context; negative responses sampled randomly.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
