# The Pushshift Reddit Dataset

## 📊 Benchmark Details

**Name**: The Pushshift Reddit Dataset

**Overview**: In this paper, we present the Pushshift Reddit dataset. Pushshift is a social media data collection, analysis, and archiving platform that since 2015 has collected Reddit data and made it available to researchers. Pushshift’s Reddit dataset is updated in real-time, and includes historical data back to Reddit’s inception. In addition to monthly dumps, Pushshift provides computational tools to aid in searching, aggregating, and performing exploratory analysis on the entirety of the dataset.

**Data Type**: text (submissions and comments; newline-delimited JSON)

**Domains**:
- Computational Social Science
- Web Science
- Health Informatics
- Natural Language Processing

**Similar Benchmarks**:
- Media Cloud
- GDELT
- StatsExchange
- Wikimedia

**Resources**:
- [Resource](https://files.pushshift.io/reddit/)
- [Resource](https://pushshift.io/api-parameters/)
- [Resource](https://doi.org/10.5281/zenodo.3608135)

## 🎯 Purpose and Intended Users

**Goal**: To provide open APIs and monthly data dumps of Reddit submissions and comments to researchers, reducing time spent on data collection, cleaning, and storage and enabling queries, aggregation, and exploratory analysis.

**Target Audience**:
- Social media researchers
- Computational social science researchers
- Web science researchers
- Health informatics researchers
- Natural Language Processing researchers
- Extremism and disinformation researchers
- Research teams and the broader research community

**Tasks**:
- Text Classification
- Topic Modeling
- Named Entity Recognition
- Summarization
- Recommender Systems
- Conversational Agent Training
- Network Analysis

**Limitations**: Unable to upload the entire dataset to Zenodo due to Zenodo's 100GB limit; the full dataset is in the order of several terabytes.

## 💾 Data

**Source**: All submissions and comments posted on Reddit between June 2005 and April 2019, collected and archived by the Pushshift platform.

**Size**: 651,778,198 submissions; 5,601,331,385 comments; 2,888,885 subreddits; dataset size: in the order of several terabytes.

**Format**: Newline-delimited JSON (ndjson); monthly files (one file per month for submissions and one file per month for comments).

**Annotation**: No manual annotation; raw Reddit data and metadata as provided by Reddit (JSON fields described in Tables 1 and 2).

## 🔬 Methodology

**Methods**:
- Automated data collection via Pushshift ingest engine
- Storage in PostgreSQL and Elasticsearch for indexing and aggregation
- Provision of an API with search and aggregation endpoints
- Monthly data dumps (files.pushshift.io)

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Legal Compliance
- Accuracy
- Data Access / Data Laws
- Governance

**Atlas Risks**:
- **Data Laws**: Data acquisition restrictions, Data usage restrictions
- **Accuracy**: Unrepresentative data
- **Legal Compliance**: Legal accountability
- **Privacy**: Data privacy rights alignment
- **Governance**: Lack of data transparency

**Demographic Analysis**: N/A

**Potential Harm**: ['Discrimination', 'Harassment', 'Radicalization', 'Hate speech', 'Disinformation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Users are asked to cite Pushshift in order to use the data; explicit license not specified in paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
