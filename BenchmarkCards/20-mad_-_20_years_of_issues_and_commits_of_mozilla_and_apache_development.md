# 20-MAD - 20 Years of Issues and Commits of Mozilla and Apache Development

## 📊 Benchmark Details

**Name**: 20-MAD - 20 Years of Issues and Commits of Mozilla and Apache Development

**Overview**: This paper presents 20-MAD, a dataset linking the commit and issue data of Mozilla and Apache projects. It includes over 20 years of information about 765 projects, 3.4M commits, 2.3M issues, and 17.3M issue comments, and its compressed size is over 6 GB. The data contains typical information about source code commits (e.g., lines added and removed, message and commit time) and issues (status, severity, votes, and summary). The issue comments have been pre-processed for natural language processing and sentiment analysis (including emoticons and valence and arousal scores). Linking code repository and issue tracker information allows studying individuals in two types of repositories and provides more accurate time zone information for issue trackers.

**Data Type**: text (issue comments) and tabular (commit and issue metadata)

**Domains**:
- Software Engineering
- Natural Language Processing

**Similar Benchmarks**:
- The JIRA Repository Dataset

**Resources**:
- [GitHub Repository](https://github.com/M3SOulu/MozillaApacheDataset/releases/tag/msr2020)
- [Resource](https://hub.docker.com/repository/docker/claesmaelick/mozilla-apache-dataset)
- [Resource](https://doi.org/10.17605/OSF.IO/KVXR4)
- [Resource](https://doi.org/10.17605/OSF.IO/SR56U)
- [GitHub Repository](https://github.com/M3SOulu/EmoticonFindeR)
- [Resource](https://doi.org/10.1145/3379597.3387487)

## 🎯 Purpose and Intended Users

**Goal**: Provide a linked dataset of commits and issue tracker data from Mozilla and Apache spanning more than 20 years to enable repository mining tasks such as studying developers' weekly and daily work patterns, large scale sentiment analysis, analysis of emoticon usage by software developers, and NLP tasks on comments; and to enable creation of software engineering language models not based on StackOverflow.

**Target Audience**:
- Software Engineering researchers
- Natural Language Processing researchers

**Tasks**:
- Sentiment Analysis
- Natural Language Processing of issue comments
- Analysis of Developer Activity (weekly and daily work patterns)
- Language Modeling for Software Engineering

**Limitations**: Not exhaustive (some Apache projects missing, e.g., Apache httpd not included). Timestamp information incomplete due to prior use of SVN/CVS and missing time zone information. Identity merging is rudimentary and was only manually checked for the most active developers (previously >100 commits, re-checked for >1000 commits). NLoN's prediction model has not been retrained with Apache data leading to some non natural language Apache comments being considered natural language. The issue description was not consistently included in the NLP pipeline for Apache.

## 💾 Data

**Source**: Mozilla Bugzilla (https://bugzilla.mozilla.org/), Apache Jira (https://issues.apache.org/jira), Mozilla Git repositories (gecko-dev: https://github.com/mozilla/gecko-dev, comm-central: https://github.com/mozilla/releases-comm-central), Apache Git repositories (list parsed from Apache project listings). Data extracted using Perceval and stored as Parquet files.

**Size**: 765 projects; 3.4M commits; 2.3M issues; 17.3M issue comments; compressed size over 6 GB; spans commits back to 1998 and issues back to 1994 for Mozilla and commits back to 1998 and issues back to 2003 for Apache.

**Format**: Apache Parquet files (original exports in JSON; intermediate processing used MongoDB and JSON), compressed dataset stored as Parquet.

**Annotation**: Semi-automatic identity merging with manual verification for high-activity developers; NLP preprocessing including text line classification (NLoN), natural language filtering, paragraph grouping, emoticon detection (custom R package), sentence detection (R package tokenizers), and automated sentiment analysis using SentiStrength and Senti4SD.

## 🔬 Methodology

**Methods**:
- Data extraction using Perceval
- Semi-automatic identity merging (graph-based) with manual verification
- Timezone inference/matching from commits to issue tracker timestamps
- Natural Language Processing: NLoN for NL detection, tokenizers for sentence splitting, emoticon extraction (custom R package), SentiStrength, and Senti4SD for sentiment analysis
- Storage as Apache Parquet files
- Docker image provided for replication

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: Identity merging was manually verified for developers with more than 100 commits in the previous version and re-checked for developers with more than 1000 commits for the updated version. Time zone coverage statistics are reported (e.g., 78.7% of Mozilla commit time zones and 59.8% of Apache commit time zones usable; inferred time zones for portions of issue and comment timestamps). NLP processing used established tools (NLoN, tokenizers, SentiStrength, Senti4SD); processing estimates (e.g., ~20 days on a laptop) and HPC timings are reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: Table 1 reports numbers and percentages of developer and issue tracker profiles linked (e.g., # developers without merging, # merged developers, # issue tracker profiles, % developers in issue tracker, % commits from developers in issue tracker, % comments from developers).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: For data protection, user personal information is anonymized in the dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
