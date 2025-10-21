# Detection of Word Adversarial Examples in Text Classiﬁcation: Benchmark and Baseline via Robust Density Estimation

## 📊 Benchmark Details

**Name**: Detection of Word Adversarial Examples in Text Classiﬁcation: Benchmark and Baseline via Robust Density Estimation

**Overview**: To encourage further research in this domain, we release a benchmark for word-level adversarial example detection on four attack methods across four NLP models and four text classification datasets.

**Data Type**: text (sentence classification pairs: clean and adversarial examples)

**Domains**:
- Natural Language Processing

**Resources**:
- [GitHub Repository](https://github.com/anoymous92874838/text-adv-detection)
- [GitHub Repository](https://github.com/maximilianmozes/fgws)

## 🎯 Purpose and Intended Users

**Goal**: Release a benchmark dataset for word-level adversarial example detection on 4 attacks, 4 text classification datasets, and 4 models and provide a competitive baseline method (RDE) to encourage further research in this field.

**Tasks**:
- Adversarial Example Detection
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Adversarial examples generated from IMDB (Maas et al., 2011), AG-News (Zhang et al., 2015), SST-2 (Socher et al., 2013), and Yelp (Zhang et al., 2015) using attack methods Textfooler (TF), PWWS, BAE, and TF-adjusted via the TextAttack library.

**Size**: IMDB: 25,000 original test samples / 10,000 generated samples; AG-News: 7,600 original test samples / 7,600 generated samples; SST-2: 2,700 original test samples / 2,700 generated samples; Yelp: 38,000 original test samples / 5,000 generated samples.

**Format**: CSV

**Annotation**: Automatically generated adversarial examples using attack algorithms; labels inherited from original datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Feature-based density estimation (Robust Density Estimation, RDE) using kPCA and Minimum Covariance Determinant (MCD)
- Baseline comparison methods: FGWS (word-frequency based), Perplexity using GPT-2, MLE (feature Gaussian likelihood)

**Metrics**:
- True Positive Rate (TPR)
- F1 Score
- Area Under ROC Curve (AUC)
- False Positive Rate (FPR) (used as thresholding parameter)

**Calculation**: TPR is the fraction of true adversarial samples out of predicted adversarial samples. F1-score is the harmonic mean of precision and recall. AUC measures the area under the TPR vs FPR curve. For TPR and F1 reported in experiments, FPR is fixed at 0.1.

**Interpretation**: For all three metrics, higher denotes better performance. TPR and F1 depend on a chosen FPR; experiments fix FPR = 0.1 (10% false positive rate). AUC considers performance across FPR values.

**Baseline Results**: RDE achieves the best performance by AUC on 29 out of 30 dataset-attack-model combinations and best performance by TPR, F1, AUC on 25 out of 30 combinations, outperforming FGWS, Perplexity (GPT-2), and MLE in the reported experiments.

**Validation**: Validation procedures include subsampling and three repetitions of random seeds for test/validation split and subsampled samples. For IMDB and AG-News, 30% of the test set is held out as validation set in some experiments. Experiments are conducted under two scenarios (Scenario 1 and Scenario 2) for dataset configuration.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness

**Atlas Risks**:
- **Robustness**: Evasion attack

**Potential Harm**: The paper states: 'For such applications, attaining outputs of an adversarial input - whether correct or not - may turn out to be harmful to the system.'

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
