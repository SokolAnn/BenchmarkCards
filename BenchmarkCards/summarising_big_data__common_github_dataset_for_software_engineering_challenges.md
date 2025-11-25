# Summarising Big Data: Common GitHub Dataset for Software Engineering Challenges

## 📊 Benchmark Details

**Name**: Summarising Big Data: Common GitHub Dataset for Software Engineering Challenges

**Overview**: A common dataset was created and shared with the researchers by localizing and filtering a copy of the GHTorrent dataset (GitHub data up to 2015), removing duplicates and errors, adding linking fields, and producing a MongoDB dataset exported as CSV to enable rapid experiments and comparable studies on software engineering problems.

**Data Type**: text, tabular, graph

**Domains**:
- Software Engineering
- Natural Language Processing

**Similar Benchmarks**:
- GHTorrent

**Resources**:
- [Resource](https://en.wikipedia.org/wiki/gitHub)
- [GitHub Repository](https://gist.github.com/paulmillr/2657075)

## 🎯 Purpose and Intended Users

**Goal**: Provide a common, smaller, easy-to-operate GitHub dataset (filtered from GHTorrent up to 2015) to allow researchers to work on many software engineering problems and to enable comparable evaluation between studies.

**Target Audience**:
- Researchers working on Software Engineering
- Researchers working on Natural Language Processing

**Tasks**:
- Task assignment
- User analysis
- Project analysis
- Software development analysis

**Limitations**: Dataset includes data associated only with the 100 selected most active users and covers GitHub data up to 2015.

## 💾 Data

**Source**: Filtered subset of the GHTorrent dataset (GitHub data up to 2015), processed in MongoDB to correct errors, remove duplicates, add linking fields, and exported for sharing.

**Size**: Authors downloaded approximately 750 GB of GHTorrent MongoDB collections. Proposed filtered dataset sizes per Table 3: Users 0.8 MB; Repos 45 MB; Commits 4 GB; Commit Comments 90 MB; Issues 3 GB; Issue Comments 4 GB; Pull Requests 5 GB; Pull Request Comments 1 GB; Followers 20 MB; Forks 5 MB; Watchers 8 MB; RepoCollaborators 2 MB.

**Format**: MongoDB archive; CSV exports of collections

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Filtering and selection of data based on the 100 most active users using MongoDB queries
- Data cleaning: remove documents with null key fields, remove duplicate documents
- Field engineering: create 'full_name' fields, extract owner/name from URLs, add 'repo_id' and 'user_id' by joining collections
- Export processed MongoDB collections as CSV and share MongoDB archive

**Metrics**:
- N/A

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: Validation performed via data cleaning procedures described in the paper: removal of documents with null key fields, deduplication (grouping by id fields), creation of 'full_name' fields where missing, joining to add 'repo_id' and 'user_id', and comparison of collection sizes with original GHTorrent (Table 3).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
