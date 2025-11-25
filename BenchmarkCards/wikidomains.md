# WIKIDOMAINS

## 📊 Benchmark Details

**Name**: WIKIDOMAINS

**Overview**: WIKIDOMAINS is a dataset of 22k definitions from 13 academic domains paired with a difficult concept within each definition, designed to support targeted concept simplification for readers encountering domain-specific text.

**Data Type**: definition pairs

**Domains**:
- Natural Language Processing
- Computer Science
- Biology
- Chemistry
- Physics
- Mathematics
- Medicine
- Business
- Economics
- Engineering
- Environmental Science
- Political Science
- Performing Arts

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/google-deepmind/wikidomains)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate reading comprehension by helping readers understand difficult concepts within domain-specific definitions.

**Target Audience**:
- Researchers
- NLP practitioners
- Educators
- Learners

**Tasks**:
- Text Simplification

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia articles containing definitions across 13 academic domains.

**Size**: 22,561 definitions

**Format**: JSON

**Annotation**: Automatically annotated difficult concepts using a heuristic.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Meaning preservation
- Rewrite understanding
- Rewrite easier
- BLEU Score
- BERTSCORE

**Calculation**: Metrics calculated using human evaluations and comparison to original definitions.

**Interpretation**: Higher scores indicate better performance in preserving meaning and ease of understanding.

**Baseline Results**: Dictionary baseline showed comparable performance to the best LLMs.

**Validation**: Results validated with human judgments and correlation with automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
