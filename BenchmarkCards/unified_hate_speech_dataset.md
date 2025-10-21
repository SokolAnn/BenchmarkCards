# Unified hate speech dataset

## 📊 Benchmark Details

**Name**: Unified hate speech dataset

**Overview**: A large-scale cross-dataset comparison for hate speech detection where the authors collect and unify 13 existing social media hate speech datasets (primarily Twitter), create unified binary and multiclass settings, and evaluate language models to study generalisation and robustness. The paper shows that combining datasets leads to more generalisable hate speech detection models.

**Data Type**: tweets (text) with binary and multiclass classification labels

**Domains**:
- Natural Language Processing
- Social Media

**Languages**:
- English

**Similar Benchmarks**:
- Measuring hate speech (MHS)
- Call me sexist, but (CMS)
- Hate Towards the Political Opponent (HTPO)
- HateX
- Offense
- Automated Hate Speech Detection (AHSD)
- Hateful Symbols or Hateful People? (HSHP)
- Are You a Racist or Am I Seeing Things? (AYR)
- Multilingual and Multi-Aspect Hate Speech Analysis (MMHS)
- HatE
- HASOC
- Detecting East Asian Prejudice on Social Media (DEAP)
- Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior (LSC)

**Resources**:
- [Resource](https://huggingface.co/cardiffnlp/twitter-roberta-base-hate-latest)
- [Resource](https://huggingface.co/cardiffnlp/twitter-roberta-base-hate-multiclass-latest)
- [Resource](https://arxiv.org/abs/2307.01680)

## 🎯 Purpose and Intended Users

**Goal**: To analyse cross-dataset generalisation of hate speech detection models and to create a unified training resource (combining 13 datasets) to develop more robust hate speech detection models.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Binary Hate Speech Classification
- Multiclass Hate Speech Classification (target group identification)

**Limitations**: Focus on Twitter and the English language; decisions in dataset selection and target-group mapping may influence results; experiments use base-sized language models due to computational limitations.

## 💾 Data

**Source**: Collection and unification of 13 existing hate speech datasets from social media (primarily Twitter): MHS, CMS, HTPO, HateX, Offense, AHSD, HSHP, AYR, MMHS, HatE, HASOC, DEAP, LSC. Non-Twitter content and non-English subsets were removed; near-duplicate tweets were removed; three datasets were dehydrated and tweet IDs were rehydrated via the Twitter API. An independent test set (Indep) was constructed by extracting tweets around International Women's Day and International Day Against Homophobia, Transphobia and Biphobia 2022 and manually annotated by an expert.

**Size**: 83,230 tweets (unified dataset); Indep test set: 171 tweets (151 non-hate, 20 hate)

**Format**: N/A

**Annotation**: Original datasets were manually annotated (varying annotator counts per dataset). For the unified labels, the authors map original annotations and assign a label when at least two annotators agree. The independent test set was manually annotated by one expert following provided annotation guidelines.

## 🔬 Methodology

**Methods**:
- Fine-tuning pre-trained language models
- Model-based evaluation
- Automated metrics (macro-averaged F1)
- Hyperparameter optimization using Ray Tune, HyperOpt and Adaptive Successive Halving

**Metrics**:
- Macro-averaged F1 score

**Calculation**: Macro-F1 is computed as the macro-averaged F1 score across classes and reported as the primary evaluation metric.

**Interpretation**: Higher Macro-F1 indicates better overall performance across classes. The authors interpret improved Macro-F1 when training on the combined/unified dataset (versus single datasets) as evidence of better generalisation and robustness.

**Validation**: Data splits use stratified 70% train / 10% validation / 20% test per dataset (using preexisting splits when provided). Results on the combined training set are averaged across each dataset-specific test set (AVG). An independent manually annotated test set (Indep) is used for targeted evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions
- **Accuracy**: Unrepresentative data

**Potential Harm**: ['Detection of hate speech towards protected groups (e.g., racism, sexism, religion, sexual orientation, disability)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User mentions in tweets are replaced with a placeholder to respect user privacy; authors state they use publicly available tweets and take measures to respect privacy.

**Data Licensing**: Datasets used are described as publicly available under open licence where applicable (specific licenses not detailed).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Authors state the work uses publicly available tweets under open licence and 'does not infringe any of the rules of Twitter’s API'; they also reference adherence to the ACM Code of Ethics.
