# DUMB: Dutch Model Benchmark

## 📊 Benchmark Details

**Name**: DUMB: Dutch Model Benchmark

**Overview**: We introduce the Dutch Model Benchmark: DUMB. The benchmark includes a diverse set of datasets for low-, medium- and high-resource tasks (nine tasks, including four newly introduced Dutch datasets). Instead of relying on a mean score across tasks, we propose Relative Error Reduction (RER), which compares the DUMB performance of language models to a strong baseline. Through experiments on 14 pre-trained language models we assess internal consistency of the tasks and identify factors that enable high performance.

**Data Type**: question-answering pairs; token-level tagged text; sentence-pair classification; document-level classification; word-pair classification

**Domains**:
- Natural Language Processing

**Languages**:
- Dutch

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- CLUE
- BasqueGLUE
- RussianSuperGLUE
- KLUE
- FLUE
- JGLUE
- IndoNLU
- ORCA
- XGLUE
- XTREME
- XTREME-R

**Resources**:
- [GitHub Repository](https://github.com/wietsedv/dumb)
- [GitHub Repository](https://github.com/wietsedv/dumb/tree/main/trainers)
- [Resource](https://dumbench.nl)
- [Resource](https://arxiv.org/abs/2305.13026)

## 🎯 Purpose and Intended Users

**Goal**: Create a balanced Dutch benchmark (DUMB) of nine tasks (including four newly introduced Dutch datasets) and propose Relative Error Reduction (RER) as a comparative model evaluation metric; assess the state of Dutch language modeling and provide baseline results and a public leaderboard.

**Target Audience**:
- ML Researchers
- Model Developers
- Researchers in Dutch Natural Language Processing

**Tasks**:
- Part-of-Speech Tagging
- Named Entity Recognition
- Word Sense Disambiguation
- Pronoun Resolution
- Causal Reasoning
- Natural Language Inference
- Sentiment Analysis
- Abusive Language Detection
- Question Answering

**Limitations**: Explicit limitations stated by the authors: (1) The benchmark does not include every NLP task type (e.g., parsing) and some tasks are simplified to classification tasks; (2) Relative Error Reduction (RER) may not be comparable to aggregate scores of other benchmarks; (3) Baseline model comparisons only contain Transformer-encoder models and no generative language models; (4) The model comparison contains more English than Dutch models, limiting some conclusions about monolingual Dutch models.

## 💾 Data

**Source**: Datasets included (as stated in the paper): Part-of-Speech Tagging: Lassy Small v6.0; Named Entity Recognition: SoNaR-1 v1.2.2; Word Sense Disambiguation: DutchSemCor (WiC-NL); Pronoun Resolution: SemEval2010 Task 1 (DPR); Causal Reasoning: COPA-NL (translated COPA); Natural Language Inference: SICK-NL; Sentiment Analysis: Dutch Book Reviews Dataset v3.0 (DBRD); Abusive Language Detection: DALC v2.0; Question Answering: SQuAD-NL (translated SQuAD2.0).

**Size**: POS (Lassy): |Train| 59,167 |Dev| 1,814 |Test| 4,184; NER (SoNaR-1): |Train| 54,472 |Dev| 1,392 |Test| 4,080; WSD (WiC-NL): |Train| 7,184 |Dev| 1,330 |Test| 1,330; PR (DPR): |Train| 786 |Dev| 142 |Test| 1,216; CR (COPA-NL): |Train| 400 |Dev| 100 |Test| 500; NLI (SICK-NL): |Train| 4,439 |Dev| 495 |Test| 4,906; SA (DBRD): |Train| 19,528 |Dev| 500 |Test| 2,224; ALD (DALC): |Train| 6,817 |Dev| 1,205 |Test| 3,270; QA (SQuAD-NL): |Train| 130,319 |Dev| 10,174 |Test| 1,699.

**Format**: N/A

**Annotation**: Lassy: fine-grained POS annotations (CGN guidelines); SoNaR-1: named entity annotations (6 entity classes + negative class); DutchSemCor: Cornetto word sense annotations; SemEval2010 Task 1: coreference annotations used to construct DPR; COPA-NL: Google Translate with two-pass manual correction; SICK-NL: Dutch translation of SICK; DBRD: sentiment labels (positive/negative); DALC v2.0: annotations for anonymized abusive and offensive Twitter messages; SQuAD-NL: translated SQuAD2.0 with post-editing and manual correction of test data by eight BSc students.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Fine-tuning with hyper-parameter grid search
- Multiple runs and averaging (5 random seeds)
- Statistical significance testing using binomial mixed effects regression models

**Metrics**:
- Accuracy
- F1 Score
- Relative Error Reduction (RER)

**Calculation**: Relative Error Reduction (RER) is computed per task as (model_score - baseline_score) / (100% - baseline_score). Example given: baseline 80% and model 85% -> RER = 5% / 20% = 25%. Baseline model used is the Dutch BERTje model.

**Interpretation**: RER expresses percent reduction in error relative to the baseline (Dutch BERTje). Aggregate comparison across tasks uses average RER. Significance testing uses two binomial mixed effects regression models per task with a significance threshold α = 0.05 to compare models against the baseline and against the best-performing model per task.

**Baseline Results**: Baseline model: Dutch BERTje. Per-task baseline scores (test set): POS Accuracy 97.8; NER F1 Score 86.1; WSD Accuracy 65.9; PR Accuracy 65.8; CR Accuracy 62.0; NLI Accuracy 85.2; SA Accuracy 93.3; ALD F1 Score 58.8; QA F1 Score 70.3. Baseline RER per task is 0 by definition for BERTje.

**Validation**: Hyper-parameter grid-search per model and task with optimal hyper-parameters chosen based on validation data; after grid search, fine-tuning re-run with 5 different random seeds and reported scores are averages over the 5 runs. Cross-validation or split strategies described per dataset (e.g., document-level random splits for POS/NER; lemma-based splits for WiC-NL). Statistical significance assessed with binomial mixed effects regression models (item correctness as dependent variable, by-item random intercepts).

## ⚠️ Targeted Risks

**Risk Categories**:
- Legal
- Governance

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Governance**: Lack of testing diversity

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The DALC dataset contains annotations for anonymized abusive and offensive Twitter messages. Other datasets are existing public datasets; detailed privacy/anonymity procedures are not specified beyond dataset descriptions.

**Data Licensing**: Lassy Small v6.0 (custom non-commercial license); SoNaR-1 v1.2.2 (custom non-commercial license); DutchSemCor (CC-BY 3.0); SICK-NL (MIT); DBRD (MIT); DALC v2.0 (GPLv3); SQuAD-NL (CC-BY-SA 4.0). The paper notes that most source datasets use permissive licenses but some restrict redistribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
