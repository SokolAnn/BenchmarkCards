# Arap-Tweet: A Large Multi-Dialect Twitter Corpus for Gender, Age and Language Variety Identification

## 📊 Benchmark Details

**Name**: Arap-Tweet: A Large Multi-Dialect Twitter Corpus for Gender, Age and Language Variety Identification

**Overview**: we present Arap-Tweet, which is a large-scale and multi-dialectal corpus of Tweets from 11 regions and 16 countries in the Arab world representing the major Arabic dialectal varieties. To build this corpus, we collected data from Twitter and we provided a team of experienced annotators with annotation guidelines that they used to annotate the corpus for age categories, gender, and dialectal variety.

**Data Type**: text (tweets) with author metadata labels (age category, gender, dialect)

**Domains**:
- Natural Language Processing
- Cyber-security
- Business
- Healthcare

**Languages**:
- Arabic

**Similar Benchmarks**:
- MADAR Arabic Dialect Corpus and Lexicon
- Mubarak & Darwish (2014) Twitter dialectal Arabic corpus
- PAN 2017 Author Profiling dialectal Arabic corpus
- YouDACC (Youtube Dialectal Arabic Comment Corpus)

**Resources**:
- [Resource](http://arap.qatar.cmu.edu)
- [Resource](https://how-old.net/)
- [Resource](http://pan.webis.de/clef17/pan17-web/author-profiling.html)

## 🎯 Purpose and Intended Users

**Goal**: developing author profiling resources and tools for the Arabic language and building a multi-dialectal annotated corpus to annotate Tweets for age categories, gender, and dialectal variety.

**Target Audience**:
- Research community
- Natural Language Processing researchers
- Cyber-security and forensic investigators
- Industry practitioners (marketing / customer segmentation)
- Healthcare practitioners (e.g., suicide prevention)

**Tasks**:
- Author Profiling
- Age Classification
- Gender Identification
- Dialect Identification
- Authorship Attribution
- Sentiment Analysis
- Deception Detection
- Topic Detection

**Limitations**: Age identification is a much more difficult task and annotation agreement is lower for age (Kappa=0.80). Coverage is limited to 11 regions (16 countries) out of 22 Arab League countries. Some sampled accounts became private between sampling and collection; selection avoided well-known public figures resulting in a smaller user sample.

## 💾 Data

**Source**: Collected from Twitter using Twitter API and Twitter Stream API; profiles sampled via dialect-specific seed words and manual review; external resources (LinkedIn, Facebook, user blogs) and profile photos (including Microsoft How-Old.net) were used to assist annotation.

**Size**: Approximately 2.4M tweets corpus; 1,100 users (100 users per region for 11 regions); minimum of 200K tweets per region; up to 3,240 tweets downloaded per user (Twitter API limit).

**Format**: N/A

**Annotation**: Manual annotation by trained university-level annotators following documented annotation guidelines; annotation manager oversaw the process; annotations for age (three categories: under 25, 25-34, above 35), gender (male/female), and dialect region; annotators were trained and piloted prior to full annotation; external resources and How-Old.net used when available.

## 🔬 Methodology

**Methods**:
- Manual annotation with annotation guidelines and pilot annotation
- Inter-Annotator Agreement evaluation

**Metrics**:
- Cohen's kappa
- Inter-Annotator Agreement (IAA)

**Calculation**: Inter-annotator agreement was measured using Cohen's kappa on a sample of 110 accounts annotated blindly by three annotators.

**Interpretation**: A value above 0.75 is considered acceptable. Reported average Kappa values: gender annotation 0.95 (acceptable), age annotation 0.80 (borderline/needs improvement), dialect annotation 0.92 (acceptable).

**Baseline Results**: Inter-annotator agreement (average Cohen's kappa): Gender = 0.95; Age = 0.80; Dialect = 0.92.

**Validation**: Quality validated via weekly inter-annotator agreement measurements and a blind evaluation sample of 110 accounts annotated by three annotators; annotators were trained and pilot annotation was conducted.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Dataset includes age group and gender breakdowns (Age groups: under 25, 25-34, above 35). Reported totals: Male 667, Female 433. Gender/age table provided; gender ratio nearly equal for 7 regions; for 4 regions about 60% male and 40% female on average.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only publicly accessible Twitter profiles were included. No anonymization procedures are described in the paper.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
