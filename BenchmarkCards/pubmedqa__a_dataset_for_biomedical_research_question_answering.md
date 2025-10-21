# PubMedQA: A Dataset for Biomedical Research Question Answering

## 📊 Benchmark Details

**Name**: PubMedQA: A Dataset for Biomedical Research Question Answering

**Overview**: We introduce PubMedQA, a novel biomedical question answering (QA) dataset collected from PubMed abstracts. The task of PubMedQA is to answer research questions with yes/no/maybe using the corresponding abstracts. PubMedQA has 1k expert-annotated, 61.2k unlabeled and 211.3k artificially generated QA instances. Each instance is composed of (1) a question (original research article title or derived from one), (2) a context (the corresponding abstract without its conclusion), (3) a long answer (the conclusion of the abstract), and (4) a yes/no/maybe answer which summarizes the conclusion. PubMedQA is intended to require reasoning over biomedical research texts, especially their quantitative contents.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- N/A

**Similar Benchmarks**:
- BioASQ
- emrQA
- BioRead
- BMKC
- HotpotQA
- Natural Questions
- ShARC
- BoolQ

**Resources**:
- [Resource](https://pubmedqa.github.io)
- [Resource](https://arxiv.org/abs/1909.06146)

## 🎯 Purpose and Intended Users

**Goal**: To build a biomedical QA dataset for answering research questions using yes/no/maybe where reasoning over biomedical research texts, especially quantitative contents, is required; and to serve as a benchmark for testing scientific reasoning abilities of machine reading comprehension models.

**Target Audience**:
- Researchers developing machine reading comprehension models

**Tasks**:
- Question Answering
- Machine Reading Comprehension
- Yes/No/Maybe Classification

**Limitations**: Articles of PubMedQA are biased towards clinical study-related topics (Appendix B). Approximately 21% of PubMedQA contexts contain no natural language descriptions of numbers. PQA-A (automatically generated subset) is imbalanced (92.8% yes vs 7.2% no). The labeled subset (PQA-L) contains 1,000 expert-annotated instances.

## 💾 Data

**Source**: Collected from PubMed articles: question titles and structured abstracts (abstracts with conclusive parts). PQA-L: 1k instances manually labeled by two annotators (qualified M.D. candidates) following Algorithm 1. PQA-U: 61.2k unlabeled instances filtered by rule-based method. PQA-A: 211.3k automatically generated instances from statement titles using a heuristic.

**Size**: PQA-L: 1,000 labeled examples; PQA-U: 61,200 unlabeled examples; PQA-A: 211,300 automatically generated examples (total ~273,500 instances).

**Format**: N/A

**Annotation**: PQA-L: Manual annotation by two annotators (qualified M.D. candidates) following Algorithm 1 (one annotator had access to long answer, the other did not; disagreements discussed to reach ground truth). PQA-U: filtered with a rule-based method. PQA-A: automatically generated via heuristic converting statement titles to questions and labeling using negation status.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based baseline evaluation (fine-tuning BioBERT and other models)

**Metrics**:
- Accuracy
- Macro-F1

**Calculation**: Main metrics are Accuracy and Macro-F1 on the PQA-L test set using question and context as input. Human performance measured via annotator agreement against discussed ground truth labels (reasoning-free and reasoning-required settings).

**Interpretation**: Higher Accuracy and Macro-F1 indicate better performance on PQA-L under the reasoning-required setting (question+context input). Single-human performance (single annotator) under reasoning-required setting is reported as 78.0% Accuracy and 72.19% Macro-F1; majority baseline is 55.2% Accuracy. Model performance is compared against these baselines.

**Baseline Results**: Multi-phase fine-tuning of BioBERT with long answer bag-of-word supervision achieves 68.1% Accuracy (reported in abstract). Single-human performance (single annotator) is 78.0% Accuracy. Majority-baseline is 55.2% Accuracy. (See Table 5 for detailed model/tabled results under different training schedules.)

**Validation**: 500 randomly sampled PQA-L instances are used for 10-fold cross validation and the remaining 500 instances constitute the PubMedQA test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
