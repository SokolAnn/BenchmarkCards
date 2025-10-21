# Moral Foundations Reddit Corpus (MFRC)

## 📊 Benchmark Details

**Name**: Moral Foundations Reddit Corpus (MFRC)

**Overview**: A collection of 16,123 English Reddit comments curated from 12 distinct subreddits, hand-annotated by at least three trained annotators for 8 categories of moral sentiment (Care, Proportionality, Equality, Purity, Authority, Loyalty, Thin Morality, Implicit/Explicit Morality) based on the updated Moral Foundations Theory framework. The paper also provides baseline moral-sentiment classification results using several NLP methods and cross-corpus comparison with the Moral Foundations Twitter Corpus (MFTC).

**Data Type**: text (Reddit comments)

**Domains**:
- Natural Language Processing
- Social Sciences

**Languages**:
- English

**Similar Benchmarks**:
- Moral Foundations Twitter Corpus (MFTC)

**Resources**:
- [Resource](https://huggingface.co/datasets/USC-MOLA-Lab/MFRC)
- [Resource](https://arxiv.org/abs/2208.05545)
- [Resource](https://huggingface.co/docs/datasets/index)
- [Resource](https://prodi.gy/notator)

## 🎯 Purpose and Intended Users

**Goal**: Provide a curated, hand-annotated Reddit corpus of moral sentiment (16,123 comments) and baseline classification results to facilitate research into moral rhetoric, moral-sentiment classification, annotator response patterns and bias, and cross-domain transfer between social media platforms.

**Target Audience**:
- Natural Language Processing researchers
- Social Sciences researchers
- Machine Learning researchers
- Model developers

**Tasks**:
- Text Classification
- Multi-label Classification
- Sentiment Analysis
- Moral Sentiment Detection

**Limitations**: The compiled dataset contains biases and is not representative of diverse moral concerns present in world populations. Potential biases include: biases specific to English-speaking countries and the English language, biases inherent to Reddit.com and its user base, biases in the researchers’ criteria for corpus curation as well as the underlying Moral Foundations Theory, bias in the assessment of moral labels, and the fact that annotators were all undergraduate research assistants at a private academic institute.

## 💾 Data

**Source**: 16,123 Reddit comments curated from 12 subreddits organized into three buckets (US politics, French politics, Everyday moral life). Subreddits sampled include: r/politics, r/conservative, r/antiwork, r/nostalgia, r/AmItheAsshole, r/confession, r/relationshipadvice, r/europe, r/worldnews, r/neoliberal, r/geopolitics, r/Conservative (French politics).

**Size**: 16,123 comments

**Format**: HuggingFace dataset

**Annotation**: Hand-annotated by at least three trained annotators (selected top five annotators performed most annotations). Each post labeled for 8 categories of moral sentiment (Care, Equality, Proportionality, Loyalty, Authority, Purity, Thin Morality, Implicit/Explicit Morality). Annotators reported confidence (Very Confident, Somewhat Confident, Not Confident). Annotations were performed on Prodigy. Majority-vote labels (>=50% agreement) used for reported frequencies.

## 🔬 Methodology

**Methods**:
- Distributed Dictionary Representations with SVM (DDR-SVM)
- BERT fine-tuning (single-label)
- Multi-label BERT fine-tuning
- Cross-corpus classification / knowledge transfer (between MFRC and MFTC)
- Stratified 10-fold cross-validation with 10% of training data used for validation

**Metrics**:
- F1 Score
- Precision
- Recall
- Fleiss's kappa
- Prevalence- and bias-adjusted Fleiss's kappa (PABAK)

**Calculation**: F1, precision, and recall are calculated across stratified 10-fold cross-validation. For multi-label BERT the union of moral labels was used for stratification and F1 macro was used for model selection; for single-label classification binary F1 was used for model selection. A weighted loss was used where a sample's weight for a label is proportional to the inverse of the label frequency.

**Interpretation**: BERT models outperform DDR-SVM models in terms of F1 and Precision; DDR-SVM models achieve higher Recall in most categories. Multi-label BERT achieved lower performance than single-label BERT. Cross-corpus experiments show some transferability between MFTC and MFRC; in general models trained and tested on MFTC had better performance in the reported comparisons.

**Baseline Results**: Baseline aggregate results (Table 10): DDR-SVM (All) Moral Sentiment F1 = 0.61 (Precision = 0.53, Recall = 0.71); BERT single-label (All) F1 = 0.76 (Precision = 0.72, Recall = 0.81); Multi-label BERT (All) F1 = 0.73 (Precision = 0.74, Recall = 0.73). Detailed per-foundation results are provided in Tables 3-9 of the paper.

**Validation**: Stratified 10-fold cross-validation; 10% of training data used for validation and hyperparameter/model selection; inter-annotator agreement assessed using Fleiss's kappa and PABAK. Cross-corpus validation performed by training on one corpus and testing on the other, with downsampling of MFTC to match MFRC label counts for fair comparison.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Annotator demographic and psychological metadata were collected (gender, sexual orientation, age, household income, first language, political ideology on a liberal-conservative scale, religious affiliation, Moral Foundation Questionnaire-2). Basic analyses show annotators’ political ideology and morality skew liberal while family income skews wealthier than the average American.

**Potential Harm**: The paper notes that dataset biases (e.g., platform-specific, English-language, annotator composition, theoretical framing) likely influenced annotations and the performance of machine learning models trained on the corpus.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotator identities are kept anonymous while demographic and psychological measures are provided.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
