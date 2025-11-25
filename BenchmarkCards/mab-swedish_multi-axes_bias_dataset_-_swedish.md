# MAB-Swedish (Multi-axes Bias Dataset - Swedish)

## 📊 Benchmark Details

**Name**: MAB-Swedish (Multi-axes Bias Dataset - Swedish)

**Overview**: A newly created large Swedish bias-labeled dataset (MAB-Swedish) translated from the English MAB, and associated Swedish multi-axes lexica and model artifacts, used to estimate and explain social bias in benchmark NLP datasets using the bipol metric. The paper also evaluates bias in several English SuperGLUE datasets and two Swedish datasets.

**Data Type**: text (bias-labeled examples for binary bias classification: biased / unbiased)

**Domains**:
- Natural Language Processing

**Languages**:
- Swedish
- English

**Similar Benchmarks**:
- MAB (Multi-axes Bias Dataset)
- SuperGLUE
- WinoBias
- Winogender
- StereoSet
- HurtLex
- CrowS-Pairs

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To determine whether social bias exists in NLP benchmark datasets and estimate it along multiple axes using the bipol metric, and to create and release a large Swedish bias-labeled dataset (MAB-Swedish), lexica, and model artifacts to facilitate multilingual bias detection.

**Target Audience**:
- Researchers

**Tasks**:
- Bias Detection
- Text Classification

**Limitations**: MAB-Swedish may not contain examples that are specific to the Swedish culture since the original dataset is from English, with specific references to the USA and Canada. The bipol metric and models are limited in scope (covering a certain number of axes, 12), so a result of 0 does not necessarily indicate a bias-free dataset.

## 💾 Data

**Source**: Machine-translated from MAB (Alkhaled et al., 2023) using the Helsinki-NLP model; the English base was constructed from Jigsaw and the Social Bias Inference Corpus v2 (SBICv2).

**Size**: 1,946,975 examples

**Format**: N/A

**Annotation**: Labels derived from base datasets (biased / unbiased). Personal identifiable information (PII) were removed. Translation quality control involved back-translation of random samples using Google NMT and review by a Swedish speaker.

## 🔬 Methodology

**Methods**:
- Automated metric: bipol
- Model-based evaluation using classifiers (RoBERTa, Electra, DeBERTa)
- Training and evaluation of mT5 on MAB-Swedish

**Metrics**:
- Bipol score (range 0.0 to 1.0)
- Macro F1 Score
- Error rate

**Calculation**: Bipol is computed in two stages: (1) classification stage producing bc = (tp+fp)/(tp+fp+tn+fn) (with positive error rate fp/(fp+tp) reported); (2) lexica-based stage computing bs as averaged normalized difference in summed frequencies across axis term types. Final score b = bc * bs if bs > 0, else b = bc. (Equations provided in Section 3.1.)

**Interpretation**: Bipol score 0.0 indicates zero or undetected bias; 1.0 indicates extreme bias. Macro F1 and error rate are used to assess classifier performance (reported for MAB-Swedish and referenced English models).

**Baseline Results**: MAB-Swedish: average macro F1 on validation = 0.7623 (s.d. 0.0075), error rate = 0.2893. English reference error rates (from Alkhaled et al., 2023): RoBERTa 0.198, Electra 0.196, DeBERTa 0.2. Table 5 reports bipol scores per dataset and model (examples: CB bipol around 0.0679--0.076; Boolq bipol around 0.0053--0.0103; WSC/AXg/RTE values listed in paper).

**Validation**: Average results reported after running each experiment twice. Translation quality control via back-translation and Swedish speaker review. Evaluation performed across multiple pretrained models (RoBERTa, Electra, DeBERTa, mT5) and dataset splits (training/validation/test for MAB-Swedish).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark evaluation reports multi-axes analysis including gender and racial axes; lexica and bipol dictionaries of lists provide term frequency breakdowns and top-5 frequent terms per axis and dataset.

**Potential Harm**: ['Social harm due to bias in datasets', 'Exposure of offensive or stereotypical content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Personal identifiable information (PII) were removed from the MAB-Swedish dataset. The authors obscured offensive terms in presentation and performed translation verification (back-translation and human review).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
