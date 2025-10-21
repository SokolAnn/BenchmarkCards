# SOLD (Sinhala Offensive Language Dataset)

## 📊 Benchmark Details

**Name**: SOLD (Sinhala Offensive Language Dataset)

**Overview**: SOLD is a manually annotated dataset for offensive language identification in Sinhala containing 10,000 tweets annotated at sentence-level (Offensive / Not Offensive) and token-level (rationales). The paper also introduces SemiSOLD, a semi-supervised dataset with more than 145,000 Sinhala tweets annotated using a semi-supervised (democratic co-learning) approach. The resources are released to enable research on offensive language detection, explainability, transfer learning and data augmentation in a low-resource language.

**Data Type**: text (Twitter posts / tweets)

**Domains**:
- Natural Language Processing

**Languages**:
- Sinhala

**Similar Benchmarks**:
- OffensEval
- TRAC
- HASOC
- HatEval
- AbuseEval
- OLID
- OGDT
- MOLD
- SOLID
- HateXplain
- TSD

**Resources**:
- [GitHub Repository](https://github.com/Sinhala-NLP/SOLD)
- [Resource](https://huggingface.co/datasets/sinhala-nlp/SOLD)
- [Resource](https://huggingface.co/datasets/sinhala-nlp/SemiSOLD)
- [Resource](https://huggingface.co/sinhala-nlp/)

## 🎯 Purpose and Intended Users

**Goal**: To provide the largest publicly available Sinhala offensive language dataset (SOLD) annotated at sentence-level and token-level to support offensive language identification and explainability in a low-resource language, and to release SemiSOLD (semi-supervised) to address data scarcity and enable transfer learning and data augmentation research.

**Target Audience**:
- Natural Language Processing researchers
- Machine Learning researchers
- Model developers
- Content Moderators

**Tasks**:
- Text Classification
- Token Classification
- Explainability (rationale extraction)

**Limitations**: Dataset is limited to Twitter data written in Sinhala script (the authors filtered out Roman and mixed-script tweets). Token-level inter-annotator agreement is lower than sentence-level (majority of token-level pairwise Kappa scores between 0.6-0.7). SemiSOLD contains noisy labels (semi-supervised) and the authors report that filtering by model uncertainty is necessary; overly permissive thresholds can reduce model performance. The dataset covers only tweets collected via keyword filtering and a Twitter language filter.

## 💾 Data

**Source**: SOLD: 10,000 tweets collected from Twitter using the Twitter API and keyword-based collection; SemiSOLD: more than 145,000 Sinhala tweets collected from Twitter for semi-supervised annotation.

**Size**: 10,000 tweets (SOLD); more than 145,000 tweets (SemiSOLD)

**Format**: N/A

**Annotation**: SOLD: Manual annotation via LightTag by ten native Sinhala annotators; each tweet annotated by three annotators; sentence-level labels (OFF/NOT) and token-level rationales (tokens contributing to offensiveness) collected; majority voting used to decide gold labels. Inter-annotator agreement measured with pairwise Fleiss' Kappa (sentence-level majority 0.7-0.8; token-level majority 0.6-0.7). SemiSOLD: annotated using a semi-supervised (democratic co-learning) approach where multiple ML models predict confidences and aggregated labels are assigned with uncertainty-based filtering.

## 🔬 Methodology

**Methods**:
- Human annotation (crowdsourcing via LightTag) for gold labels
- Automated metrics (model evaluation)
- Cross-lingual transfer learning
- Semi-supervised data augmentation (democratic co-learning)
- Weakly-supervised token extraction using LIME

**Metrics**:
- Macro-averaged F1 Score
- Precision
- Recall
- Weighted F1 Score

**Calculation**: Macro-averaged F1 computed across the OFF and NOT classes. Per-class Precision, Recall and F1 reported. Experiments run with five random seeds and mean values reported. For token-level evaluation, Precision, Recall and Macro F1 of offensive tokens were used. SemiSOLD labeling used model confidence averages and uncertainty thresholds (examples filtered by standard deviation thresholds 0.05, 0.1, 0.15).

**Interpretation**: Macro-averaged F1 is used to account for class imbalance; higher Macro-F1 indicates better balanced performance across offensive and not-offensive classes. Models are compared against majority/minority baselines and improvements are reported as absolute scores and percentage differences versus non-transfer / non-augmented baselines.

**Baseline Results**: Best reported sentence-level result: XLM-R achieved Macro F1 = 0.83. Best reported token-level result: XLM-R achieved F1 = 0.72. Majority-class baselines reported in paper for comparison.

**Validation**: Dataset split randomly into 75% training and 25% testing. During model training an evaluation set consisting of one-fifth of the training data was used for early stopping. Experiments repeated with five random seeds; mean reported. Inter-annotator agreement computed (Fleiss' Kappa for sentence-level; character-offset pairwise Kappa for token-level). SemiSOLD filtered by model uncertainty thresholds and validated by improvements in downstream evaluation on the SOLD test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities, Impact on human agency

**Demographic Analysis**: N/A

**Potential Harm**: ['Offensive content', 'Hate speech', 'Cyber-bullying', 'Toxicity']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors do not collect Twitter user IDs and replace username mentions with @USER tokens and URLs with <URL> tokens to conceal personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
