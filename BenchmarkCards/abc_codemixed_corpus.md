# ABC Codemixed Corpus

## 📊 Benchmark Details

**Name**: ABC Codemixed Corpus

**Overview**: The ABC Codemixed Corpus is the first labeled and general-purpose corpus for understanding code-mixing in context, with over 355,641 messages focused on English, Mandarin, and other languages, aimed at facilitating research in computational linguistics, sociolinguistics, and NLP applications.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Sociolinguistics

**Languages**:
- English
- Mandarin
- Tamil
- Malay
- Hokkien
- Japanese
- Korean

**Similar Benchmarks**:
- L3Cube-HingCorpus
- TweetTaglish
- NSC

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To study how private message communication varies across different levels of interpersonal intimacy, with a particular focus on the use of code-mixing.

**Target Audience**:
- ML Researchers
- Sociolinguists

**Tasks**:
- Code-Mixing Analysis
- Sociolinguistic Studies
- Relationship Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected through voluntary donations from Singaporean university students sharing private instant messaging conversations.

**Size**: 355,641 messages

**Format**: JSON

**Annotation**: Messages annotated for language identification and relational dynamics based on participant metadata.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated language tagging
- Statistical analysis

**Metrics**:
- Cohen’s Kappa
- BLEU Score

**Calculation**: Correlations were computed to analyze the relationships between code-mixing and linguistic features using Pearson correlations and PCA.

**Interpretation**: High percentage of code-mixing correlates with informal, expressive, and socially-oriented discourse.

**Validation**: Validation through stratified random sampling and comparison with existing tagging methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of participant demographics included gender and age breakdowns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization measures were implemented to protect personally identifiable information.

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0).

**Consent Procedures**: Informed consent obtained through voluntary data donation protocols.

**Compliance With Regulations**: Complied with ethical review processes to ensure responsible data collection.
