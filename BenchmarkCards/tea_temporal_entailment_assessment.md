# TEA (Temporal Entailment Assessment)

## 📊 Benchmark Details

**Name**: TEA (Temporal Entailment Assessment)

**Overview**: We propose a novel entailment dataset that requires models to correctly determine the internal and external temporal structure of predications when performing natural language inference.

**Data Type**: text (sentence pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SNLI
- MNLI
- DNC
- TimeBank
- VerbOcean
- WordNet

**Resources**:
- [GitHub Repository](https://github.com/tttthomasssss/iwcs2019)

## 🎯 Purpose and Intended Users

**Goal**: Provide a novel entailment dataset (TEA) that casts the problem of determining when a consequent state is licensed by an event as a natural language inference task, focused on temporally and aspectually modified predications.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Natural Language Inference
- Entailment Detection
- Binary Classification

**Limitations**: TEA focuses on perfect and progressive aspect only and does not cover other aspect types such as Aktionsart. TEA was annotated by two annotators (the first and second authors) with an initial disagreement rate of just under 20%; the authors identify a possible annotation artefact due to sequential (non-random) annotation which they attempted to mitigate. The dataset intentionally uses short sentences and does not include temporal adverbials (authors note adding adverbials as future work).

## 💾 Data

**Source**: Candidate verb pairs were sampled from the before-after category of VerbOcean, the WordNet verb entailment graph, the entailment datasets of Weisman et al. (2012) and Vulić et al. (2017), and the relation inference dataset of Levy and Dagan (2016). Candidate pairs were manually filtered to retain only pairs with a temporal relation; nouns were chosen as arguments to form full sentences.

**Size**: 11,138 sentence pairs (class distribution: 22% entailment, 78% non-entailment)

**Format**: N/A

**Annotation**: Manually annotated by two annotators (the first and second authors). Entailment interpreted as common-sense inference. Initial annotation disagreement was just under 20%; disagreements were resolved case-by-case through discussion and chosen strongest readings. The dataset was not crowdsourced.

## 🔬 Methodology

**Methods**:
- Diagnostic classification (auxiliary-verb agreement) using logistic regression with stratified J-K-fold cross-validation
- Translation operation evaluation (averaged vector offset and feedforward neural network projection)
- Embedding similarity evaluation using cosine similarity and average precision (area under precision-recall curve)
- Binary classification evaluation for pre-trained biLSTMs (softmax prediction scores)
- Cross-validation (10-fold for translation neural network experiments; stratified J-K-fold for agreement task)
- Automated metrics (precision/recall curves, MRR, accuracy, macro-averaged F1)

**Metrics**:
- Average Precision (Area under Precision-Recall curve)
- Accuracy
- Macro-averaged F1 Score
- Mean Reciprocal Rank (MRR)
- Precision
- Recall
- Cosine Similarity

**Calculation**: Average Precision: precision and recall measured over varying thresholds and reported as average precision (area under the precision-recall curve). MRR: averaged over 10 randomly sampled seed sets (for averaged offset) and 10 cross-validation folds (for neural network). Auxiliary-verb agreement: averaged accuracy using stratified J-K-fold cross-validation with a scikit-learn logistic regression classifier. BiLSTM classification: accuracy and macro-averaged F1 from softmax prediction scores.

**Interpretation**: Higher average precision indicates better entailment detection ability; MRR indicates success in generating correct inﬂected verb forms. Authors interpret that embedding models and pre-trained biLSTMs fail to outperform a majority-class / tense-pair baseline on TEA, attributing this to models' reliance on distributional/contextual similarity which yields many false positives and prevents reliable inference governed by tense and aspect.

**Baseline Results**: TEA results (reported): Avg. Precision -- word2vec: 0.31, APT: 0.28, fastText: 0.30, ELMo: 0.21, BERT: 0.27. biLSTM-DNC: Avg. Precision 0.22; Accuracy 0.58; F1-Score 0.49. biLSTM-SNLI: Avg. Precision 0.21; Accuracy 0.51; F1-Score 0.47. Majority class baseline Avg. Precision 0.22; Majority class / tense pair baseline Avg. Precision 0.35. (Auxiliary-verb agreement results: averaged accuracies reported in Table 2; translation operation evaluated with MRR as shown in figures.)

**Validation**: Annotation validation: dataset annotated by two annotators with disagreements (~20%) resolved through discussion; authors report resolving all initial disagreements and assert annotations are robust. Experimental validation: cross-validation used (10-fold and stratified J-K-fold) for respective experiments; pre-trained biLSTMs achieved 83% and 88% accuracy on SNLI and DNC development sets respectively prior to evaluation on TEA.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
