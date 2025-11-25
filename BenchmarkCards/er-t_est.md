# ER-T EST

## 📊 Benchmark Details

**Name**: ER-T EST

**Overview**: ER-T EST is a framework for evaluating explanation regularization (ER) models' out-of-distribution (OOD) generalization along three dimensions: unseen dataset tests, contrast set tests, and functional tests. It is designed to analyze how ER design choices (rationale extractor, alignment criterion, human rationale type, instance selection, annotation time) affect ID and OOD performance.

**Data Type**: text (text classification instances with extractive token-level rationales; contrast set perturbations of real-world text; synthetic functional test instances created from templates)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- Contrast Set Tests (Gardner et al., 2020)
- Functional Tests / CheckList (Ribeiro et al., 2020)
- ERASER

**Resources**:
- [GitHub Repository](https://github.com/INK-USC/ER-Test)
- [Resource](https://arxiv.org/abs/2205.12542)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified evaluation framework (ER-T EST) for measuring how explanation regularization methods affect language models' out-of-distribution generalization via: (A) unseen dataset tests, (B) contrast set tests, and (C) functional tests.

**Tasks**:
- Text Classification
- Sentiment Analysis
- Natural Language Inference
- Named Entity Recognition
- Hate Speech Detection

**Limitations**: Contrast set tests and functional tests are generally expensive to create and not many tasks have pre-constructed tests available. Certain tests in ER-T EST may not be applicable to all NLP tasks (e.g., constructing contrast sets for token classification is not straightforward). ER-T EST covers a limited region in the space of OOD evaluation.

**Out of Scope Uses**:
- Token classification tasks (e.g., Named Entity Recognition) — constructing contrast set tests for token classification is not straightforward, which limits applicability to sequence classification tasks.

## 💾 Data

**Source**: Datasets used (as stated in the paper): SST (Short movie reviews), Yelp, Amazon, Movies (long movie reviews), e-SNLI, MNLI, IMDb (contrast sets), Flights (functional tests), Linguistically-Informed Transformations (LIT) (contrast sets for NLI), ANLP-NLI (functional tests for NLI), CoNLL-2003, OntoNotes v5.0, Stormfront (Stf), HatEval, Gab Hate Corpus (GHC). Task-level lexicons used: AFINN and SenticNet. User study data: Amazon Mechanical Turk annotations (time study).

**Size**: N/A

**Format**: N/A

**Annotation**: Instance-level human rationales: manual extractive token-level annotations by humans (instance-level). Task-level human rationales: distantly-supervised rationales generated via task lexicons (AFINN, SenticNet) applied across instances. User study annotations collected via Amazon Mechanical Turk (three Turkers per instance for time estimates; an initial training set D_init of 1000 instances used in time-budget experiments).

## 🔬 Methodology

**Methods**:
- Unseen dataset tests (evaluate model on datasets beyond training distribution)
- Contrast set tests (evaluate model on manually perturbed counterfactual instances; use contrast consistency metric)
- Functional tests (evaluate model on synthetic template-based tests covering Vocabulary, Robustness, Logic, Entity)
- Human annotation study (Amazon Mechanical Turk) for annotation time budgets
- Statistical significance testing (unpaired Welch's t-test, p < 0.05)

**Metrics**:
- Accuracy
- Macro F1
- Contrast consistency
- Failure rate
- Normalized failure rate (min-max scaled per functional test)
- False Positive Rate Difference (FPRD) for fairness
- Mean and standard deviation over seeds

**Calculation**: Unseen dataset tests: use each dataset's standard metric (sentiment analysis: Accuracy; NLI: Macro F1). Contrast set tests: contrast consistency = percentage of instances for which both the original instance and all of its contrast instances are predicted correctly. Functional tests: failure rate = percentage of instances predicted incorrectly; normalized failure rate = min-max scaling per functional test, aggregate = mean normalized failure rate across functional tests. Statistical significance: unpaired Welch's t-test between each ER model and No-ER baseline (alternative hypothesis: ER model mean > No-ER mean), p < 0.05.

**Interpretation**: Higher Accuracy and Macro F1 indicate better task performance on unseen datasets. Higher contrast consistency is better. Lower failure rate / lower normalized failure rate indicates better performance on functional tests. Significance is assessed via Welch's t-test (p < 0.05). In this work, ER is interpreted as having little impact on in-distribution (ID) performance but can yield large OOD performance gains under certain design choices.

**Baseline Results**: No-ER baseline results are reported in the paper's tables. Examples from Table 1 (No-ER): SST (seen Acc) = 94.22 (±0.77), Amazon (unseen Acc) = 90.72 (±1.36), Yelp = 92.07 (±2.66), Movies = 89.83 (±6.79); e-SNLI (seen F1) = 76.18 (±1.28), MNLI (unseen F1) = 46.15 (±4.38). The paper compares these No-ER baselines to multiple ER variants across tables.

**Validation**: Hyperparameters tuned on development sets (seen dataset dev). Report mean over three random seeds and standard deviation. Early stopping based on total development set loss (task loss + ER loss) with patience of 10 epochs. Use unpaired Welch's t-test (p < 0.05) to measure statistical significance of ER improvements over No-ER.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Explainability
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Governance**: Lack of testing diversity, Incomplete usage definition

**Demographic Analysis**: Evaluates group fairness in hate speech detection via False Positive Rate Difference (FPRD) across group identifiers in lexicons (measures model bias against group identifiers).

**Potential Harm**: ['Bias against protected or identified groups in hate speech detection (measured as increased false positives for group identifiers)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
