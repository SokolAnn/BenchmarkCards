# POLUSA

## 📊 Benchmark Details

**Name**: POLUSA

**Overview**: POLUSA is a dataset that represents the online media landscape as perceived by an average US news consumer. The dataset contains 0.9M articles covering policy topics published between Jan. 2017 and Aug. 2019 by 18 news outlets representing the political spectrum. Each outlet is labeled by its political leaning, which the authors derive using a systematic aggregation of eight data sources. The news dataset is balanced with respect to publication date and outlet popularity.

**Data Type**: text (news articles with metadata such as author, publication date, URL, outlet name, and political leaning)

**Domains**:
- Social Sciences
- Natural Language Processing
- Political Science

**Languages**:
- English

**Similar Benchmarks**:
- The Media Frames Corpus
- NELA-GT-2018
- HuffPost
- BBC

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.3813663)
- [GitHub Repository](https://github.com/lukasgebhard/Political-News-Filter)
- [Resource](https://doi.org/10.1145/3383583.3398567)
- [Resource](https://commoncrawl.org/2016/10/news-dataset-available/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset of 0.9M online news articles covering policy topics (Jan. 2017 - Aug. 2019) balanced by time and outlet popularity to represent the online news landscape as perceived by an average US news consumer, enabling studies of media effects, political partisanship, and usage in data-intense deep-learning methods.

**Target Audience**:
- Social Scientists
- Computer Science Researchers
- Machine Learning Researchers
- Domain Experts studying media bias

**Tasks**:
- Text Classification
- Topic Classification
- Language Model Pretraining

**Limitations**: Dataset contains only English articles; temporal and popularity balancing choices trade off uniformity against the number of articles (more aggressive balancing would strongly reduce the number of articles); ten outlets with high temporal variation were dropped; outlets with low agreement among political-leaning measures (<0.75) are labeled as 'undefined'.

## 💾 Data

**Source**: Articles extracted from the Common Crawl News Archive (CCNA). Initial base selection contained articles from 30 news outlets (Jan. 2017 - Aug. 2019), reduced and processed to a final set of 18 outlets. Political-leaning labels for outlets derived by systematic aggregation of eight prior measures (self-declarations, content analyses, surveys and social network data). Additional resources used for classifier training: CCNA, HuffPost and BBC datasets.

**Size**: 0.9M articles (900,000 articles)

**Format**: N/A

**Annotation**: Political leanings assigned to outlets via systematic aggregation of eight prior measures; topic annotation (policy vs non-policy) produced by a convolutional neural network trained on 0.6M labeled articles (GloVe embeddings) and articles kept with p(a) >= 0.75. Near-duplicates removed using nearest-neighbor clustering of simhashes; non-English and non-article content removed via language filtering and URL heuristics.

## 🔬 Methodology

**Methods**:
- Near-duplicate removal via nearest-neighbor clustering of articles' simhashes
- Convolutional Neural Network classification (GloVe embeddings) to filter policy-topic articles
- Language filtering to keep only English articles
- URL heuristics (blacklists) to remove non-article and non-policy content
- Assignment of political leanings by systematic aggregation of eight prior measures
- Temporal and popularity-based balancing (popularity approximated by Alexa rank; subsampling to adjust outlet shares)

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: The policy-topic classifier was trained on 87.5% of a labeled set of 0.6M articles and evaluated on the remaining 12.5%, yielding F1 = 94.4, Precision = 95.6, Recall = 93.2. Articles with classifier probability p(a) >= 0.75 were kept as policy-topic articles.

**Interpretation**: Classifier performance (F1, Precision, Recall) indicates the authors consider the policy-topic filtering to be high quality; articles with p(a) >= 0.75 are interpreted as likely reporting on policy topics. Balancing by time and by modeled popularity (via Alexa rank) is used to align the dataset to the perceived real-world distribution of what an average US news consumer reads.

**Baseline Results**: Policy-topic classifier evaluation on 12.5% held-out data: F1 = 94.4, Precision = 95.6, Recall = 93.2.

**Validation**: Classifier validated on a 12.5% held-out portion of the 0.6M labeled dataset. Outlet political-leaning reliability ensured by aggregating eight measures and labeling outlets with agreement < 0.75 as 'undefined'. Temporal distortions mitigated by dropping ten outlets with high temporal variation and by subsampling outlets with overly many articles relative to Alexa-rank-based popularity model. Near-duplicate removal reduces duplicate-content noise.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Representativeness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Data contamination
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
