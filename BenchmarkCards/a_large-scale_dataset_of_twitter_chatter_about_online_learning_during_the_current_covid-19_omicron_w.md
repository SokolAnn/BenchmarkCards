# A Large-Scale Dataset of Twitter Chatter about Online Learning during the Current COVID-19 Omicron Wave

## 📊 Benchmark Details

**Name**: A Large-Scale Dataset of Twitter Chatter about Online Learning during the Current COVID-19 Omicron Wave

**Overview**: This work presents a large-scale open-access Twitter dataset of conversations about online learning from different parts of the world since the first detected case of the COVID-19 Omicron variant in November 2021. The dataset is compliant with the privacy policy, developer agreement, and guidelines for content redistribution of Twitter, as well as with the FAIR (Findability, Accessibility, Interoperability, and Reusability) principles for scientific data management.

**Data Type**: text (Tweet IDs)

**Domains**:
- Big Data
- Data Mining
- Data Science
- Natural Language Processing
- Healthcare

**Languages**:
- English
- Indonesian
- Tagalog
- Estonian
- Spanish
- Hindi

**Similar Benchmarks**:
- CoAID
- COVID-19-FAKES
- ANTi-Vax
- CoVaxxy
- A COVID-19 Rumor Dataset

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.6837118)
- [GitHub Repository](https://github.com/DocNow/hydrator/releases)
- [GitHub Repository](https://github.com/DocNow/hydrator)
- [GitHub Repository](https://github.com/DocNow/twarc)
- [Resource](https://docs.rapidminer.com/latest/studio/operators/data_access/applications/twitter/search_twitter.html)
- [Resource](https://developer.twitter.com/en/developer-terms/agreement-and-policy)

## 🎯 Purpose and Intended Users

**Goal**: To provide an open-access, large-scale Twitter dataset of tweets about online learning posted between 9th November 2021 and 13th July 2022 to serve as a data resource for analysis of interest, views, opinions, perspectives, attitudes, and feedback towards online learning during the Omicron wave of COVID-19.

**Target Audience**:
- Researchers in Big Data
- Researchers in Data Mining
- Researchers in Data Science
- Researchers in Natural Language Processing
- Researchers in Healthcare

**Tasks**:
- Sentiment Analysis
- Aspect-based Sentiment Analysis
- Popularity Prediction (predicting popular tweets)
- Sarcasm Detection
- Topic Modeling
- Retweet Pattern Analysis
- Tweet Ranking
- Content Value Analysis
- Credibility Assessment
- Conspiracy Detection
- Emoji Prediction
- Relevance Ranking
- Satire Detection
- Deception Detection
- Topic Extraction
- User Characterization
- Demographic Inference

**Limitations**: The Twitter API search feature does not return an exhaustive list of tweets for a given date range, so multiple tweets posted in the date range may not have been returned and are thus not part of this dataset. Tweets deleted after collection will not be retrievable upon hydration. The released dataset contains only Tweet IDs (other tweet attributes were deleted to comply with Twitter policies).

## 💾 Data

**Source**: Twitter; Tweet IDs collected using the RapidMiner Search Twitter operator and the Twitter API Advanced Search between 9th November 2021 and 13th July 2022.

**Size**: 52,984 Tweet IDs

**Format**: Plain text .txt files (nine .txt files, each containing lists of Tweet IDs)

**Annotation**: No manual annotation; dataset contains only Tweet IDs (no labels or additional annotations).

## 🔬 Methodology

**Methods**:
- Automated data collection using RapidMiner Search Twitter operator (connecting to Twitter API)
- Keyword-based search (bag of synonyms/terms for COVID-19/Omicron and online learning) to fetch tweets containing at least one COVID-19 term and at least one online-learning term
- Data cleaning and deduplication using RapidMiner (duplicate tweets removed)
- Provision of hydration instructions (use of Hydrator, Twarc, or Social Media Mining Toolkit) to retrieve full tweet data from Tweet IDs

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: Duplicate tweets were removed after collection using RapidMiner. Compliance with Twitter privacy policy, developer agreement, and content redistribution guidelines was verified (only Tweet IDs distributed). Dataset adherence to FAIR principles (unique DOI, interoperable .txt files, re-usable via hydration) is documented.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Dataset contains tweets in 38 languages; English: 50,539 Tweets; Indonesian: 527 Tweets; Tagalog: 525 Tweets; Estonian: 364 Tweets; Spanish: 236 Tweets; Hindi: 179 Tweets. A total of 17,950 distinct Twitter users posted the tweets.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset contains only Tweet IDs to comply with Twitter's privacy policy, developer agreement, and content redistribution guidelines. The paper notes that tweets are public per Twitter policy and that deleted tweets will not be retrievable upon hydration.

**Data Licensing**: CC-BY 4.0

**Consent Procedures**: Not applicable

**Compliance With Regulations**: Dataset collection and sharing conducted in compliance with Twitter privacy policy, developer agreement, and content redistribution guidelines; dataset released via Zenodo with a DOI and documented to follow FAIR principles.
