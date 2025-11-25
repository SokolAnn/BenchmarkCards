# ArCOV-19: The First Arabic COVID-19 Twitter Dataset with Propagation Networks

## 📊 Benchmark Details

**Name**: ArCOV-19: The First Arabic COVID-19 Twitter Dataset with Propagation Networks

**Overview**: ArCOV-19 is an Arabic COVID-19 Twitter dataset that spans one year (27th January 2020 to 31st January 2021) and includes about 2.7M tweets alongside the propagation networks of the most-popular subset (most-retweeted and most-liked). The propagation networks include both retweets and conversational threads. The release also includes the search queries and a language-independent crawler to encourage curation of similar datasets. The dataset is designed to enable research in Natural Language Processing, Information Retrieval, and Social Computing.

**Data Type**: text (tweets; propagation networks including retweets and conversational threads)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Social Computing

**Languages**:
- Arabic

**Similar Benchmarks**:
- Large Arabic Twitter Dataset on COVID-19 (Alqurashi et al., 2020)
- A large-scale covid-19 twitter chatter dataset for open scientific research (Banda et al., 2020)
- Covid-19: The first public coronavirus twitter dataset (Chen et al., 2020)
- Geocov19 (Qazi et al., 2020)
- Multilingual COVID-19 Twitter datasets referenced (Lopez et al., 2020; Dashtian and Murthy, 2021)

**Resources**:
- [Resource](https://gitlab.com/bigirqu/ArCOV-19/)
- [Resource](https://gitlab.com/bigirqu/ArCOV-19/-/tree/master/code/crawler)
- [Resource](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets)
- [GitHub Repository](https://github.com/Mottl/GetOldTweets3)
- [Resource](https://pickaw.com/en/)
- [GitHub Repository](https://github.com/azubiaga/pheme-twitter-conversation-collection)
- [Resource](https://developer.twitter.com/en/developer-terms/agreement-and-policy)

## 🎯 Purpose and Intended Users

**Goal**: To provide the first publicly-available Arabic Twitter dataset focused on COVID-19 (covering 27th January 2020 to 31st January 2021) including propagation networks for a most-popular subset, to support research in multiple areas such as Natural Language Processing, Information Retrieval, and Social Computing.

**Target Audience**:
- Natural Language Processing researchers
- Information Retrieval researchers
- Social Computing researchers
- Domain experts in Emergency Management
- Researchers working on Misinformation Detection

**Tasks**:
- Event Detection
- Summarization
- Geolocation
- Sentiment Analysis
- Stance Detection
- Hate Speech Detection
- Misinformation Detection
- Claim Verification
- Information Propagation Analysis
- User Influence Analysis

**Limitations**: Collection missed some days due to Twitter Search API limitations (search API limits to past 7 days); used GetOldTweets3 to recover some missed days. Replies were fully collected only until end of April 2020 at time of writing and collection of the rest was ongoing. Some retweets/replies could not be collected because tweets/accounts were deleted or private. Dataset excludes retweets from source tweets to avoid duplicates. Dataset limited to Arabic tweets only.

## 💾 Data

**Source**: Collected via Twitter Search API using manually-crafted daily queries (configured to return Arabic tweets and to exclude retweets). Source tweets collected from 27th January 2020 to 31st January 2021. Propagation networks (retweets and conversational threads) were collected for the top 1,000 most-popular tweets per day using Pickaw (retweets) and the PHEME Twitter conversation collection script (replies). Full list of search queries and the crawler implementation are released.

**Size**: 2,675,049 source tweets (about 2.7M); Top Subset: 370,132 tweet IDs; Retweets of Top Subset: 7,925,821 retweet IDs; Replies of Top Subset: 1,476,950 reply IDs; Unique users: 690,339 users.

**Format**: Released as tweet ID lists for source tweets and top subset; propagation networks released as lists of tweet IDs for retweets and conversational threads; search queries as text lists; crawler code in a public repository.

**Annotation**: No manual annotation for the main ArCOV-19 release. The top subset was filtered using an automatic qualification pipeline (inappropriate-words filter, heuristics for spam such as more than two URLs or four hashtags or fewer than four tokens, duplicate removal). (A separate annotated dataset ArCOV19-Rumors is mentioned as constructed on top of ArCOV-19.)

## 🔬 Methodology

**Methods**:
- Statistical analysis
- Temporal analysis (time series of keywords/hashtags/country mentions)
- Topical analysis (frequent words, hashtags, domains of shared URLs)
- Geographic analysis using Tweet place and coordinates attributes
- Propagation network collection and analysis (retweet and reply distributions)

**Metrics**:
- Counts (number of tweets, users, retweets, replies)
- Percentages (e.g., percentage geotagged, percentage including URLs)
- Popularity score (sum of retweet and favorite counts) used to rank tweets

**Calculation**: Popularity score is calculated as the sum of a tweet's retweet count and favorite (like) count. The top subset per day consists of the top 1,000 qualified tweets ranked by this score. Qualification filters exclude tweets containing inappropriate words, tweets with more than two URLs or four hashtags, tweets shorter than four tokens, and duplicate textual content (keeping the most popular duplicate). Counts and percentages are computed over the collected data as reported (e.g., geotagged 2,078 (0.08%), geolocated 60,873 (2.28%)).

**Interpretation**: Preliminary analyses interpret temporal spikes, topical distributions, and domain/linking patterns as representative of COVID-19 discussions in the Arabic Twitterverse during the covered period (e.g., spikes align with first reported cases in Arab countries; news domains dominate shared URLs). High retweet/reply counts are interpreted as evidence of highly propagated/popular content.

**Validation**: Data quality ensured by duplicate removal and a qualification pipeline to filter likely spam and low-quality tweets for the top subset. Representativeness validated by aligning temporal spikes of keywords/hashtags/country mentions with known dates of first reported COVID-19 cases in Arab countries and by analysis of domains and user statistics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misinformation

**Atlas Risks**:
- **Misuse**: Spreading disinformation
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Geographic analysis: 60,873 geolocated tweets (2.28% of total) and 2,078 geotagged tweets (0.08% of total). Geolocated tweets posted by users from 102 countries; 92.75% from the Arab world. Distribution of geolocated tweets: Saudi Arabia 41.7%, Kuwait 9.6%, UAE 6.8%, Oman 6.6%, Egypt 5.4%, Lebanon 5.3%, etc. User statistics: 690,339 unique users; 5,575 verified users (0.81%); 18.66% of tweets posted by verified users.

**Potential Harm**: ['Misinformation dissemination and propagation (supports detection/mitigation research)', 'Potential societal harms from misinformation such as panic, increased cases, or hoarding as described in the paper']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset released as tweet IDs and other ID lists in consideration of Twitter content redistribution policy. The paper notes that few users enable geotagging due to privacy and safety reasons.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
