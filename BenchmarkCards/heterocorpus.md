# HeteroCorpus

## 📊 Benchmark Details

**Name**: HeteroCorpus

**Overview**: A corpus created specifically for studying heteronormative language in English, consisting of 7,265 manually annotated tweets.

**Data Type**: Tweets

**Domains**:
- Natural Language Processing
- Gender Studies

**Languages**:
- English

**Similar Benchmarks**:
- Gender bias text corpora
- Sexism detection datasets

**Resources**:
- [GitHub Repository](https://github.com/juanmvsa/HeteroCorpus)

## 🎯 Purpose and Intended Users

**Goal**: To identify and mitigate heteronormative language in NLP systems.

**Target Audience**:
- Research community
- NLP practitioners
- Gender studies researchers

**Tasks**:
- Heteronormative language detection
- Gender bias analysis
- NLP system evaluation

**Limitations**: N/A

**Out of Scope Uses**:
- Hate speech detection

## 💾 Data

**Source**: Twitter

**Size**: 7,265 tweets

**Format**: Annotated textual data

**Annotation**: Manually annotated by six annotators

## 🔬 Methodology

**Methods**:
- SVM classification
- Logistic regression
- BERT-based models

**Metrics**:
- Accuracy
- F1-score

**Calculation**: Metrics calculated based on the classification performance of the models.

**Interpretation**: BERT models outperformed traditional classifiers indicating the complexity of identifying heteronormativity.

**Validation**: Cohen's Kappa and Fleiss' Kappa used to assess annotation reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias in language processing
- Misrepresentation of gender
- Harm to LGBTQIA+ communities

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential perpetuation of stereotypes and exclusion of non-binary identities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All tweets posted publicly with identifying characteristics removed.

**Data Licensing**: Dataset follows Twitter's privacy policy and is not fully released.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
