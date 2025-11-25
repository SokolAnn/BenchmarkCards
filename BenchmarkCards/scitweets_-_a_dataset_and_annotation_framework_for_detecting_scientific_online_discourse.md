# SciTweets - A Dataset and Annotation Framework for Detecting Scientific Online Discourse

## 📊 Benchmark Details

**Name**: SciTweets - A Dataset and Annotation Framework for Detecting Scientific Online Discourse

**Overview**: We propose SciTweets, a publicly available dataset and annotation framework for science discourse on Twitter, including (a) a hierarchical definition of science-relatedness, (b) an annotation framework and sampling strategy, (c) a ground truth dataset of 1,261 expert-annotated tweets, and (d) baseline classification models for detecting science-relatedness and specific forms of scientific knowledge.

**Data Type**: text (tweets)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Online Social Networks

**Languages**:
- English

**Similar Benchmarks**:
- CLIMATE-FEVER
- COVID-Fact
- FEVER
- SciClops
- Monant Medical Misinformation Dataset

**Resources**:
- [GitHub Repository](https://github.com/AI-4-Sci/SciTweets)
- [Resource](https://arxiv.org/abs/2206.07360v2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a hierarchical definition of science-relatedness, an annotation framework, and a high-quality expert-annotated dataset to enable development and evaluation of methods for analysing science-related online discourse.

**Target Audience**:
- Natural Language Processing researchers
- Information Retrieval researchers
- Communication studies researchers
- Computational social science researchers

**Tasks**:
- Text Classification
- Multi-label Classification
- Claim Detection
- Claim Verification
- Information Retrieval (claim retrieval)

**Limitations**: SciTweets is a comparably small corpus; precision is expected to be lower when classifiers are applied to a random sample of TweetsKB due to the higher ratio of false positives in larger random samples.

## 💾 Data

**Source**: Sampled from the TweetsKB full text archive (metadata of more than 2 billion English tweets created from archiving 10 billion raw tweets via the 1% Twitter API stream between February 2013 and December 2020).

**Size**: 1,261 tweets

**Format**: N/A

**Annotation**: Expert annotation by four annotators (two co-authors, one PhD student, one bachelor’s student). Labels include individual annotator labels and consolidated ground-truth labels. Inter-annotator agreement measured via Fleiss Kappa with average 0.63 (category scores 0.61, 0.63, 0.66).

## 🔬 Methodology

**Methods**:
- Expert human annotation
- Heuristic-based candidate sampling
- Weakly supervised classifier-based sampling
- Multi-label classification
- 10-fold cross validation

**Metrics**:
- Precision
- Recall
- F1 Score
- Precision@100
- Fleiss Kappa (inter-annotator agreement)

**Calculation**: Binary science-related prediction is obtained by mapping multi-label predictions to a binary decision: a tweet is science-related if at least one subcategory (1.1, 1.2, 1.3) is predicted. Precision@100 was computed by setting prediction thresholds so that the classifier makes 100 positive predictions per subcategory out of 100,000 tweets and measuring precision on those positives.

**Interpretation**: The classifier performs better on the binary science-related vs not task than on the finer-grained multi-label subcategory task. The authors report approx. 89% F1 (stated in contributions) for distinguishing science from non-science and approx. 78% F1 (macro average) for detecting subcategories; reported 10-fold cross validation results include binary F1 84.34 and per-subcategory F1s: 77.97 (1.1), 76.60 (1.2), 80.35 (1.3). Precision when selecting top 100 predictions per category on 100K tweets is reported as 85.00% (1.1), 74.00% (1.2), 86.00% (1.3). The paper notes that precision is expected to decrease when evaluated on random samples of TweetsKB.

**Baseline Results**: Reported (contributions): approx. 89% F1 for binary science-related detection and approx. 78% F1 (macro) for subcategory detection. 10-fold CV results (Table 3): binary - Precision 84.70, Recall 83.99, F1 84.34; multi-label - 1.1 F1 77.97, 1.2 F1 76.60, 1.3 F1 80.35. Precision@100 (Table 4): 1.1 85.00%, 1.2 74.00%, 1.3 86.00%.

**Validation**: Annotation quality validated via Fleiss Kappa computed across four annotators. Model validation performed using 10-fold cross validation on SciTweets (excluding high disagreement cases). Additional validation: set thresholds to obtain 100 positive predictions per subcategory on 100K tweets and manually annotated resulting 215 tweets from the second annotation stage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misinformation
- Bias

**Atlas Risks**:
- **Misuse**: Spreading disinformation
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Potential Harm**: ['Misinformation spread', 'Detrimental effects on public health and society']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY Creative Commons license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
