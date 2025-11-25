# Tamarian-English Parallel Corpus

## 📊 Benchmark Details

**Name**: Tamarian-English Parallel Corpus

**Overview**: This work assembles a Tamarian-English dictionary of utterances and constructs a parallel corpus of 456 English-Tamarian utterances, to investigate the feasibility of translating this metaphor-rich language.

**Data Type**: parallel corpus of utterances

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Tamarian

**Resources**:
- [GitHub Repository](https://github.com/cognitiveailab/darmok)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the feasibility of translating the metaphor-rich constructed language of Tamarian using a parallel corpus.

**Target Audience**:
- ML Researchers
- Linguists
- Domain Experts

**Tasks**:
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Tamarian utterances from the original Star Trek broadcast episode and several licensed novels

**Size**: 456 utterances

**Format**: N/A

**Annotation**: Manually authored examples for each Tamarian utterance

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score

**Calculation**: Translation performance was evaluated using SACRE BLEU and binary classification accuracy.

**Interpretation**: Translation accuracy indicates the percentage of correct translations from English to Tamarian.

**Baseline Results**: Best performing model achieves a translation accuracy of 76% on unseen test set.

**Validation**: 5-fold cross-validation with 60% of data used for training, 20% for development, 20% for testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Translation Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
