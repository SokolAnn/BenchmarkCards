# Phoenix event dataset

## 📊 Benchmark Details

**Name**: Phoenix event dataset

**Overview**: A next-generation, daily-updated, near-real-time political event dataset named Phoenix that builds on advances in open-source natural language processing and news collection to produce reproducible, CAMEO-coded who-did-what-to-whom event records. The dataset improves the news collection process and event coding software and provides a processing pipeline to produce daily-updated data.

**Data Type**: text (news article text) and structured event records (CAMEO-coded events)

**Domains**:
- Natural Language Processing
- Political Science
- International Relations

**Languages**:
- English

**Similar Benchmarks**:
- Integrated Crisis Early Warning System (ICEWS)
- Global Database of Events, Language, and Tone (GDELT)

**Resources**:
- [Resource](https://arxiv.org/abs/1612.00866)
- [GitHub Repository](https://github.com/openeventdata/scraper)
- [GitHub Repository](https://github.com/johnb30/atlas)
- [GitHub Repository](https://github.com/openeventdata/Dictionaries)
- [GitHub Repository](https://github.com/openeventdata/petrarch2/blob/1.0.0/petrarch2/utilities.py#L265)
- [GitHub Repository](https://github.com/openeventdata/eldiablo)
- [GitHub Repository](https://github.com/caerusassociates/hypnos)
- [GitHub Repository](https://github.com/grangier/python-goose)
- [Resource](http://cliff.mediameter.org/)
- [Resource](https://clavin.bericotechnologies.com/)
- [Resource](https://www.docker.com/)
- [Resource](http://dx.doi.org/10.7910/DVN/28075)
- [Resource](http://www.aclweb.org/anthology/P/P14/P14-5010)

## 🎯 Purpose and Intended Users

**Goal**: To create a reproducible, near-real-time political event dataset using open-source NLP (CoreNLP), new event coding software (PETRARCH/PETRARCH2), and an automated scraping and processing pipeline so that daily-updated event data can be produced and used for applications such as monitoring ongoing events.

**Target Audience**:
- Analysts
- Researchers
- Event data community

**Tasks**:
- Event Extraction
- Information Extraction
- Event Coding (CAMEO)
- Geolocation of events

**Limitations**: Geolocation is not fully implemented/accurate; processing time is high due to deep parsing; requires human-in-the-loop updates for actor dictionaries; realtime scraping can experience server failures or scraper bugs causing drops in data; no publicly-available gold standard is available for definitive validation.

**Out of Scope Uses**:
- The dataset should not be used as a direct representation of on-the-ground truth (event counts reflect media coverage rather than ground truth).

## 💾 Data

**Source**: Scraped content from 450 English-language news sites (RSS-based scraping) ingested hourly; processed with Stanford CoreNLP for deep parses; event coding performed with PETRARCH and PETRARCH2 using the CAMEO ontology; actor dictionaries from the Open Event Data project; geolocation via CLIFF and CLAVIN heuristics.

**Size**: 254,060 events over 102 days (examined sample); average ~2,200 events per day; data sourced from 450 English-language news sites.

**Format**: Tabular (27 columns: EventID, Date, Year, Month, Day, SourceActorFull, SourceActorEntity, SourceActorRole, SourceActorAttribute, TargetActorFull, TargetActorEntity, TargetActorRole, TargetActorAttribute, EventCode, EventRootCode, QuadClass, GoldsteinScore, Issues, ActionLat, ActionLong, Location-Name, GeoCountryName, GeoStateName, SentenceID, URLs, NewsSources)

**Annotation**: Automatically coded using PETRARCH/PETRARCH2 with the CAMEO ontology; issue coding via keyword lookups; geolocation via CLIFF/CLAVIN heuristics; actor dictionaries maintained/updated by project contributors (human updates required for new actors).

## 🔬 Methodology

**Methods**:
- Automated event coding (PETRARCH and PETRARCH2)
- Deep syntactic parsing using Stanford CoreNLP
- Realtime web scraping via RSS (atlas scraper)
- Geolocation using CLIFF and CLAVIN heuristics
- Issue coding via keyword lookup
- Reproducible deployment tools: EL:DIABLO (VM setup) and hypnos (Dockerized REST API)

**Metrics**:
- Event counts (events per day)
- Goldstein Score (event intensity score)
- QuadClass distribution
- Pearson correlation between Phoenix and ICEWS daily event counts

**Calculation**: Correlation between Phoenix and ICEWS daily event counts computed over overlapping period; reported overall Pearson correlation = 0.31, rising to 0.49 when days with fewer than 1,000 Phoenix events are excluded. Event counts are aggregated per day. GoldsteinScore is the standard scale used in prior datasets (as implemented in Phoenix). QuadClass derived from mapped CAMEO root categories into classes 0-4 as described in the paper.

**Interpretation**: Higher daily event counts indicate more media-reported events; QuadClass and GoldsteinScore provide event valence/intensity measures; Pearson correlation with ICEWS is used to assess similarity of aggregated signal but does not imply ground-truth accuracy. Face validity assessed via case study (Syria subset).

**Baseline Results**: Phoenix: 254,060 events over 102 days (average ~2,200 events/day). Comparison with ICEWS over overlapping period shows broad similarity; Pearson correlation = 0.31 overall, 0.49 when excluding days with <1,000 Phoenix events.

**Validation**: Face validity checks (case study on Syria) and system/data-level comparison to ICEWS. No public gold-standard ground-truth dataset available for definitive validation; referenced IARPA OSI ground-truth work is not publicly available.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Governance

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Transparency**: Uncertain data provenance
- **Governance**: Lack of data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
