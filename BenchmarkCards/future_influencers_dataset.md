# Future Influencers Dataset

## 📊 Benchmark Details

**Name**: Future Influencers Dataset

**Overview**: This research presents a compiled dataset of over 1 million publicly shared tweets by future influencers and develops a scalable NLP pipeline using SOTA models to investigate the futures projected by futurists on Twitter.

**Data Type**: text (tweets)

**Domains**:
- Natural Language Processing
- Social Media Networks

**Resources**:
- [Resource](https://osf.io/z925y/)
- [GitHub Repository](https://github.com/JustAnotherArchivist/snscrape.git)
- [Resource](https://doi.org/10.1145/3582515.3609573)
- [Resource](https://arxiv.org/abs/2308.02035)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the futures projected by futurists on Twitter and explore the impact of language cues on anticipatory thinking among social media users, and to model anticipated futures from social data.

**Tasks**:
- Topic Modeling
- Text Clustering
- Exploratory Data Analysis

**Limitations**: Analysis confined to a specific subset of Twitter users (influencers), which may restrict generalizability; not all tweets attributed to future influencers necessarily reflect their own future anticipations (some may be retweets or quotations); study limited to tweets published by future influencers and did not include user comments or associated sentiment analysis.

## 💾 Data

**Source**: Tweets were obtained using the scraping library snsscrape; Tweets were gathered between 1 January 2021 and 31 March 2023; the dataset comprises tweets posted by 'future influencers' selected by human experts (final list included about 250 futurists).

**Size**: 1.2 million tweets

**Format**: N/A

**Annotation**: Accounts/tweets were carefully selected by human experts (final list ~250 futurists).

## 🔬 Methodology

**Methods**:
- Latent Dirichlet Allocation (LDA) using Gensim (multi-core implementation)
- BERTopic (sentence embeddings + PCA dimensionality reduction + KMeans clustering + c-TF-IDF)
- Coherence evaluation using the C_V measure (Röder et al.)
- Expert judgment for validation and hyperparameter selection
- Online/batch training for scalability (LDA on multiple CPU cores; precomputed sentence transformers on GPU for BERTopic)

**Metrics**:
- Coherence (C_V)
- Number of topics (topic count)

**Calculation**: Coherence calculated using the C_V measure developed by Röder et al.; hyperparameters optimized by maximizing coherence and using expert judgment; LDA and BERTopic trained in batches for scalability.

**Interpretation**: Higher C_V coherence indicates better topic coherence; LDA achieved a coherence score reported as "more than 50%" (described as decent for its class); BERTopic achieved coherence of 65% (described as good); consistent topic contributions over time suggest themes remain relevant.

**Baseline Results**: LDA: identified 15 topics with a coherence score of more than 50%. BERTopic: produced ~100 hierarchically organized clusters (coherence ~65%), which can be merged to ~20 well-separated topics (with a loss in coherence).

**Validation**: Validation performed via the C_V coherence score (Röder et al.) and expert judgment; n=15 chosen as optimal for LDA based on C_V; BERTopic topics evaluated for coherence and optionally merged (trade-off between number of topics and coherence).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment
- **Data Laws**: Data acquisition restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
