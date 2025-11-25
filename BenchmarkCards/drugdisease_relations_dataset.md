# Drug–Disease Relations dataset

## 📊 Benchmark Details

**Name**: Drug–Disease Relations dataset

**Overview**: A labeled dataset for identifying treatment relations between drugs and diseases, constructed from FDA Drug Labels; contains a large crowdsourced training set and a smaller expert-annotated test set and is intended to support learning facts about drug–disease relationships that have medical significance.

**Data Type**: text (sentences from FDA Drug Labels with annotated drug–disease relation spans)

**Domains**:
- Healthcare

**Similar Benchmarks**:
- Chemical–Disease Relations (CDR)
- Penn Adverse Drug Reactions (ADR)

**Resources**:
- [GitHub Repository](https://github.com/roamanalytics/roamresearch/tree/master/Papers/Feature4Healthcarelexicons)
- [GitHub Repository](https://github.com/roamanalytics/roamresearch/tree/master/BlogPosts/Features_for_healthcareguide)
- [Resource](https://arxiv.org/abs/1811.00070v2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that can be used to learn facts about drug–disease relationships that have medical significance.

**Tasks**:
- Named Entity Recognition
- Relation Extraction

**Limitations**: We expect the crowdsourced labels to be used only for training; the authors use a smaller expert-annotated test set for evaluation.

## 💾 Data

**Source**: FDA Drug Labels corpus (official drug labels); annotations collected via crowdsourcing on the Figure Eight platform and expert annotation for the test set.

**Size**: 9,500 crowdsourced training examples and 500 expert-annotated test examples (initially launched as 10,000 sentences)

**Format**: N/A

**Annotation**: Crowdsourced via Figure Eight with labels inferred using Expectation Maximization (Dawid and Skene, 1979) for training data; expert annotation for the test set (500 examples).

## 🔬 Methodology

**Methods**:
- Automated metrics (per-token and chunk-level F1)
- 5-fold cross-validation for hyperparameter tuning
- Train/test evaluation on held-out test sets
- Repeated experiments (three runs) to report mean and standard deviation

**Metrics**:
- Macro-F1 (per-token)
- F1 Score (chunk-level, approximate matching for ADR)

**Calculation**: Per-token macro-F1 is computed for most datasets; for ADR chunk-level F1 is computed via approximate matching. Mean values and standard deviations are calculated over three runs of repeated experiments. Hyperparameters are tuned using 5-fold cross-validation on training data.

**Interpretation**: Higher F1 indicates better token/chunk labeling performance. The authors interpret superior macro-F1 and chunk-F1 scores as evidence that the combined ELMo-LSTM-CRF-HB model outperforms base models; no numeric thresholds for good vs. poor performance are provided.

**Baseline Results**: For Drug–Disease Relations (per-token macro-F1): rand-LSTM-CRF: 48.2 ± 1.12; HB-CRF: 42.3 ± 0.30; ELMo-LSTM-CRF: 50.6 ± 0.64; ELMo-LSTM-CRF-HB: 51.9 ± 0.52 (Table 2).

**Validation**: For datasets with predefined splits, hyperparameters were tuned with 5-fold cross-validation on the training set and evaluated on the test set. For datasets without predefined splits, the data were divided into five equal parts and evaluated with cross-validation; experiments were repeated three times to smooth random initialization variation. For the Drug–Disease Relations dataset, crowdsourced training labels were inferred via Expectation Maximization and evaluated against an expert-annotated test set (inter-annotator agreement between crowd-inferred labels and expert labels reported as 0.82).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Data Laws

**Atlas Risks**:
- **Privacy**: Reidentification
- **Accuracy**: Unrepresentative data
- **Data Laws**: Data usage restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper notes that clinical transcription data used in other experiments were de-identified and explicitly discusses that de-identification is hard or impossible for language data, raising privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
