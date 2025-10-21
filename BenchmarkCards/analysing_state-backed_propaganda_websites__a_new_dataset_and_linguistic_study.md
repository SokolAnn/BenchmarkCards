# Analysing State-Backed Propaganda Websites: a New Dataset and Linguistic Study

## 📊 Benchmark Details

**Name**: Analysing State-Backed Propaganda Websites: a New Dataset and Linguistic Study

**Overview**: This paper provides a new dataset of articles from two state-backed disinformation websites, enabling studies of disinformation networks and the training of NLP tools for disinformation detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Chinese
- English
- French
- German
- Spanish

**Resources**:
- [Resource](https://zenodo.org/records/10007383)
- [GitHub Repository](https://github.com/GateNLP/wordpress-site-extractor)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate further research in disinformation analysis and to aid in the training of NLP tools for disinformation detection.

**Target Audience**:
- NLP Researchers
- Data Scientists
- Policy Makers

**Limitations**: The dataset may not be fully representative of all types of Russian disinformation due to the limited number of sources included.

## 💾 Data

**Source**: Data was collected from two state-backed disinformation websites: Reliable Recent News (rrn.world) and WarOnFakes (waronfakes.com) using the WordPress REST API.

**Size**: 14,053 articles

**Format**: N/A

**Annotation**: Articles were annotated with metadata including language versions and links.

## 🔬 Methodology

**Methods**:
- Topic clustering
- Linguistic analysis
- Temporal analysis

**Metrics**:
- Count of articles
- Mean sentence length
- Topic assignment effectiveness

**Calculation**: Metrics were calculated based on analysis of article content and clustering of topics using BERTopic.

**Interpretation**: The dataset allows for the analysis of topics, publication times, and linguistic properties of state-backed disinformation.

**Baseline Results**: N/A

**Validation**: The topic analysis has not been formally validated against expert annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: The dataset may contain disturbing or distressing content related to disinformation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection followed institutional ethics policy, ensuring no personally identifiable information was collected.

**Data Licensing**: Dataset is released under a license that prohibits commercial activity.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
