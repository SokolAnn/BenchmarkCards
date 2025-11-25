# AI2 Reasoning Challenge (ARC)

## 📊 Benchmark Details

**Name**: AI2 Reasoning Challenge (ARC)

**Overview**: We present a new question set, text corpus, and baselines assembled to encourage AI research in advanced question answering. Together, these constitute the AI2 Reasoning Challenge (ARC), which requires far more powerful knowledge and reasoning than previous challenges such as SQuAD or SNLI.

**Data Type**: question-answering pairs (multiple-choice); text (science sentences / corpus)

**Domains**:
- Natural Language Processing
- Education
- Science

**Similar Benchmarks**:
- SQuAD
- SNLI
- bAbI
- WikiHop
- SciTail
- MCTest
- NewsQA
- CNN/DailyMail
- TriviaQA
- Allen AI Science Challenge (2016)

**Resources**:
- [Resource](http://data.allenai.org/arc)
- [GitHub Repository](https://github.com/allenai/arc-solvers)
- [Resource](http://allenai.org/data.html)

## 🎯 Purpose and Intended Users

**Goal**: To encourage AI research in advanced question answering by providing a new question set, a related science text corpus, and baseline systems, and to pose ARC as a community challenge requiring more powerful knowledge and reasoning.

**Target Audience**:
- AI Researchers
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Multiple-choice Question Answering
- Commonsense Reasoning
- Multihop Reasoning

**Limitations**: The Challenge partition is operationally defined as questions answered incorrectly by both an IR-based solver and a PMI-based solver (an approximation of 'hard' questions). The ARC Corpus often contains relevant knowledge in distributed form (estimated ~95% coverage), but simple retrieval methods may not be able to exploit this evidence.

## 💾 Data

**Source**: Questions drawn from a variety of sources including public standardized tests and other collections (see Table 7), plus an anonymous content partner (referred to as 'Mercury'). The ARC Corpus was mined from the Web using science-related query templates and augmented with the AristoMini corpus.

**Size**: 7,787 questions total (Challenge Set: 2,590 questions; Easy Set: 5,197 questions). ARC Corpus: 14M sentences (1.4GB of text). Train/Dev/Test partitions given in Table 1 (Train: 3,370; Dev: 869; Test: 3,548).

**Format**: N/A

**Annotation**: Questions are authored for human standardized tests and include correct answer labels (multiple-choice, typically 4-way). The Challenge partition was defined by automatic solvers (IR and PMI) failing to answer correctly.

## 🔬 Methodology

**Methods**:
- Automated evaluation with a per-question scoring rubric (including partial credit for ties)
- Baseline system evaluation using retrieval and statistical baselines (IR, PMI)
- Baseline system evaluation using structured and neural models (TableILP, TupleInference, DecompAttn, DGEM, DGEM-OpenIE, BiDAF)
- Use of an information retrieval step to retrieve candidate sentences from a corpus for entailment-based models

**Metrics**:
- Accuracy (reported as percentage correct)

**Calculation**: For each question, a system receives 1 point if it chooses the correct answer and 1/k if it reports a k-way tie that includes the correct answer. The overall score is the sum of points divided by the number of questions and reported as a percentage.

**Interpretation**: Scores are reported as percent correct and compared to a random baseline (Guess-all ≈ 25%). Significance is assessed (paper reports a 95% confidence interval of ±2.5% for the random baseline); systems not significantly above random on the Challenge Set are considered to have not solved the task.

**Baseline Results**: Test set scores (Challenge Set / Easy Set): IR (dataset defn): 1.02% / 74.48%; PMI (dataset defn): 2.03% / 77.82%; IR (using ARC Corpus): 20.26% / 62.55%; TupleInference: 23.83% / 60.81%; DecompAttn: 24.34% / 58.27%; Guess-all ("random"): 25.02% / 25.02%; DGEM-OpenIE: 26.41% / 57.45%; BiDAF: 26.54% / 50.11%; TableILP: 26.97% / 36.15%; DGEM: 27.11% / 58.97%.

**Validation**: Dataset partitioned into Train/Dev/Test (Table 1). Challenge questions are those answered incorrectly by both the IR and PMI solvers. The ARC Corpus relevance was estimated via sampled analyses (informal analysis suggests the corpus mentions knowledge relevant to ~95% of Challenge questions).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Questions vary in target student grade level (as assigned by examiners) from 3rd grade to 9th grade (ages ~8 to 13). Table 2 provides grade-level distribution and counts for Challenge and Easy sets.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
