# OpenBookQA

## 📊 Benchmark Details

**Name**: OpenBookQA

**Overview**: A new question answering dataset, OpenBookQA, modeled after open book exams. The dataset includes an "open book" set F of 1326 elementary-level science facts and roughly 5957 multiple-choice questions that probe understanding and application of these facts by requiring combining a core fact from F with broad common knowledge obtained from other sources.

**Data Type**: multiple-choice question-answering pairs

**Domains**:
- Natural Language Processing
- Science Education

**Languages**:
- English

**Similar Benchmarks**:
- TQA
- QAngaroo
- NarrativeQA
- MultiRC
- Story Cloze Test
- MCScript
- ProPara
- ARC (AI2 Reasoning Challenge)
- SQuAD
- SciTail
- TriviaQA
- NewsQA
- MCTest

**Resources**:
- [Resource](http://data.allenai.org/OpenBookQA)
- [Resource](https://arxiv.org/abs/1809.02789)
- [GitHub Repository](https://github.com/allenai/ARC-Solvers)
- [Resource](https://allennlp.org)
- [Resource](https://pytorch.org)

## 🎯 Purpose and Intended Users

**Goal**: To provide a new dataset for open book question answering that assesses deeper understanding by requiring systems to combine a provided set of core science facts (open book F) with external common knowledge and multi-hop reasoning.

**Target Audience**:
- Natural Language Processing researchers
- Machine Learning researchers
- Model developers
- NLP community

**Tasks**:
- Question Answering
- Multiple-choice Question Answering
- Multi-hop Reasoning

**Limitations**: The provided open book F is generally insufficient by itself to answer questions; auxiliary facts K are noisy (often incomplete, over-complete, or distantly related) and should not be viewed as gold; some questions (about 21% in a sample) do not actually require the associated core fact; retrieving the correct external common knowledge remains a major open challenge; crowd-sourced authoring introduces human bias/artifacts.

## 💾 Data

**Source**: Questions: 5957 4-way multiple-choice questions (Q). Open book F: 1326 elementary-level science facts (subset of WorldTree corpus filtered from 2287 "central" facts). Auxiliary set K: about 6000 additional (noisy) facts. External knowledge sources referenced: ConceptNet, WordNet, Wikipedia, and a corpus with 14M science-related sentences.

**Size**: 5957 questions; 1326 core facts in F; ~6000 auxiliary facts in K; Train/Dev/Test splits: 4957/500/500

**Format**: N/A

**Annotation**: Created via crowdsourcing on Amazon Mechanical Turk (workers from North America with 'masters' qualification) using a multi-stage pipeline: workers generate questions from a shown core fact and a second common-fact, automatic filters for hardness and uniformity, IR/solver checks to ensure difficulty for retrieval-based systems, a 5-worker answerability check requiring at least 4/5 correct, random shuffling of answer choices to de-bias, and expert filtering for Dev and Test sets.

## 🔬 Methodology

**Methods**:
- Human evaluation (crowd-worker answerability checks and human accuracy estimation)
- Automated metrics (accuracy)
- Oracle experiments (providing gold core fact f and/or additional fact k)
- Evaluation of pre-trained retrieval/IR/ILP/neural baselines
- Neural model training and evaluation with multiple random seeds

**Metrics**:
- Accuracy
- Standard deviation across runs

**Calculation**: For each question, a solver receives 1 point if it chooses the correct answer, and 1/k if it reports a k-way tie that includes the correct answer. Human performance is estimated empirically from the 5-worker annotations and reported as a conservative lower-bound (~H(Q) - 3%) using Hoeffding's inequality. Reported scores are percentages (accuracy) with standard deviation across 5 runs for trained models.

**Interpretation**: Higher accuracy (%) indicates better performance. The paper reports human performance near 92% (conservative estimate) and a random/guess-all baseline of 25%; models approaching human performance indicate strong capability, while scores near 25% indicate random behavior. Oracle experiments (providing gold facts) show improvements, indicating the importance of retrieval and reasoning.

**Baseline Results**: Selected Test accuracies (percentage): Human solver 91.7; Guess All (random) 25.0; TupleInference 17.9; PMI 21.2; TableILP 23.4; DGEM 24.4; IR with F 24.8; Embedd+Sim 41.8; ESIM 48.9 ±1.1; Plausible Answer Detector 49.6 ±0.7; Odd-one-out Solver 50.2 ±1.6; Question Match 50.2 ±0.9; Oracle (f only) 55.8 ±2.3; Oracle (f + k) 76.9 ±0.7. (Standard deviations reported where given in paper.)

**Validation**: Answerability validated by requiring at least 4 out of 5 crowd-workers to answer each candidate question correctly; Dev and Test splits further filtered by in-house expert reviewers; human performance re-checked by obtaining new annotations for random samples; neural model results averaged over 5 runs with different random seeds and best-Dev models evaluated on Test.

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
