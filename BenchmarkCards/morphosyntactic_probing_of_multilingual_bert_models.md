# Morphosyntactic Probing of Multilingual BERT Models

## 📊 Benchmark Details

**Name**: Morphosyntactic Probing of Multilingual BERT Models

**Overview**: We introduce an extensive dataset for multilingual probing of morphological information in language models (247 tasks across 42 languages from 10 families), each consisting of a sentence with a target word and a morphological tag as the desired label, derived from the Universal Dependencies treebanks. We apply perturbation methods (masking, permutation) and Shapley values to locate where disambiguating information resides in the input.

**Data Type**: Sentences with a target word and morphological tag labels (morphosyntactic annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- Basque
- Belarusian
- Latvian
- Lithuanian
- Afrikaans
- Bulgarian
- Croatian
- Czech
- Polish
- Russian
- Serbian
- Slovak
- Slovenian
- Ukrainian
- Albanian
- Armenian
- Greek
- Irish
- Persian
- Arabic
- Hebrew
- Turkish
- Estonian
- Finnish
- Hungarian
- Catalan
- French
- Italian
- Latin
- Portuguese
- Romanian
- Spanish
- Hindi
- Urdu
- Dutch
- English
- German
- Icelandic
- Norwegian Bokmal
- Norwegian Nynorsk
- Swedish

**Similar Benchmarks**:
- Universal Dependencies (UD) Treebanks
- UniMorph
- LINSPECTOR
- SIGMORPHON shared tasks

**Resources**:
- [GitHub Repository](https://github.com/juditacs/morphology-probes)
- [Resource](https://arxiv.org/abs/2306.06205)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large multilingual morphosyntactic probing dataset (247 tasks across 42 languages) derived from Universal Dependencies and to analyze where morphological information for each task resides in context using perturbation methods and Shapley value attribution.

**Tasks**:
- Morphological tagging
- Morphological feature classification
- Probing / Diagnostic classification

**Limitations**: The dataset is dominated by Indo-European languages and has a modest number of non-European tasks; several languages (e.g., Chinese, Japanese, Vietnamese, Korean) were excluded due to lack of UD data or incompatible tagsets; tasks with very rare classes were discarded (classes with fewer than 200 occurrences).

## 💾 Data

**Source**: Universal Dependencies treebanks (UD 2.9), extended with Kote et al. (2019) Albanian treebank and a silver standard Hungarian dataset (Nemeskey 2020).

**Size**: 247 tasks across 42 languages; for each task: 2,000 training samples, 200 development samples, 200 test samples (per-task splits as described in paper).

**Format**: CoNLL-U (Universal Dependencies) gold tokenization; sampled into train/dev/test splits as described in the paper.

**Annotation**: Existing Universal Dependencies morphosyntactic tags (per-token UD annotations). No new manual annotation described; tasks sampled from UD annotations with downsampling/discarding to limit class imbalance.

## 🔬 Methodology

**Methods**:
- Automated metrics (accuracy)
- Probing with auxiliary classifiers (feature-based probes: linear and MLP probes)
- Perturbation experiments (masking target word, masking left/right context, masking both sides, permutation of word order)
- Shapley value analysis to assign contribution by relative position
- Baselines comparison (bidirectional character LSTM chLSTM, fastText, Stanza)

**Metrics**:
- Accuracy
- Effect (percentage change in accuracy due to perturbation)
- Statistical significance tests (paired t-test, binomial sign test) as reported

**Calculation**: Perturbation effect E(m; t; p) is defined as E(m;t;p) = 1 - Acc(m;t;p) / Acc(m;t), where Acc(m;t) is the unperturbed probing accuracy for model m on task t and Acc(m;t;p) is the accuracy under perturbation p. Shapley values are computed over 9 relative positions with v(S) = 100 * (Acc_S - Acc_all_masked) / (Acc_full - Acc_all_masked) as described in the paper.

**Interpretation**: Higher Accuracy indicates stronger recoverable morphological information in model representations. Effect quantifies how much accuracy is lost under input perturbations (larger effect = more information removed). Shapley values quantify contribution of target and contextual positions; authors interpret results to mean most information is in the target word and left (preceding) context generally contributes more than right context (example summary: XLM-RoBERTa context contribution left/right = ~27.0%/18.6%, target = ~54.4%).

**Baseline Results**: Average test accuracy across all 247 tasks: mBERT 90.4%, XLM-RoBERTa 91.8%, chLSTM (bidirectional char-LSTM) 85.0%, fastText 83.3%, Stanza 91.4% (Stanza excludes Albanian tasks).

**Validation**: Train/dev/test splits sampled from UD treebanks with no overlap of target words across splits; early stopping based on development loss and accuracy; results averaged over 10 runs with different random seeds (Shapley computations run once due to cost).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
