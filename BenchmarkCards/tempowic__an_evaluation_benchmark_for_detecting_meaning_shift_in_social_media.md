# TempoWiC: An Evaluation Benchmark for Detecting Meaning Shift in Social Media

## 📊 Benchmark Details

**Name**: TempoWiC: An Evaluation Benchmark for Detecting Meaning Shift in Social Media

**Overview**: To bridge this gap, we present TempoWiC, a new benchmark especially aimed at accelerating research in social media-based meaning shift.

**Data Type**: tweet pairs (text)

**Domains**:
- Natural Language Processing
- Social Media

**Languages**:
- English

**Similar Benchmarks**:
- SuperGLUE Word-in-Context (WiC)
- XL-WiC
- Am2ico
- MCL-WiC
- WiC-TSV

**Resources**:
- [GitHub Repository](https://github.com/cardiffnlp/TempoWiC)
- [Resource](https://arxiv.org/abs/2209.07216v2)

## 🎯 Purpose and Intended Users

**Goal**: A new benchmark especially aimed at accelerating research in social media-based meaning shift.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers

**Tasks**:
- Word-in-Context Classification
- Meaning Shift Detection
- Binary Classification

**Limitations**: This work only covers English.

## 💾 Data

**Source**: Corpus of 100M tweets collected from the Twitter API for the period between the start of 2019 and September of 2021; initial candidate words drawn from WordNet (82K lemmas); trending words selected via monthly frequency counts and trending scores following Chen et al. (2021).

**Size**: 3,297 instances (train: 1,428 instances; validation: 396 instances; test: 1,473 instances)

**Format**: N/A

**Annotation**: Two-stage annotation: Stage 1 breadth annotation (10 instances for 210 words) to select words; Stage 2 depth annotation with 100 instances per selected word, each instance annotated by three annotators; final label by majority vote. Annotators: four recruited via institution recruitment office, native or near-native English speakers, paid. Words with Krippendorff's alpha below 0.1 were removed.

## 🔬 Methodology

**Methods**:
- Fine-tuning pretrained language models on tweet pairs
- Contextual embedding similarity (cosine similarity of target word embeddings)
- Logistic regression on cosine similarity
- MLP classifiers on concatenated embeddings

**Metrics**:
- Macro-F1
- Accuracy

**Calculation**: Results are reported according to the standard Macro-F1 metric for multi-class classification problems. Accuracy is also reported for completeness.

**Interpretation**: Macro-F1 provides a more accurate representation of performance on this unbalanced dataset; no explicit numeric thresholds for good vs. poor performance are provided.

**Baseline Results**: Main test results (Table 3): Fine-tuning - RoBERTa-base: Accuracy 66.89%, Macro-F1 58.26%; RoBERTa-large: Accuracy 66.49%, Macro-F1 59.10%; TimeLMs-2019-90M: Accuracy 66.46%, Macro-F1 57.70%; TimeLMs-2021-124M: Accuracy 65.04%, Macro-F1 54.75%; BERTweet-large: Accuracy 67.93%, Macro-F1 60.62%. Similarity - RoBERTa-large: Accuracy 72.98%, Macro-F1 67.09%; TimeLMs-2019-90M: Accuracy 74.07%, Macro-F1 70.33% (best reported); TimeLMs-2021-124M: Accuracy 71.01%, Macro-F1 63.51%. Naive baselines: Random Accuracy 50.00%, Macro-F1 50.00%; All True Accuracy 36.59%, Macro-F1 26.79%; All False Accuracy 63.41%, Macro-F1 38.80%.

**Validation**: Dataset split with held-out validation set (396 instances). Fine-tuning results are averages of 3 runs. MLP hyper-parameters tuned via grid search on the validation set. Inter-annotator agreement reported: Fleiss' Kappa 0.446, Krippendorff's alpha 0.439, maximum pairwise Krippendorff's alpha 0.627.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
