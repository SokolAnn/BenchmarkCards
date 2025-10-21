# LSICC: A LARGE SCALE INFORMAL CHINESE CORPUS

## 📊 Benchmark Details

**Name**: LSICC: A LARGE SCALE INFORMAL CHINESE CORPUS

**Overview**: Introduce a large-scale corpus of informal Chinese. This corpus contains around 37 million book reviews and 50 thousand netizen’s comments to the news. We explore the informal words frequencies of the corpus and show the difference between our corpus and the existing ones. The corpus can be further used to train deep learning based natural language processing tasks such as Chinese word segmentation, sentiment analysis.

**Data Type**: text (book reviews and forum/discussion comments; informal Chinese sentences)

**Domains**:
- Natural Language Processing
- Recommender Systems
- Social Network Analysis

**Languages**:
- Chinese (Simplified)

**Similar Benchmarks**:
- Weibo News
- Sougou News
- People’s Daily
- Baidu Encyclopedia
- Sina Weibo News

**Resources**:
- [Resource](https://arxiv.org/abs/1811.10167)
- [GitHub Repository](https://github.com/JaniceZhao/Douban-Dushu-Dataset.git)
- [GitHub Repository](https://github.com/JaniceZhao/Chinese-Forum-Corpus.git)

## 🎯 Purpose and Intended Users

**Goal**: Construct a large-scale informal Chinese dataset (LSICC) and analyze informal word frequency differences between LSICC and existing Chinese corpora; provide a dataset suitable for training deep learning based NLP tasks such as Chinese word segmentation and sentiment analysis.

**Tasks**:
- Chinese Word Segmentation
- Sentiment Analysis
- Recommendation Systems
- Social Network Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Collected from DouBan DuShu (book reviews) and Chiphell (forum discussions).

**Size**: Around 37 million short comments (from ~18,000 books and ~1,000,000 users) and more than 50,000 discussions.

**Format**: Cleaned text; preprocessed (Traditional Chinese converted to Simplified Chinese; over-short comments removed; special characters/English words/emoticons identified).

**Annotation**: No manual annotation described; contains user-provided metadata such as star ratings for DouBan DuShu comments.

## 🔬 Methodology

**Methods**:
- Manual collection of 70 informal words as a benchmark
- Automated word frequency counting of the 70 informal words
- Comparative analysis of informal word proportions across corpora

**Metrics**:
- Informal word frequency (count)
- Total word count
- Proportion of informal words (informal words / total words, expressed as per mille)

**Calculation**: Count frequencies of the 70 manually collected informal words and the total number of words in each corpus; compute proportion = informal word count / total word count (expressed in per mille).

**Interpretation**: Higher proportion of informal words indicates a corpus is more representative of informal Chinese. LSICC has the highest proportion among compared corpora, indicating greater informality and suitability for informal-language tasks.

**Baseline Results**: LSICC: 621,807 informal words; 705,231,306 total words; proportion 8.82‰. Weibo News: 46,831 informal words; 125,082,112 total words; proportion 3.74‰. Sougou News: 1,238 informal words; 14,160,148 total words; proportion 0.87‰. People’s Daily: 25 informal words; 3,482,887 total words; proportion 0.07‰.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
